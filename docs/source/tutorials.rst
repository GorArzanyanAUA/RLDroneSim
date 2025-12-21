Tutorials
=========

This tutorial explains how to customize reinforcement learning experiments in
RLDroneSim using the YAML-based configuration system. All aspects of training,
simulation, and reward design are controlled through a single configuration file,
allowing rapid experimentation without modifying source code.

Configuration Overview
----------------------

RLDroneSim experiments are defined through a YAML configuration file, typically:

.. code-block:: text

   rl_pid/rl_training/configs/default_config.yaml

The configuration is divided into logical sections:
- Environment definition
- Training setup
- Algorithm-specific hyperparameters
- Reward formulation
- Simulation and vehicle configuration

Each section is described below.

Environment Configuration
-------------------------

The ``environment_config`` section defines how the RL environment is constructed
and what the agent can observe and control.

.. code-block:: yaml

   environment_config:
     max_episode_steps: 100
     mode: "altitude"
     observable_gains: "PSC_POSZ_P+PSC_VELZ_P+PSC_ACCZ_P+PSC_VELZ_D"
     observable_states: "alt_err+vZ_err+accZ_err"
     action_gains: "PSC_POSZ_P+PSC_VELZ_P+PSC_ACCZ_P+PSC_VELZ_D"
     action_dt: 1.0
     takeoff_altitude: 5.0
     verbose: false

Key concepts:

- **mode** selects the flight-control task (e.g., altitude, position, attitude).
- **observable_gains** define which control-loop parameters are visible to the agent.
- **observable_states** define which UAV states are observed.
- **action_gains** define which control-loop parameters the agent can modify.
- **action_dt** sets the interval between agent actions and observations.

This design allows RL agents to tune controller parameters online without
directly commanding actuators.

Training Configuration
---------------------

The ``training_config`` section controls the overall training process.

.. code-block:: yaml

   training_config:
     total_timesteps: 1000000
     runs_base: "/home/pid_rl/rl_training/runs"
     algo: "td3"
     mission: "hover"
     log_interval: 5
     progress_bar: true
     reset_num_timesteps: false

Important fields:

- **total_timesteps**: total number of environment steps.
- **algo**: reinforcement learning algorithm (e.g., ``td3``, ``ddpg``).
- **mission**: experiment identifier used for logging.
- **runs_base**: base directory for all training outputs.

Algorithm Hyperparameters
-------------------------

RLDroneSim supports multiple algorithms via Stable-Baselines3.
Each algorithm has its own parameter block.

Example: TD3 configuration.

.. code-block:: yaml

   td3_params:
     learning_rate: 0.0015
     buffer_size: 80000
     learning_starts: 10000
     batch_size: 1024
     tau: 0.005
     gamma: 0.99
     train_freq: 1
     gradient_steps: 10
     action_noise:
       type: "NormalActionNoise"
       mean: 0.0
       sigma: 0.05
     policy_kwargs:
       net_arch:
         pi: [512, 512]
         qf: [512, 512]
     device: "cuda"

This section allows:
- Full control over learning dynamics
- Custom actor–critic architectures
- Exploration noise tuning
- CPU/GPU selection

Switching algorithms requires only changing ``algo`` and the corresponding
parameter block.

Callbacks and Logging
---------------------

Callbacks define auxiliary training behavior.

.. code-block:: yaml

   callbacks:
     - type: "checkpoint"
       save_freq: 1000
     - type: "tensorboard"

Checkpointing and TensorBoard logging are enabled by default.
Logs are written automatically to:

.. code-block:: text

   rl_pid/rl_training/runs/{mission}/{algo}

Reward Configuration
--------------------

The reward function is defined in the ``reward_config`` section.
Each flight mode can have its own reward structure.

.. code-block:: yaml

   reward_config:
     altitude:
       alt_w: 3
       xy_w: 2
       velN_w: 1
       velE_w: 1
       velZ_w: 1
       step_reward: 100
       crash_penalty_att: -20
       crash_penalty_vel: -20
       crash_penalty_flip: -20
       crash_penalty_far: -20

Reward design directly affects learning stability and safety.
Careful tuning is required to avoid unsafe or exploitative behavior.

Drone and SITL Configuration
----------------------------

The ``drone_config`` and ``sitl_config`` sections define how the simulator and
autopilot are launched.

.. code-block:: yaml

   sitl_config:
     ardupilot_path: "/home/pid_rl/ardupilot"
     frame: "gazebo-iris"
     speedup: 25
     wipe_eeprom: true
     ideal_sensors: true
     no_mavproxy: true

These parameters control:
- Vehicle model
- Simulation speed
- Sensor realism
- SITL startup behavior

Gazebo Configuration
--------------------

Gazebo-specific parameters are defined separately.

.. code-block:: yaml

   gazebo_config:
     sdf_file: "/home/pid_rl/ardupilot_gazebo/worlds/simple_world.sdf"
     gui: false
     verbose: false

Disabling the GUI significantly improves training performance.
Environmental effects such as wind should be defined directly in the SDF file.

Summary
-------

RLDroneSim uses a centralized configuration system to expose all relevant aspects
of reinforcement learning experiments. By modifying a single YAML file, users can
change control objectives, observation and action spaces, learning algorithms,
reward functions, and simulation parameters without touching the codebase.
