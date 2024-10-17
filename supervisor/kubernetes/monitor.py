"""Kubernetes Monitor for Supervisor."""

import logging

_LOGGER: logging.Logger = logging.getLogger(__name__)

class KubernetesContainerStateEvent:
    """Class to represent the state of a Kubernetes container."""

    def __init__(self, name: str, state: str, container_id: str, timestamp: int):
        """Initialize Kubernetes container state event."""
        self.name = name
        self.state = state
        self.container_id = container_id
        self.timestamp = timestamp

    def __repr__(self) -> str:
        """Return string representation of the event."""
        return f"<KubernetesContainerStateEvent(name={self.name}, state={self.state}, container_id={self.container_id}, timestamp={self.timestamp})>"
