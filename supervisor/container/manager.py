"""Container API base class for common container operations."""

import logging
from typing import Any, NamedTuple

_LOGGER: logging.Logger = logging.getLogger(__name__)

class CommandReturn(NamedTuple):
    """Class to represent the return value of a command executed in a container."""
    stdout: str
    stderr: str
    returncode: int

class ContainerAPI:
    """Base class for container operations."""

    def create_container(self, name: str, image: str, env: dict[str, str]) -> None:
        """Create container."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def update_container(self, name: str, image: str, env: dict[str, str]) -> None:
        """Update container."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def delete_container(self, name: str) -> None:
        """Delete container."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_container_logs(self, name: str) -> str:
        """Get container logs."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def execute_command_in_container(self, name: str, command: str) -> Any:
        """Execute command in container."""
        raise NotImplementedError("This method should be overridden by subclasses")
