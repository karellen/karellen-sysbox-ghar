# Karellen Sysbox GitHub Actions Runner

**NOTE: This project is NOT associated with, endorsed or supported by GitHub, Docker or Nestybox**

**All trademarks are property of their respective owners**

This is a packaged ephemeral GitHub Actions Runner designed to run on Sysbox Docker runtime to allow
for safe(er), fast and efficient self-hosted GitHub Actions Runners usable with public repositories.
The containerized GitHub Actions Runner is further fully DinD- and `sudo`-capable while having no privileges on the 
underlying host.

The orchestration is as follows:
* `systemd` service on the host obtains organization runner registration token
* the token is provided to the container via a mounted volume
* after runner configuration is completed (successfully or otherwise) the token is securely delete from the 
  shared volume
* if configuration is completed the runner is started
* after the runner completes finishes execution the container is terminated
* the `systemd` service automatically restarts creating a new 

Under the above scheme any adversarial code that may be loaded by the runner inside the container has no exposure to
any tokens or other cryptographic primitives that may have been to register the runner in the first place.
