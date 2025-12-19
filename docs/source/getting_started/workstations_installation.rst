Workstations installation
=========================

## Setup for Ubuntu 22.04

This project uses Docker for easy deployment and consistent environment setup. The configuration has been tested on Ubuntu 22.04 host machines with NVIDIA GPU support.

### Prerequisites

- Docker and Docker Compose installed
- NVIDIA GPU with compatible drivers (for GPU acceleration)
- Linux host machine (recommended)
- X11 server access for GUI applications

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone git@github.com:GorArzanyanAUA/pid_rl.git
   cd pid_rl
   ```

2. **Configure X11 access for GUI applications**
   ```bash
   xhost +local:docker
   ```

3. **Build the Docker container**
   ```bash
   DOCKER_BUILDKIT=1 docker-compose build
   ```

4. **Start the container in detached mode**
   ```bash
   docker-compose up -d
   ```

5. **Enter the container**
   ```bash
   docker exec -it pid_rl_container bash
   ```

## Setup for Windows with WSLG

This section describes how to set up the project on Windows using WSLG (Windows Subsystem for Linux GUI) for GUI applications.

### Prerequisites

- Windows 11 with WSL2 and WSLG enabled
- Docker Desktop for Windows installed
- WSL2 distribution (Ubuntu 22.04 recommended)
- WSLG support enabled

### Installation Steps

1. **Clone the repository inside your WSL environment**
   ```bash
   git clone git@github.com:GorArzanyanAUA/pid_rl.git
   cd pid_rl
   ```

2. **Build the Docker container using the WSLG-specific compose file**
   ```bash
   DOCKER_BUILDKIT=1 docker compose -f docker-compose-wslg.yml build
   ```

3. **Start the container in detached mode**
   ```bash
   docker compose -f docker-compose-wslg.yml up -d
   ```

4. **Enter the container**
   ```bash
   docker exec -it pid_rl_container bash
   ```


### DEVELOPMENT NOTES!!!
For now some of the files are being copied into the container at start time. Letter those will be set in the Dockerfile.
Meanwhile, after creating the container you may need to rebuild the ArduCopter make the changed files take effect.
   ```bash
   ./waf clean
   ./waf configure --board sitl
   ./waf copter
   ```

Also, you may need to correct the version of the protobuf.
   ```bash
   pip uninstall mavsdk
   python3 -m pip uninstall -y protobuf
   sudo apt-get update
   sudo apt-get install -y python3-protobuf
   ```

Also, new cpp code was added under clock_node, you may need to build it. 
   ```bash
   cd clock_node
   mkdir -p build && cd build
   cmake -DCMAKE_BUILD_TYPE=Release ..
   make -j
   ```
For now you need to set the GZ_PARTITION env variable in the terminal where you run the node.

### Troubleshooting

- **Different host OS**: The Dockerfile should work on any machine, but you may need to modify `docker-compose.yml` for non-Linux systems
- **GPU compatibility**: If you encounter CUDA version issues, update the CUDA version in the Dockerfile to match your GPU
- ****: If you encounter CUDA version issues, update the CUDA version in the Dockerfile to match your GPU
