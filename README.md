# Practice_ROS2


Commands:

ros2 pkg list - Get list of all installed packages

ros2 pkg create cpp_package_practical_1 --build-type ament_cmake --license Apache-2.0 --dependencies rclcpp --node-name test1_cpp - Create CPP Package

ros2 pkg create py_package_practical_1 --build-type ament_python --license Apache-2.0 --dependencies rclpy --node-name test1_py - Create Python Package

ros2 run cpp_package_practical_1 test1_cpp

ros2 run py_package_practical_1 test1_py 

rm -rf build/ install/ log/

colcon build

source install/setup.zsh 
source install/local_setup.zsh

colcon build && source install/local_setup.zsh

echo $SHELL    

gnome-text-editor ~/.zshrc


Create Workspace --> create src --> create package --> create node

c_cpp_properties.json

{
  "configurations": [
    {
      "browse": {
        "databaseFilename": "${default}",
        "limitSymbolsToIncludedHeaders": false
      },
      "includePath": [
        "/opt/ros/jazzy/include/**",
        "/usr/include/**"
      ],
      "name": "ROS",
      "intelliSenseMode": "gcc-x64",
      "compilerPath": "/usr/bin/gcc",
      "cStandard": "gnu11",
      "cppStandard": "c++14"
    }
  ],
  "version": 4
}

settings.json

{
    "ros.distro": "jazzy",
    "python.autoComplete.extraPaths": [
        "/opt/ros/jazzy/lib/python3.12/site-packages"
    ],
    "python.analysis.extraPaths": [
        "/opt/ros/jazzy/lib/python3.12/site-packages"
    ]
}