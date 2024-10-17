"""Kubernetes Interface for Supervisor."""

from kubernetes import client, config
from kubernetes.client import V1Deployment, V1DeploymentSpec, V1PodTemplateSpec, V1ObjectMeta, V1PodSpec, V1Container

class KubernetesInterface:
    """Base class for Kubernetes-related operations."""

    def __init__(self):
        """Initialize Kubernetes interface."""
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
        except client.exceptions.ApiException as e:
            raise Exception(f"Exception when creating deployment: {e}")

    def delete_deployment(self, name: str) -> None:
        """Delete Kubernetes deployment."""
        api_instance = client.AppsV1Api()
        try:
            api_instance.delete_namespaced_deployment(
                name=name,
                namespace="default",
                body=client.V1DeleteOptions()
            )
        except client.exceptions.ApiException as e:
            raise Exception(f"Exception when deleting deployment: {e}")

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
        except client.exceptions.ApiException as e:
            raise Exception(f"Exception when updating deployment: {e}")

    def start_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Start Kubernetes deployment."""
        self.create_deployment(name, image, env)

    def stop_deployment(self, name: str) -> None:
        """Stop Kubernetes deployment."""
        self.delete_deployment(name)

    def restart_deployment(self, name: str, image: str, env: dict[str, str]) -> None:
        """Restart Kubernetes deployment."""
        self.update_deployment(name, image, env)
