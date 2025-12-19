Running Scripts
===============

RLDroneSim provides example scripts for training and evaluating reinforcement learning agents.
All example scripts are located in the ``rl_pid/examples`` directory.

Training
--------

To start training, run:

.. code-block:: bash

   python rl_pid/examples/train_vectorized.py

The default training configuration is defined in:

.. code-block:: text

   rl_pid/rl_training/configs/default_config.yaml

This configuration file allows you to:
- Adjust environment-specific parameters
- Select and configure the RL algorithm
- Tune learning hyperparameters
- Change the simulation world and physics parameters
- Enable or disable the GUI (disabling the GUI significantly improves training speed)

Simulation Time Server
----------------------

Before running the training script, a simulation time server must be started in a separate terminal:

.. code-block:: bash

   /clock_node/build/sim_time_server

This node provides synchronized simulation time required for correct interaction between
Gazebo and ArduPilot SITL.

Logging and Monitoring
----------------------

TensorBoard log files are saved automatically during training.

Logs are stored in:

.. code-block:: text

   rl_pid/rl_training/runs/{mission}/{algo}

To monitor training progress or inspect results after training, run:

.. code-block:: bash

   tensorboard --logdir rl_pid/rl_training/runs

Evaluation
----------

To evaluate a trained model, use:

.. code-block:: bash

   python rl_pid/examples/eval_model.py

Specify the directory containing the trained model (typically one of the folders inside
``rl_pid/rl_training/runs``). The script loads the latest trained policy and runs it in the
simulation environment.
