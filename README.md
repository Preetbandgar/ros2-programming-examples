# ROS2 Development Workspace

![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy-22314E)
![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Linux-E95420)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

Active ROS 2 engineering workspace for building modular robotics software examples with Python (`rclpy`).

The workspace demonstrates ROS 2 package organization, publishers, subscribers, services, actions, custom interfaces, parameters, and logging. It is intentionally evolving with my ROS 2 learning path.

## Current Progress

### Completed

- ✔ Publishers & Subscribers
- ✔ Services & Clients
- ✔ Actions
- ✔ Custom Interfaces
- ✔ Modular Package Architecture
- ✔ Gazebo Fundamentals
- ✔ RViz2 Visualization
- ✔ Foxglove Debugging
- ✔ Nav2 Fundamentals

### Currently Learning

- Standard ROS 2 interfaces: `std_srvs`, `builtin_interfaces`, `visualization_msgs`
- TF2
- Launch files and parameter configuration
- QoS profiles

### Upcoming

- Executors & Callback Groups
- Lifecycle Nodes
- ROS 2 package management: `ament_python`, `ament_cmake`, `package.xml`, `rosdep`
- `robot_localization` with EKF
- Behavior Trees
- Pluginlib fundamentals
- ROS 2 testing with `pytest` and `launch_testing`
- Mixed `rclpy` / `rclcpp` development

## Project Overview

This repository is a continuously maintained ROS 2 development workspace focused on practical, modular examples rather than a single finished robot application. It shows package structure, node implementation, custom interfaces, command-line validation, and clean workspace organization.

## Objectives

- Build and maintain a modular ROS 2 workspace with focused packages.
- Practice core ROS 2 communication patterns using Python nodes.
- Keep the repository accurate, professional, and easy to extend as new concepts are added.

## Development Status

This repository is actively maintained and continuously expanded as I progress through my ROS 2 learning journey. Implemented work is kept separate from planned topics so the repository reflects its current state honestly.

## Repository Architecture

```text
ros2-programming-examples/
├── README.md
└── src/
    ├── my_robot_interfaces/
    ├── robot_core/
    ├── robot_sensors/
    ├── robot_state/
    ├── robot_safety/
    ├── robot_navigation/
    ├── robot_bringup_sensors/
    └── robot_navigation_diagnostics/
```

Most packages are `ament_python`; `my_robot_interfaces` is `ament_cmake` because it defines custom interfaces.

## Package Overview

| Package | Description |
| --- | --- |
| `my_robot_interfaces` | Custom messages, services, and actions for robot state, safety, mode control, and navigation. |
| `robot_core` | Basic node examples and robot chatter publisher/subscriber pair. |
| `robot_sensors` | Battery, motor temperature, fake LiDAR, LiDAR watchdog, and IMU monitoring examples. |
| `robot_state` | Robot state publisher/subscriber, robot mode service/client, and pose tracking. |
| `robot_safety` | Safety service/client, thermal guard, and emergency velocity command publisher. |
| `robot_navigation` | Area navigation action server using the custom `MapsArea` action. |
| `robot_bringup_sensors` | IMU tilt monitoring and alert publishing example. |
| `robot_navigation_diagnostics` | Position tracking and path/map safety checking examples. |

## Implemented ROS 2 Concepts and Features

- Multi-package ROS 2 workspace structure
- Python node development with `rclpy`
- Publishers, subscribers, services, clients, and an action server
- Custom `msg`, `srv`, and `action` interfaces
- Timers, callbacks, parameters, and ROS 2 logging
- CLI-based build and execution workflow with `colcon` and `ros2 run`

## Installation

- Ubuntu with ROS 2 (Jazzy) installed
- Python 3
- `colcon` build tools
- Standard ROS 2 message packages used by the examples

Clone and source ROS 2:

```bash
git clone https://github.com/Preetbandgar/ros2-programming-examples.git
cd ros2-programming-examples
source /opt/ros/jazzy/setup.bash
```

Install dependencies:

```bash
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build

```bash
colcon build
source install/setup.bash
```

## Run

```bash
ros2 pkg executables robot_core
ros2 pkg executables robot_sensors
ros2 pkg executables robot_state
ros2 pkg executables robot_safety
ros2 pkg executables robot_navigation
```

Example commands:

```bash
ros2 run robot_core robot_speaker_exe
ros2 run robot_core robot_listener_exe

ros2 run robot_state robot_mode_server_exe
ros2 run robot_state robot_mode_client_exe

ros2 run robot_sensors lidar_fake_node_exe
ros2 run robot_sensors lidar_watchdog_node_exe

ros2 run robot_navigation area_navigation_action_server_exe
```

After changing packages or interfaces, rebuild and source again:

```bash
colcon build
source install/setup.bash
```

## Tools and Technologies

- ROS 2 Jazzy
- Python 3
- `rclpy`
- `ament_python`
- `ament_cmake`
- `rosidl_default_generators`
- `colcon`
- ROS 2 CLI tools
- RViz2, Gazebo, and Foxglove for ongoing validation work

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
