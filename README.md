# Practice_ROS2

## Sections

ros2_ws_0 - This is URDF/XACRO with ROS2 Workspace
ros2_ws_1 - This is basic ROS2 Workspace
ros2_ws_2 - This is Gazebo with ROS2 Workspace
ros2_ws_3 - This is SLAM and Nav2 with ROS2 Workspace
ros2_ws_4 - This is MoveIt with ROS2 Workspace
ros2_ws_5 - This is ROS2_Control with ROS2 Workspace
ros2_ws_6 - This is QT with ROS2 Workspace
ros2_ws_7 - This is Blender + Avatar + Fuel with ROS2 Workspace

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