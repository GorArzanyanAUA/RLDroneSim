Architecture
============

RLDroneSim is designed as a modular platform that enables reinforcement learning agents
to operate **on top of an existing UAV flight stack**, rather than replacing it.
The architecture integrates realistic simulation, full autopilot firmware,
and a Python-based RL environment into a single training and evaluation pipeline.

Overview
--------

The platform consists of three main components:

- **Gazebo Simulation**
- **ArduPilot Software-in-the-Loop (SITL)**
- **Python RL Environment**

These components are synchronized to form a closed-loop control system suitable
for reinforcement learning experiments.

.. figure:: _static/ArdupilotEnv.png
   :align: center
   :alt: RLDroneSim architecture overview

   High-level architecture of the RLDroneSim platform.

Core Components
---------------

Gazebo Simulation
^^^^^^^^^^^^^^^^^

Gazebo provides the 3D simulation environment and physics engine.
It models UAV dynamics, sensor feedback, and environmental effects
(e.g., gravity, wind, collisions).

Gazebo is responsible for:
- Vehicle dynamics and physics integration
- Sensor simulation
- World and environment configuration

ArduPilot SITL
^^^^^^^^^^^^^^

ArduPilot SITL runs the **same flight-control firmware used on real UAVs**.
It provides validated control loops, state estimation, navigation logic,
and safety mechanisms.

SITL is coupled with Gazebo to overcome the simplified internal physics
of the firmware and ensure realistic closed-loop behavior.

Python RL Environment
^^^^^^^^^^^^^^^^^^^^^

The Python environment wraps the simulation and exposes a
**Gymnasium-compatible interface** to the RL agent.

Communication with ArduPilot SITL is implemented using **pymavlink**.
Through this interface, the environment gains access to:
- UAV state and telemetry
- Internal control-loop parameters (e.g., PID coefficients)
- Real-time parameter updates during flight

By using pymavlink, the RL agent can interact with the autopilot
without bypassing or modifying core firmware logic.

Control and Data Flow
---------------------

At each environment time step:

1. The environment queries the UAV state from ArduPilot SITL
   (e.g., altitude, velocity, controller errors).
2. The RL agent observes the current state.
3. The agent outputs actions corresponding to **incremental updates
   of control-loop coefficients**.
4. Updated parameters are sent to ArduPilot via MAVLink.
5. ArduPilot applies the new parameters within its existing control loops.
6. Gazebo advances the simulation and returns updated sensor feedback.

This design allows RL to **adapt and tune control behavior online**
while preserving firmware-level realism and safety.

Environment Reset Mechanism
---------------------------

A critical requirement for reinforcement learning is the ability to
**fully reset the environment** between episodes. Neither Gazebo nor
ArduPilot SITL natively support complete resets of internal controller state.

To address this, RLDroneSim introduces **custom Lua scripts inside ArduPilot SITL**
that explicitly reset:
- Internal control loops
- EKF and state-estimation filters
- Controller integrators and cached state

These scripts, combined with Gazebo world and model resets, ensure that each
episode starts from a **clean and reproducible initial state**. This mechanism
is essential for implementing the ``reset()`` function of the RL environment
and for stable, unbiased training.

Deployment Architecture
-----------------------

After training, the learned policy can be deployed on real UAV hardware.
Deployment follows a companion-computer-based architecture.

A lightweight onboard computer (e.g., **Raspberry Pi**) runs the trained RL agent
in inference mode. The companion computer communicates with the flight controller
via a **serial MAVLink connection**, allowing it to:

- Read UAV state and telemetry
- Modify control-loop parameters in real time

In this setup:
- ArduPilot continues to execute all safety-critical control logic
- The RL agent operates as an adaptive, high-level module
- No modification of core flight firmware is required

This deployment strategy enables rapid experimentation and real-world testing
while maintaining compatibility with existing UAV hardware.

Design Philosophy
-----------------

RLDroneSim follows an *augment, not replace* approach:

- Low-level control loops remain inside ArduPilot
- RL operates at a supervisory or adaptive level
- Integration with real hardware is simplified
- Sim-to-real transfer is improved compared to controller-replacement methods

The modular architecture makes the platform extensible to other UAV tasks,
control objectives, and RL algorithms without restructuring the simulation core.
