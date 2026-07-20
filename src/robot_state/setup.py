from setuptools import find_packages, setup

package_name = 'robot_state'

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
    description='Robot state, mode, and pose tracking nodes.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "robot_state_pub_exe = robot_state.robot_state_publisher:main",
            "robot_state_sub_exe = robot_state.robot_state_subscriber:main",
            "robot_mode_server_exe = robot_state.robot_mode_server:main",
            "robot_mode_client_exe = robot_state.robot_mode_client:main",
            "pose_tracking_sub_exe = robot_state.pose_subscriber:main",
        ],
    },
)
