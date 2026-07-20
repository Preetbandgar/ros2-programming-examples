# --- STAGE 1: BUILD ENVIRONMENT ---
FROM ros:jazzy-ros-base AS builder
ENV DEBIAN_FRONTEND=noninteractive

# Install system build dependencies
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    ros-jazzy-rosidl-default-generators \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

# Copy your exact src directory layout
COPY ./src ./src

# Initialize rosdep, update database, and install required system/ROS dependencies
RUN rosdep update && \
    apt-get update && \
    rosdep install --from-paths src --ignore-src -y -r && \
    rm -rf /var/lib/apt/lists/*

# Build your custom messages package first, then build your python nodes
RUN . /opt/ros/jazzy/setup.sh && \
    colcon build --merge-install --cmake-args -DCMAKE_BUILD_TYPE=Release

# --- STAGE 2: PRODUCTION RUNTIME ---
FROM ros:jazzy-ros-base AS runner
ENV DEBIAN_FRONTEND=noninteractive

# Create a secure corporate non-root user
ARG USERNAME=robot_operator
ARG USER_UID=1042
ARG USER_GID=1042

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

USER $USERNAME
WORKDIR /home/$USERNAME/robot_app

# Copy ONLY compiled artifacts from build stage to minimize final runtime size
COPY --from=builder /ros2_ws/install ./install

# Automatically source ROS2 and your custom workspace for the operator
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc && \
    echo "source /home/$USERNAME/robot_app/install/setup.bash" >> ~/.bashrc

# Default fallback command (Overridden by your launch scripts or runtime configurations)
CMD ["bash"]

