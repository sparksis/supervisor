"""Internal network manager for Supervisor."""

from contextlib import suppress
from ipaddress import IPv4Address
import logging

import docker
import requests

from ..const import DOCKER_NETWORK, DOCKER_NETWORK_MASK, DOCKER_NETWORK_RANGE
from ..exceptions import DockerError

_LOGGER: logging.Logger = logging.getLogger(__name__)


class DockerNetwork:
    """Internal Supervisor Network.

    This class is not AsyncIO safe!
    """

    def __init__(self, docker_client: docker.DockerClient):
        """Initialize internal Supervisor network.

        Args:
            docker_client (docker.DockerClient): Docker client instance.
        """
        self.docker: docker.DockerClient = docker_client
        self._network: docker.models.networks.Network = self._get_network()

    @property
    def name(self) -> str:
        """Return name of network.

        Returns:
            str: Name of the network.
        """
        return DOCKER_NETWORK

    @property
    def network(self) -> docker.models.networks.Network:
        """Return docker network.

        Returns:
            docker.models.networks.Network: Docker network instance.
        """
        return self._network

    @property
    def containers(self) -> list[str]:
        """Return list of connected containers from network.

        Returns:
            list[str]: List of connected container IDs.
        """
        return list(self.network.attrs.get("Containers", {}).keys())

    @property
    def gateway(self) -> IPv4Address:
        """Return gateway of the network.

        Returns:
            IPv4Address: Gateway IP address.
        """
        return DOCKER_NETWORK_MASK[1]

    @property
    def supervisor(self) -> IPv4Address:
        """Return supervisor of the network.

        Returns:
            IPv4Address: Supervisor IP address.
        """
        return DOCKER_NETWORK_MASK[2]

    @property
    def dns(self) -> IPv4Address:
        """Return dns of the network.

        Returns:
            IPv4Address: DNS IP address.
        """
        return DOCKER_NETWORK_MASK[3]

    @property
    def audio(self) -> IPv4Address:
        """Return audio of the network.

        Returns:
            IPv4Address: Audio IP address.
        """
        return DOCKER_NETWORK_MASK[4]

    @property
    def cli(self) -> IPv4Address:
        """Return cli of the network.

        Returns:
            IPv4Address: CLI IP address.
        """
        return DOCKER_NETWORK_MASK[5]

    @property
    def observer(self) -> IPv4Address:
        """Return observer of the network.

        Returns:
            IPv4Address: Observer IP address.
        """
        return DOCKER_NETWORK_MASK[6]

    def _get_network(self) -> docker.models.networks.Network:
        """Get supervisor network.

        Returns:
            docker.models.networks.Network: Docker network instance.

        Raises:
            DockerError: If the network cannot be created.
        """
        try:
            return self.docker.networks.get(DOCKER_NETWORK)
        except docker.errors.NotFound:
            _LOGGER.info("Can't find Supervisor network, creating a new network")

        ipam_pool = docker.types.IPAMPool(
            subnet=str(DOCKER_NETWORK_MASK),
            gateway=str(self.gateway),
            iprange=str(DOCKER_NETWORK_RANGE),
        )

        ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])

        try:
            return self.docker.networks.create(
                DOCKER_NETWORK,
                driver="bridge",
                ipam=ipam_config,
                enable_ipv6=False,
                options={"com.docker.network.bridge.name": DOCKER_NETWORK},
            )
        except docker.errors.APIError as err:
            raise DockerError(f"Can't create Supervisor network: {err}", _LOGGER.error) from err

    def attach_container(
        self,
        container: docker.models.containers.Container,
        alias: list[str] | None = None,
        ipv4: IPv4Address | None = None,
    ) -> None:
        """Attach container to Supervisor network.

        Args:
            container (docker.models.containers.Container): Docker container instance.
            alias (list[str] | None, optional): List of aliases for the container. Defaults to None.
            ipv4 (IPv4Address | None, optional): IPv4 address for the container. Defaults to None.

        Raises:
            DockerError: If the container cannot be linked to the network.
        """
        ipv4_address = str(ipv4) if ipv4 else None

        # Reload Network information
        with suppress(docker.errors.DockerException, requests.RequestException):
            self.network.reload()

        # Check stale Network
        if container.name in (
            val.get("Name") for val in self.network.attrs.get("Containers", {}).values()
        ):
            self.stale_cleanup(container.name)

        # Attach Network
        try:
            self.network.connect(container, aliases=alias, ipv4_address=ipv4_address)
        except docker.errors.APIError as err:
            raise DockerError(
                f"Can't link container to hassio-net: {err}", _LOGGER.error
            ) from err

    def detach_default_bridge(
        self, container: docker.models.containers.Container
    ) -> None:
        """Detach default Docker bridge.

        Args:
            container (docker.models.containers.Container): Docker container instance.

        Raises:
            DockerError: If the container cannot be disconnected from the default bridge.
        """
        try:
            default_network = self.docker.networks.get("bridge")
            default_network.disconnect(container)

        except docker.errors.NotFound:
            return

        except docker.errors.APIError as err:
            raise DockerError(
                f"Can't disconnect container from default: {err}", _LOGGER.warning
            ) from err

    def stale_cleanup(self, container_name: str):
        """Remove force a container from Network.

        Fix: https://github.com/moby/moby/issues/23302

        Args:
            container_name (str): Name of the container to remove.

        Raises:
            DockerError: If the container cannot be disconnected from the network.
        """
        try:
            self.network.disconnect(container_name, force=True)
        except docker.errors.NotFound:
            pass
        except (docker.errors.DockerException, requests.RequestException) as err:
            raise DockerError() from err
