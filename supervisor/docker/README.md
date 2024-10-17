# Supervisor Docker Package Documentation

This document provides a comprehensive overview of the `supervisor/docker` package, explaining its overall structure and functionality. The package contains multiple modules, each with its own classes and methods. This documentation includes sections for each module and provides examples of how to use the classes and methods in each module.

## Table of Contents

- [Modules](#modules)
  - [addon.py](#addonpy)
  - [audio.py](#audiopy)
  - [cli.py](#clipy)
  - [const.py](#constpy)
  - [dns.py](#dnspy)
  - [homeassistant.py](#homeassistantpy)
  - [interface.py](#interfacepy)
  - [manager.py](#managerpy)
  - [monitor.py](#monitorpy)
  - [multicast.py](#multicastpy)
  - [network.py](#networkpy)
  - [observer.py](#observerpy)
  - [stats.py](#statspy)
  - [supervisor.py](#supervisorpy)

## Modules

### addon.py

The `addon.py` module contains the `DockerAddon` class, which is a Docker Supervisor wrapper for Home Assistant add-ons. This class provides methods to manage Docker containers for add-ons, including running, updating, and stopping containers.

#### Example Usage

```python
from supervisor.docker.addon import DockerAddon

# Initialize DockerAddon
docker_addon = DockerAddon(coresys, addon)

# Run the add-on container
await docker_addon.run()

# Update the add-on container
await docker_addon.update(version, image)

# Stop the add-on container
await docker_addon.stop()
```

### audio.py

The `audio.py` module contains the `DockerAudio` class, which is a Docker Supervisor wrapper for Supervisor Audio. This class provides methods to manage Docker containers for audio services.

#### Example Usage

```python
from supervisor.docker.audio import DockerAudio

# Initialize DockerAudio
docker_audio = DockerAudio(coresys)

# Run the audio container
await docker_audio.run()
```

### cli.py

The `cli.py` module contains the `DockerCli` class, which is a Docker Supervisor wrapper for the Home Assistant CLI. This class provides methods to manage Docker containers for the CLI.

#### Example Usage

```python
from supervisor.docker.cli import DockerCli

# Initialize DockerCli
docker_cli = DockerCli(coresys)

# Run the CLI container
await docker_cli.run()
```

### const.py

The `const.py` module contains various constants used throughout the `supervisor/docker` package. These constants include environment variables, mount types, and container states.

### dns.py

The `dns.py` module contains the `DockerDNS` class, which is a Docker Supervisor wrapper for Supervisor DNS. This class provides methods to manage Docker containers for DNS services.

#### Example Usage

```python
from supervisor.docker.dns import DockerDNS

# Initialize DockerDNS
docker_dns = DockerDNS(coresys)

# Run the DNS container
await docker_dns.run()
```

### homeassistant.py

The `homeassistant.py` module contains the `DockerHomeAssistant` class, which is a Docker Supervisor wrapper for Home Assistant. This class provides methods to manage Docker containers for Home Assistant, including running, updating, and stopping containers.

#### Example Usage

```python
from supervisor.docker.homeassistant import DockerHomeAssistant

# Initialize DockerHomeAssistant
docker_homeassistant = DockerHomeAssistant(coresys)

# Run the Home Assistant container
await docker_homeassistant.run()

# Update the Home Assistant container
await docker_homeassistant.update(version, image)

# Stop the Home Assistant container
await docker_homeassistant.stop()
```

### interface.py

The `interface.py` module contains the `DockerInterface` class, which is an interface for Docker Supervisor objects. This class provides common methods for managing Docker containers, such as running, updating, and stopping containers.

### manager.py

The `manager.py` module contains the `DockerAPI` class, which is a manager for Supervisor Docker. This class provides methods to interact with the Docker API, including running containers, pulling images, and managing networks.

### monitor.py

The `monitor.py` module contains the `DockerMonitor` class, which is a monitor for Supervisor Docker. This class provides methods to monitor Docker events and handle container state changes.

### multicast.py

The `multicast.py` module contains the `DockerMulticast` class, which is a Docker Supervisor wrapper for Home Assistant multicast. This class provides methods to manage Docker containers for multicast services.

#### Example Usage

```python
from supervisor.docker.multicast import DockerMulticast

# Initialize DockerMulticast
docker_multicast = DockerMulticast(coresys)

# Run the multicast container
await docker_multicast.run()
```

### network.py

The `network.py` module contains the `DockerNetwork` class, which is an internal network manager for Supervisor. This class provides methods to manage Docker networks, including attaching and detaching containers.

### observer.py

The `observer.py` module contains the `DockerObserver` class, which is a Docker Supervisor wrapper for the observer plugin. This class provides methods to manage Docker containers for the observer plugin.

#### Example Usage

```python
from supervisor.docker.observer import DockerObserver

# Initialize DockerObserver
docker_observer = DockerObserver(coresys)

# Run the observer container
await docker_observer.run()
```

### stats.py

The `stats.py` module contains the `DockerStats` class, which calculates and represents Docker stats data. This class provides methods to retrieve and process container statistics.

### supervisor.py

The `supervisor.py` module contains the `DockerSupervisor` class, which is a Docker Supervisor wrapper for the Supervisor itself. This class provides methods to manage the Docker container for the Supervisor, including attaching, retagging, and updating the container.

#### Example Usage

```python
from supervisor.docker.supervisor import DockerSupervisor

# Initialize DockerSupervisor
docker_supervisor = DockerSupervisor(coresys)

# Attach to the Supervisor container
await docker_supervisor.attach(version)

# Retag the Supervisor container
await docker_supervisor.retag()

# Update the Supervisor container
await docker_supervisor.update(version, image)
```
