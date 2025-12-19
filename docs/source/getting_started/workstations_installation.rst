Workstations Installation
=========================

Setup for Ubuntu 22.04
---------------------

This project uses Docker for easy deployment and consistent environment setup.
The configuration has been tested on Ubuntu 22.04 host machines with NVIDIA GPU support.

Prerequisites
-------------

- Docker and Docker Compose installed
- NVIDIA GPU with compatible drivers (for GPU acceleration)
- Linux host machine (recommended)
- X11 server access for GUI applications

Installation Steps
------------------

1. **Clone the repository**

   .. code-block:: bash

      git clone git@github.com:GorArzanyanAUA/pid_rl.git
      cd pid_rl

2. **Configure X11 access for GUI applications**

   .. code-block:: bash

      xhost +local:docker

3. **Build the Docker container**

   .. code-block:: bash

      DOCKER_BUILDKIT=1 docker-compose build

4. **Start the container in detached mode**

   .. code-block:: bash

      docker-compose up -d

5. **Enter the container**

   .. code-block:: bash

      docker exec -it pid_rl_container bash


Setup for Windows (WSLG)
-----------------------

This section describes how to set up the project on Windows using WSLG
(Windows Subsystem for Linux GUI) for GUI applications.

Prerequisites
-------------

- Windows 11 with WSL2 and WSLG enabled
- Docker Desktop for Windows installed

Installation Steps
------------------

1. **Clone the repository inside your WSL environment**

   .. code-block:: bash

      git clone git@github.com:GorArzanyanAUA/pid_rl.git
      cd pid_rl

2. **Build the Docker container using the WSLG-specific compose file**

   .. code-block:: bash

      DOCKER_BUILDKIT=1 docker compose -f docker-compose-wslg.yml build

3. **Start the container in detached mode**

   .. code-block:: bash

      docker compose -f docker-compose-wslg.yml up -d

4. **Enter the container**

   .. code-block:: bash

      docker exec -it pid_rl_container bash

.. warning::

   Running the platform on Windows using WSLG is supported, but preliminary
   tests show **significant performance degradation** compared to native Linux.
   Native Ubuntu is strongly recommended for training.


Development Notes
-----------------

Currently, some files are copied into the container at startup.  
These will be moved into the Dockerfile in future revisions.

After creating the container, you may need to rebuild ArduCopter
to ensure modified files take effect:

.. code-block:: bash

   ./waf clean
   ./waf configure --board sitl
   ./waf copter

You may also need to correct the protobuf version:

.. code-block:: bash

   pip uninstall mavsdk
   python3 -m pip uninstall -y protobuf
   sudo apt-get update
   sudo apt-get install -y python3-protobuf

New C++ code was added under ``clock_node`` and must be built manually:

.. code-block:: bash

   cd clock_node
   mkdir -p build && cd build
   cmake -DCMAKE_BUILD_TYPE=Release ..
   make -j

For now, the ``GZ_PARTITION`` environment variable must be set manually
in the terminal where the node is executed.


Troubleshooting
---------------

- **Different host OS**  
  The Dockerfile should work on most systems, but ``docker-compose.yml``
  may require adjustments for non-Linux hosts.

- **GPU compatibility**  
  If CUDA version mismatches occur, update the CUDA version in the Dockerfile
  to match your installed NVIDIA drivers.
