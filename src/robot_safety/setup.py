from setuptools import find_packages, setup

package_name = 'robot_safety'

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
    description='Robot safety services, guards, and emergency command nodes.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "robot_safety_server_exe = robot_safety.safety_server:main",
            "robot_safety_client_exe = robot_safety.safety_client_node:main",
            "thermal_guard_sub_exe = robot_safety.thermal_safety_guard:main",
            "emergency_brake_vel_pub_exe = robot_safety.emergency_brake:main",
        ],
    },
)
