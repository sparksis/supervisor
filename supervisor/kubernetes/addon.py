"""Kubernetes Addon for Supervisor."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from kubernetes import client, config
from kubernetes.client import V1Deployment, V1DeploymentSpec, V1PodTemplateSpec, V1ObjectMeta, V1PodSpec, V1Container

from ..addons.addon import Addon
from ..coresys import CoreSys
from ..exceptions import KubernetesError

if TYPE_CHECKING:
    from ..addons.addon import Addon

_LOGGER: logging.Logger = logging.getLogger(__name__)

class KubernetesAddon:
    """Kubernetes Supervisor wrapper for Home Assistant."""

    def __init__(self, coresys: CoreSys, addon: Addon):
        """Initialize Kubernetes Home Assistant wrapper."""
        self.addon: Addon = addon
        self.coresys: CoreSys = coresys
        config.load_kube_config()

    @staticmethod
    def slug_to_name(slug: str) -> str:
        """Convert slug to deployment name."""
        return f"addon-{slug}"

    @property
    def name(self) -> str:
        """Return name of Kubernetes deployment."""
        return KubernetesAddon.slug_to_name(self.addon.slug)

    def create_deployment(self) -> None:
        """Create Kubernetes deployment for the addon."""
        api_instance = client.AppsV1Api()
        container = V1Container(
            name=self.name,
            image=self.addon.image,
            ports=[client.V1ContainerPort(container_port=80)],
            env=[client.V1EnvVar(name="SUPERVISOR_TOKEN", value=self.addon.supervisor_token)]
        )
        template = V1PodTemplateSpec(
            metadata=V1ObjectMeta(labels={"app": self.name}),
            spec=V1PodSpec(containers=[container])
        )
        spec = V1DeploymentSpec(
            replicas=1,
            template=template,
            selector={'matchLabels': {'app': self.name}}
        )
        deployment = V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=V1ObjectMeta(name=self.name),
            spec=spec
        )
        try:
            api_instance.create_namespaced_deployment(
                namespace="default",
                body=deployment
            )
            _LOGGER.info("Deployment %s created", self.name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when creating deployment: %s\n", e)
            raise KubernetesError() from e

    def delete_deployment(self) -> None:
        """Delete Kubernetes deployment for the addon."""
        api_instance = client.AppsV1Api()
        try:
            api_instance.delete_namespaced_deployment(
                name=self.name,
                namespace="default",
                body=client.V1DeleteOptions()
            )
            _LOGGER.info("Deployment %s deleted", self.name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when deleting deployment: %s\n", e)
            raise KubernetesError() from e

    def update_deployment(self) -> None:
        """Update Kubernetes deployment for the addon."""
        api_instance = client.AppsV1Api()
        container = V1Container(
            name=self.name,
            image=self.addon.image,
            ports=[client.V1ContainerPort(container_port=80)],
            env=[client.V1EnvVar(name="SUPERVISOR_TOKEN", value=self.addon.supervisor_token)]
        )
        template = V1PodTemplateSpec(
            metadata=V1ObjectMeta(labels={"app": self.name}),
            spec=V1PodSpec(containers=[container])
        )
        spec = V1DeploymentSpec(
            replicas=1,
            template=template,
            selector={'matchLabels': {'app': self.name}}
        )
        deployment = V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=V1ObjectMeta(name=self.name),
            spec=spec
        )
        try:
            api_instance.patch_namespaced_deployment(
                name=self.name,
                namespace="default",
                body=deployment
            )
            _LOGGER.info("Deployment %s updated", self.name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when updating deployment: %s\n", e)
            raise KubernetesError() from e

    def start(self) -> None:
        """Start the Kubernetes deployment for the addon."""
        self.create_deployment()
        _LOGGER.info("Kubernetes deployment %s started", self.name)

    def stop(self) -> None:
        """Stop the Kubernetes deployment for the addon."""
        self.delete_deployment()
        _LOGGER.info("Kubernetes deployment %s stopped", self.name)

    def restart(self) -> None:
        """Restart the Kubernetes deployment for the addon."""
        self.update_deployment()
        _LOGGER.info("Kubernetes deployment %s restarted", self.name)
