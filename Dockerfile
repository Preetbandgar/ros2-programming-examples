# ROS 2 Jazzy Development Environment
FROM ros:jazzy-ros-base

ENV DEBIAN_FRONTEND=noninteractive

# --------------------------------------------------
# Install development tools
# --------------------------------------------------
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    curl \
    wget \
    vim \
    nano \
    tree \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-argcomplete \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Initialize rosdep
# --------------------------------------------------
RUN rosdep init || true
RUN rosdep update

# --------------------------------------------------
# Configure ubuntu user
# --------------------------------------------------
RUN usermod -aG sudo ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/ubuntu && \
    chmod 0440 /etc/sudoers.d/ubuntu

# Create workspace as root
RUN mkdir -p /home/ubuntu/ros2-programming-examples/src && \
    chown -R ubuntu:ubuntu /home/ubuntu/ros2-programming-examples

# Copy entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Switch to ubuntu user
USER ubuntu

WORKDIR /home/ubuntu/ros2-programming-examples

# Source ROS automatically
RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/ubuntu/.bashrc

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]
