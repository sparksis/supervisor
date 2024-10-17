"""Init file for Supervisor Docker object."""

from collections.abc import Awaitable
from ipaddress import IPv4Address
import logging
import os

from awesomeversion.awesomeversion import AwesomeVersion
import docker
import requests

from ..exceptions import DockerError
from ..jobs.const import JobExecutionLimit
from ..jobs.decorator import Job
from .const import PropagationMode
from .interface import DockerInterface

_LOGGER: logging.Logger = logging.getLogger(__name__)


class DockerSupervisor(DockerInterface):
    """Docker Supervisor wrapper for Supervisor.

    This class provides methods to manage the Docker container for the Supervisor, including attaching, retagging, and updating the container.
    """

    @property
    def name(self) -> str:
        """Return name of Docker container.

        Returns:
            str: Docker container name.
        """
        return os.environ["SUPERVISOR_NAME"]

    @property
    def ip_address(self) -> IPv4Address:
        """Return IP address of this container.

        Returns:
            IPv4Address: IP address of the container.
        """
        return self.sys_docker.network.supervisor

    @property
    def privileged(self) -> bool:
        """Return True if the container run with Privileged.

        Returns:
            bool: True if the container runs with Privileged, False otherwise.
        """
        return self.meta_host.get("Privileged", False)

    @property
    def host_mounts_available(self) -> bool:
        """Return True if container can see mounts on host within its data directory.

        Returns:
            bool: True if the container can see mounts on the host within its data directory, False otherwise.
        """
        return self._meta and any(
            mount.get("Propagation") == PropagationMode.SLAVE
            for mount in self.meta_mounts
            if mount.get("Destination") == "/data"
        )

    @Job(name="docker_supervisor_attach", limit=JobExecutionLimit.GROUP_WAIT)
    async def attach(
        self, version: AwesomeVersion, *, skip_state_event_if_down: bool = False
    ) -> None:
        """Attach to running docker container.

        Args:
            version (AwesomeVersion): Version of the Docker image.
            skip_state_event_if_down (bool, optional): Whether to skip state event if the container is down. Defaults to False.

        Raises:
            DockerError: If there is an error during the attachment.
        """
        try:
            docker_container = await self.sys_run_in_executor(
                self.sys_docker.containers.get, self.name
            )
        except (docker.errors.DockerException, requests.RequestException) as err:
            raise DockerError() from err

        self._meta = docker_container.attrs
        _LOGGER.info(
            "Attaching to Supervisor %s with version %s",
            self.image,
            self.sys_supervisor.version,
        )

        # If already attach
        if docker_container.id in self.sys_docker.network.containers:
            return

        # Attach to network
        _LOGGER.info("Connecting Supervisor to hassio-network")
        await self.sys_run_in_executor(
            self.sys_docker.network.attach_container,
            docker_container,
            alias=["supervisor"],
            ipv4=self.sys_docker.network.supervisor,
        )

    @Job(name="docker_supervisor_retag", limit=JobExecutionLimit.GROUP_WAIT)
    def retag(self) -> Awaitable[None]:
        """Retag latest image to version.

        Returns:
            Awaitable[None]: Awaitable object.
        """
        return self.sys_run_in_executor(self._retag)

    def _retag(self) -> None:
        """Retag latest image to version.

        Need run inside executor.

        Raises:
            DockerError: If there is an error during the retagging.
        """
        try:
            docker_container = self.sys_docker.containers.get(self.name)

            docker_container.image.tag(self.image, tag=str(self.version))
            docker_container.image.tag(self.image, tag="latest")
        except (docker.errors.DockerException, requests.RequestException) as err:
            raise DockerError(
                f"Can't retag Supervisor version: {err}", _LOGGER.error
            ) from err

    @Job(name="docker_supervisor_update_start_tag", limit=JobExecutionLimit.GROUP_WAIT)
    def update_start_tag(self, image: str, version: AwesomeVersion) -> Awaitable[None]:
        """Update start tag to new version.

        Args:
            image (str): Docker image name.
            version (AwesomeVersion): Version of the Docker image.

        Returns:
            Awaitable[None]: Awaitable object.
        """
        return self.sys_run_in_executor(self._update_start_tag, image, version)

    def _update_start_tag(self, image: str, version: AwesomeVersion) -> None:
        """Update start tag to new version.

        Need run inside executor.

        Args:
            image (str): Docker image name.
            version (AwesomeVersion): Version of the Docker image.

        Raises:
            DockerError: If there is an error during the update.
        """
        try:
            docker_container = self.sys_docker.containers.get(self.name)
            docker_image = self.sys_docker.images.get(f"{image}:{version!s}")

            # Find start tag
            for tag in docker_container.image.tags:
                start_image = tag.partition(":")[0]
                start_tag = tag.partition(":")[2] or "latest"

                # If version tag
                if start_tag != "latest":
                    continue
                docker_image.tag(start_image, start_tag)
                docker_image.tag(start_image, version.string)

        except (docker.errors.DockerException, requests.RequestException) as err:
            raise DockerError(f"Can't fix start tag: {err}", _LOGGER.error) from err
