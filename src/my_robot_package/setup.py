from setuptools import find_packages, setup

package_name = 'my_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pritam',
    maintainer_email='157994717+Preetbandgar@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "hello_robot_exe = my_robot_package.my_first_node:main",
            "robot_speaker_exe = my_robot_package.robot_speaker:main",
            "robot_listener_exe = my_robot_package.robot_listener:main",
            "robot_battery_level_exe = my_robot_package.battery_sim:main",
            "battery_listener_exe = my_robot_package.battery_listener:main",
            "motor_temp_pub_exe = my_robot_package.motor_temp_publisher:main",
            "thermal_guard_sub_exe = my_robot_package.thermal_safety_guard:main",
            "robot_state_pub_exe = my_robot_package.robot_state_publisher:main",
            "robot_state_sub_exe = my_robot_package.robot_state_subscriber:main",
            "robot_mode_server_exe = my_robot_package.robot_mode_server:main",
            "robot_mode_client_exe = my_robot_package.robot_mode_client:main",
            "robot_safety_server_exe = my_robot_package.safety_server:main",
            "robot_safety_client_exe = my_robot_package.safety_client_node:main",
            "area_navigation_action_server_exe = my_robot_package.area_navigation_server:main",
            "emergency_brake_vel_pub_exe = my_robot_package.emergency_brake:main",
            "pose_tracking_sub_exe = my_robot_package.pose_subscriber:main"
        ],
    },
)
