"""Kubernetes API for Supervisor."""

import logging
from kubernetes import client, config
from kubernetes.client import V1Deployment, V1DeploymentSpec, V1PodTemplateSpec, V1ObjectMeta, V1PodSpec, V1Container

_LOGGER: logging.Logger = logging.getLogger(__name__)

class KubernetesAPI:
    """Manage Kubernetes interactions."""

    def __init__(self):
        """Initialize Kubernetes API."""
        config.load_kube_config()

    def create_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Create Kubernetes deployment."""
        api_instance = client.AppsV1Api()
        container = V1Container(
            name=name,
            image=image,
            env=[client.V1EnvVar(name=key, value=value) for key, value in env.items()]
        )
        template = V1PodTemplateSpec(
            metadata=V1ObjectMeta(labels={"app": name}),
            spec=V1PodSpec(containers=[container])
        )
        spec = V1DeploymentSpec(
            replicas=1,
            template=template,
            selector={'matchLabels': {'app': name}}
        )
        deployment = V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=V1ObjectMeta(name=name),
            spec=spec
        )
        try:
            api_instance.create_namespaced_deployment(
                namespace="default",
                body=deployment
            )
            _LOGGER.info("Deployment %s created", name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when creating deployment: %s\n", e)
            raise Exception(f"Exception when creating deployment: {e}") from e

    def update_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Update Kubernetes deployment."""
        api_instance = client.AppsV1Api()
        container = V1Container(
            name=name,
            image=image,
            env=[client.V1EnvVar(name=key, value=value) for key, value in env.items()]
        )
        template = V1PodTemplateSpec(
            metadata=V1ObjectMeta(labels={"app": name}),
            spec=V1PodSpec(containers=[container])
        )
        spec = V1DeploymentSpec(
            replicas=1,
            template=template,
            selector={'matchLabels': {'app': name}}
        )
        deployment = V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=V1ObjectMeta(name=name),
            spec=spec
        )
        try:
            api_instance.patch_namespaced_deployment(
                name=name,
                namespace="default",
                body=deployment
            )
            _LOGGER.info("Deployment %s updated", name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when updating deployment: %s\n", e)
            raise Exception(f"Exception when updating deployment: {e}") from e

    def delete_deployment(self, name: str) -> None:
        """Delete Kubernetes deployment."""
        api_instance = client.AppsV1Api()
        try:
            api_instance.delete_namespaced_deployment(
                name=name,
                namespace="default",
                body=client.V1DeleteOptions()
            )
            _LOGGER.info("Deployment %s deleted", name)
        except client.exceptions.ApiException as e:
            _LOGGER.error("Exception when deleting deployment: %s\n", e)
            raise Exception(f"Exception when deleting deployment: {e}") from e

    def start_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Start Kubernetes deployment."""
        self.create_deployment(name, image, env)

    def stop_deployment(self, name: str) -> None:
        """Stop Kubernetes deployment."""
        self.delete_deployment(name)

    def restart_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Restart Kubernetes deployment."""
        self.update_deployment(name, image, env)
