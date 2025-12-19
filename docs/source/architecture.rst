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

.. figure:: /_static/architecture_placeholder.png
   :align: center
   :alt: RLDroneSim architecture overview

   *Figure: High-level architecture of the RLDroneSim platform (placeholder).*

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

Design Philosophy
-----------------

RLDroneSim follows an *augment, not replace* approach:

- Low-level control loops remain inside ArduPilot
- RL operates at a supervisory or adaptive level
- Integration with real hardware is simplified
- Sim-to-real transfer is improved compared to controller-replacement methods

The modular architecture makes the platform extensible to other UAV tasks,
control objectives, and RL algorithms without restructuring the simulation core.
