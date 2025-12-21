RLDroneSim Documentation
========================

Welcome to the RLDroneSim documentation.
RLDroneSim is a realistic and extensible reinforcement learning (RL) platform designed 
for developing agents that integrate seamlessly with widely used open-source Ardupilot UAV software stack.
Built on Ardupilot SITL and Gazebo, the platform enables RL agents to operate on top of the existing Ardupilot firmware.
This design allows augmentation of current UAV functionality—improving adaptability, robustness, 
and autonomy with minimal integration effort.
RLDroneSim offers a Gym-compatible environment, enabling rapid development and evaluation of RL methods 
within a realistic simulation that reflects real-world UAV dynamics.

This site covers how to get the environment running, the internal architecture, demos, tutorials, and
directions for further research.

Project repository: https://anonymous.4open.science/r/RLDroneSim-C815/README.md

.. toctree::
   :maxdepth: 2
   :caption: Contents

   getting_started/index
   architecture
   tutorials/index
   further_research

Getting started
---------------

First time here? Start with :doc:`the getting started guide <getting_started/index>`
to set up your workstation, run the basic scripts, and see common issues.

Architecture
------------

Read :doc:`Architecture <architecture>` for an overview of the main
components of RLDroneSim, how they interact, and where to plug in your own code.


Tutorials
---------

See :doc:`Tutorials <tutorials>` for step-by-step guides that walk through
specific tasks, training workflows, and integrations.

Further research
----------------

The :doc:`Further research <further_research>` section collects ideas,
extensions, and references for pushing RLDroneSim beyond the base use cases.
