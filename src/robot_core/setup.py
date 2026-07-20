from setuptools import find_packages, setup

package_name = 'robot_core'

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
    description='Core ROS 2 publisher and subscriber examples.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "hello_robot_exe = robot_core.my_first_node:main",
            "robot_speaker_exe = robot_core.robot_speaker:main",
            "robot_listener_exe = robot_core.robot_listener:main",
        ],
    },
)
