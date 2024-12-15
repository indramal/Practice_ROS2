from setuptools import find_packages, setup

package_name = 'py_package_practical_1'

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
    maintainer='ihackerubuntu',
    maintainer_email='wmindramalw@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_py = py_package_practical_1.node_py:main',
            'topic_py = py_package_practical_1.topic_py:main',
            'service_client_py = py_package_practical_1.service_client_py:main',
            'service_server_py = py_package_practical_1.service_server_py:main',
            'parameters_py = py_package_practical_1.parameters_py:main',
            'lifecycle_py = py_package_practical_1.lifecycle_py:main',
            'lifecycle_node_manager_py = py_package_practical_1.lifecycle_node_manager_py:main',
        ],
    },
)
