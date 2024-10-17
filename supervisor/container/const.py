"""Constants for container operations."""

from enum import Enum

class ContainerState(Enum):
    """Container states."""

    UNKNOWN = "unknown"
    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED = "paused"
    RESTARTING = "restarting"
    REMOVING = "removing"
    DEAD = "dead"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    FAILED = "failed"

class RestartPolicy(Enum):
    """Restart policies."""

    NO = "no"
    ON_FAILURE = "on-failure"
    ALWAYS = "always"
    UNLESS_STOPPED = "unless-stopped"
