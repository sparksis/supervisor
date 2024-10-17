# Supervisor Docker Package API Specification

This document provides a comprehensive breakdown of the public APIs in the `supervisor/docker` package. It includes detailed descriptions of each API and their usage.

## Table of Contents

- [DockerAddon](#dockeraddon)
- [DockerAudio](#dockeraudio)
- [DockerCli](#dockercli)
- [DockerDNS](#dockerdns)
- [DockerHomeAssistant](#dockerhomeassistant)
- [DockerInterface](#dockerinterface)
- [DockerAPI](#dockerapi)
- [DockerMonitor](#dockermonitor)
- [DockerMulticast](#dockermulticast)
- [DockerNetwork](#dockernetwork)
- [DockerObserver](#dockerobserver)
- [DockerStats](#dockerstats)
- [DockerSupervisor](#dockersupervisor)

## DockerAddon

The `DockerAddon` class is a Docker Supervisor wrapper for Home Assistant add-ons. It provides methods to manage Docker containers for add-ons, including running, updating, and stopping containers.

### Methods

- `__init__(self, coresys: CoreSys, addon: Addon)`: Initialize Docker Home Assistant wrapper.
- `slug_to_name(slug: str) -> str`: Convert slug to container name.
- `image(self) -> str | None`: Return name of Docker image.
- `ip_address(self) -> IPv4Address`: Return IP address of this container.
- `timeout(self) -> int`: Return timeout for Docker actions.
- `version(self) -> AwesomeVersion`: Return version of Docker image.
- `arch(self) -> str`: Return arch of Docker image.
- `name(self) -> str`: Return name of Docker container.
- `environment(self) -> dict[str, str | None]`: Return environment for Docker add-on.
- `cgroups_rules(self) -> list[str] | None`: Return a list of needed cgroups permission.
- `ports(self) -> dict[str, str | int | None] | None`: Filter None from add-on ports.
- `security_opt(self) -> list[str]`: Control security options.
- `tmpfs(self) -> dict[str, str] | None`: Return tmpfs for Docker add-on.
- `network_mapping(self) -> dict[str, IPv4Address]`: Return hosts mapping.
- `network_mode(self) -> str | None`: Return network mode for add-on.
- `pid_mode(self) -> str | None`: Return PID mode for add-on.
- `uts_mode(self) -> str | None`: Return UTS mode for add-on.
- `capabilities(self) -> list[Capabilities] | None`: Generate needed capabilities.
- `ulimits(self) -> list[docker.types.Ulimit] | None`: Generate ulimits for add-on.
- `cpu_rt_runtime(self) -> int | None`: Limit CPU real-time runtime in microseconds.
- `mounts(self) -> list[Mount]`: Return mounts for container.
- `run(self) -> None`: Run Docker image.
- `update(self, version: AwesomeVersion, image: str | None = None, latest: bool = False, arch: CpuArch | None = None) -> None`: Update a docker image.
- `install(self, version: AwesomeVersion, image: str | None = None, latest: bool = False, arch: CpuArch | None = None, *, need_build: bool | None = None) -> None`: Pull Docker image or build it.
- `_build(self, version: AwesomeVersion, image: str | None = None) -> None`: Build a Docker container.
- `export_image(self, tar_file: Path) -> Awaitable[None]`: Export current images into a tar file.
- `import_image(self, tar_file: Path) -> None`: Import a tar file as image.
- `cleanup(self, old_image: str | None = None, image: str | None = None, version: AwesomeVersion | None = None) -> None`: Check if old version exists and cleanup other versions of image not in use.
- `write_stdin(self, data: bytes) -> None`: Write to add-on stdin.
- `_write_stdin(self, data: bytes) -> None`: Write to add-on stdin.
- `stop(self, remove_container: bool = True) -> None`: Stop/remove Docker container.
- `_validate_trust(self, image_id: str, image: str, version: AwesomeVersion) -> None`: Validate trust of content.
- `_hardware_events(self, device: Device) -> None`: Process Hardware events for adjust device access.

## DockerAudio

The `DockerAudio` class is a Docker Supervisor wrapper for Supervisor Audio. It provides methods to manage Docker containers for audio services.

### Methods

- `image(self) -> str`: Return name of Supervisor Audio image.
- `name(self) -> str`: Return name of Docker container.
- `mounts(self) -> list[Mount]`: Return mounts for container.
- `cgroups_rules(self) -> list[str]`: Return a list of needed cgroups permission.
- `capabilities(self) -> list[Capabilities]`: Generate needed capabilities.
- `ulimits(self) -> list[docker.types.Ulimit]`: Generate ulimits for audio.
- `cpu_rt_runtime(self) -> int | None`: Limit CPU real-time runtime in microseconds.
- `run(self) -> None`: Run Docker image.

## DockerCli

The `DockerCli` class is a Docker Supervisor wrapper for the Home Assistant CLI. It provides methods to manage Docker containers for the CLI.

### Methods

- `image(self)`: Return name of HA cli image.
- `name(self) -> str`: Return name of Docker container.
- `run(self) -> None`: Run Docker image.

## DockerDNS

The `DockerDNS` class is a Docker Supervisor wrapper for Supervisor DNS. It provides methods to manage Docker containers for DNS services.

### Methods

- `image(self) -> str`: Return name of Supervisor DNS image.
- `name(self) -> str`: Return name of Docker container.
- `run(self) -> None`: Run Docker image.

## DockerHomeAssistant

The `DockerHomeAssistant` class is a Docker Supervisor wrapper for Home Assistant. It provides methods to manage Docker containers for Home Assistant, including running, updating, and stopping containers.

### Methods

- `machine(self) -> str | None`: Return machine of Home Assistant Docker image.
- `image(self) -> str`: Return name of Docker image.
- `name(self) -> str`: Return name of Docker container.
- `timeout(self) -> int`: Return timeout for Docker actions.
- `ip_address(self) -> IPv4Address`: Return IP address of this container.
- `cgroups_rules(self) -> list[str]`: Return a list of needed cgroups permission.
- `mounts(self) -> list[Mount]`: Return mounts for container.
- `run(self) -> None`: Run Docker image.
- `execute_command(self, command: str) -> CommandReturn`: Create a temporary container and run command.
- `is_initialize(self) -> Awaitable[bool]`: Return True if Docker container exists.
- `_validate_trust(self, image_id: str, image: str, version: AwesomeVersion) -> None`: Validate trust of content.

## DockerInterface

The `DockerInterface` class is an interface for Docker Supervisor objects. It provides common methods for managing Docker containers, such as running, updating, and stopping containers.

## DockerAPI

The `DockerAPI` class is a manager for Supervisor Docker. It provides methods to interact with the Docker API, including running containers, pulling images, and managing networks.

## DockerMonitor

The `DockerMonitor` class is a monitor for Supervisor Docker. It provides methods to monitor Docker events and handle container state changes.

## DockerMulticast

The `DockerMulticast` class is a Docker Supervisor wrapper for Home Assistant multicast. It provides methods to manage Docker containers for multicast services.

### Methods

- `image(self) -> str`: Return name of Supervisor Multicast image.
- `name(self) -> str`: Return name of Docker container.
- `run(self) -> None`: Run Docker image.

## DockerNetwork

The `DockerNetwork` class is an internal network manager for Supervisor. It provides methods to manage Docker networks, including attaching and detaching containers.

## DockerObserver

The `DockerObserver` class is a Docker Supervisor wrapper for the observer plugin. It provides methods to manage Docker containers for the observer plugin.

### Methods

- `image(self) -> str`: Return name of Supervisor Observer image.
- `name(self) -> str`: Return name of Docker container.
- `run(self) -> None`: Run Docker image.

## DockerStats

The `DockerStats` class calculates and represents Docker stats data. It provides methods to retrieve and process container statistics.

## DockerSupervisor

The `DockerSupervisor` class is a Docker Supervisor wrapper for the Supervisor itself. It provides methods to manage the Docker container for the Supervisor, including attaching, retagging, and updating the container.

### Methods

- `image(self) -> str`: Return name of Supervisor image.
- `name(self) -> str`: Return name of Docker container.
- `attach(self, version: AwesomeVersion) -> None`: Attach to the Supervisor container.
- `retag(self) -> None`: Retag the Supervisor container.
- `update(self, version: AwesomeVersion, image: str | None = None) -> None`: Update the Supervisor container.
