# Aceest Fitness

An automated health and fitness tracking application. This project uses continuous integration to build and package the application into a highly optimized Docker container.

## 🚀 Running the Application

Because this application relies on a Graphical User Interface (GUI), the Docker container requires access to your host machine's X11 display server to render visual windows. 

### Prerequisites

If you are running the image on a Linux host (like Rocky Linux), ensure you allow local container connections to your X11 display by executing this on your host terminal first:
```bash
xhost +local:docker
```

### Launch the Container

Run the following command to execute the Docker image prepared by the Jenkins build:

```bash
sudo docker run --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
  aceest-fitness
```

#### What these flags mean:
* `--rm` • Automatically removes the container file system when it exits to keep your storage clean.
* `-e DISPLAY=$DISPLAY` • Passes your host's current graphic display environmental variable into the container.
* `-v /tmp/.X11-unix:/tmp/.X11-unix:ro` • Mounts the X11 communication socket directory from your host as Read-Only (`ro`), allowing the application inside to draw windows directly on your screen.

---

## 🛠️ Development & CI/CD Pipelines

This repository is equipped to support multiple automation workflows:

### GitHub Actions (Alternative)
The workspace includes a `.github/workflows/ci.yml` pipeline file. On every code push or pull request to the `main` branch, the pipeline will:
1. Initialize an isolated virtual environment.
2. Install Python dependencies and run `pytest`.
3. Package and verify the multi-stage Docker image layer configurations.
