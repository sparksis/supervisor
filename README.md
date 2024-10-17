# Home Assistant Supervisor

## First private cloud solution for home automation

Home Assistant (former Hass.io) is a container-based system for managing your
Home Assistant Core installation and related applications. The system is
controlled via Home Assistant which communicates with the Supervisor. The
Supervisor provides an API to manage the installation. This includes changing
network settings or installing and updating software.

## Installation

Installation instructions can be found at https://home-assistant.io/getting-started.

## Development

For small changes and bugfixes you can just follow this, but for significant changes open a RFC first.
Development instructions can be found [here][development].

## Release

Releases are done in 3 stages (channels) with this structure:

1. Pull requests are merged to the `main` branch.
2. A new build is pushed to the `dev` stage.
3. Releases are published.
4. A new build is pushed to the `beta` stage.
5. The [`stable.json`][stable] file is updated.
6. The build that was pushed to `beta` will now be pushed to `stable`.

## Supervisor Docker Package

The `supervisor/docker` package is a comprehensive set of modules for managing Docker containers within the Home Assistant Supervisor. It includes various modules such as `docker.py`, `audio.py`, `cli.py`, `const.py`, `dns.py`, `homeassistant.py`, `interface.py`, `manager.py`, `monitor.py`, `multicast.py`, `network.py`, `observer.py`, `stats.py`, and `supervisor.py`. Each module has classes and methods that provide detailed functionality for managing Docker containers.

For more information, please refer to the [Supervisor Docker Package Documentation](supervisor/docker/README.md).

[development]: https://developers.home-assistant.io/docs/supervisor/development
[stable]: https://github.com/home-assistant/version/blob/master/stable.json

[![Home Assistant - A project from the Open Home Foundation](https://www.openhomefoundation.org/badges/home-assistant.png)](https://www.openhomefoundation.org/)
