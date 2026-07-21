#!/bin/bash
set -e

source /opt/ros/jazzy/setup.bash

if [ -f "/home/ubuntu/ros2-programming-examples/install/setup.bash" ]; then
    source /home/ubuntu/ros2-programming-examples/install/setup.bash
fi

exec "$@"