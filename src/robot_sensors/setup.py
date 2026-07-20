from setuptools import find_packages, setup

package_name = 'robot_sensors'

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
    description='Sensor simulation and monitoring nodes.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "robot_battery_level_exe = robot_sensors.battery_sim:main",
            "battery_listener_exe = robot_sensors.battery_listener:main",
            "motor_temp_pub_exe = robot_sensors.motor_temp_publisher:main",
            "lidar_fake_node_exe = robot_sensors.lidar_pub_node:main",
            "lidar_watchdog_node_exe = robot_sensors.lidar_sub_watchdog:main",
            "robot_imu_monitor_exe = robot_sensors.imu_monitor:main",
        ],
    },
)
