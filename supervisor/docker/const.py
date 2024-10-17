"""Docker constants."""

from enum import StrEnum

from docker.types import Mount

from ..const import MACHINE_ID


class Capabilities(StrEnum):
    """Linux Capabilities.

    This class defines various Linux capabilities that can be assigned to Docker containers.
    """

    BPF = "BPF"
    DAC_READ_SEARCH = "DAC_READ_SEARCH"
    IPC_LOCK = "IPC_LOCK"
    NET_ADMIN = "NET_ADMIN"
    NET_RAW = "NET_RAW"
    PERFMON = "PERFMON"
    SYS_ADMIN = "SYS_ADMIN"
    SYS_MODULE = "SYS_MODULE"
    SYS_NICE = "SYS_NICE"
    SYS_PTRACE = "SYS_PTRACE"
    SYS_RAWIO = "SYS_RAWIO"
    SYS_RESOURCE = "SYS_RESOURCE"
    SYS_TIME = "SYS_TIME"


class ContainerState(StrEnum):
    """State of supervisor managed docker container.

    This class defines the possible states of a Docker container managed by the supervisor.
    """

    FAILED = "failed"
    HEALTHY = "healthy"
    RUNNING = "running"
    STOPPED = "stopped"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


class RestartPolicy(StrEnum):
    """Restart policy of container.

    This class defines the possible restart policies for Docker containers.
    """

    NO = "no"
    ON_FAILURE = "on-failure"
    UNLESS_STOPPED = "unless-stopped"
    ALWAYS = "always"


class MountType(StrEnum):
    """Mount type.

    This class defines the possible types of mounts for Docker containers.
    """

    BIND = "bind"
    VOLUME = "volume"
    TMPFS = "tmpfs"
    NPIPE = "npipe"


class PropagationMode(StrEnum):
    """Propagation mode, only for bind type mounts.

    This class defines the possible propagation modes for bind type mounts in Docker containers.
    """

    PRIVATE = "private"
    SHARED = "shared"
    SLAVE = "slave"
    RPRIVATE = "rprivate"
    RSHARED = "rshared"
    RSLAVE = "rslave"


ENV_TIME = "TZ"
ENV_TOKEN = "SUPERVISOR_TOKEN"
ENV_TOKEN_OLD = "HASSIO_TOKEN"

LABEL_MANAGED = "supervisor_managed"

MOUNT_DBUS = Mount(
    type=MountType.BIND, source="/run/dbus", target="/run/dbus", read_only=True
)
MOUNT_DEV = Mount(type=MountType.BIND, source="/dev", target="/dev", read_only=True)
MOUNT_DEV.setdefault("BindOptions", {})["ReadOnlyNonRecursive"] = True
MOUNT_DOCKER = Mount(
    type=MountType.BIND,
    source="/run/docker.sock",
    target="/run/docker.sock",
    read_only=True,
)
MOUNT_MACHINE_ID = Mount(
    type=MountType.BIND,
    source=MACHINE_ID.as_posix(),
    target=MACHINE_ID.as_posix(),
    read_only=True,
)
MOUNT_UDEV = Mount(
    type=MountType.BIND, source="/run/udev", target="/run/udev", read_only=True
)
