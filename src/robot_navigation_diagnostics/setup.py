from setuptools import find_packages, setup

package_name = 'robot_navigation_diagnostics'

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
        'console_scripts': ["position_tracker_exe = robot_navigation_diagnostics.position_tracker:main",
                            "navigation_safety_checker_exe = robot_navigation_diagnostics.nav_safety_checker:main",
        ],
    },
)
