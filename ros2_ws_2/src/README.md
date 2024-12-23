# This is ROS2 and Gazebo Practice

Check - https://automaticaddison.com/

## 1. robot_description

This is bring robot up in gazebo with URDF and Xacro.

## 2. robot_imu_sensor

Add to xacro file

<gazebo reference="base_link">
        <sensor name="imu_sensor" type="imu">
            <always_on>1</always_on>
            <update_rate>1</update_rate>
            <visualize>true</visualize>
            <topic>imu</topic>
            <plugin filename="gz-sim-imu-system" name="gz::sim::systems::Imu">
            </plugin>
        </sensor>
    </gazebo>

## 3. robot_camera_sensor

Camera box in URDF/XACRO file

<link name="sensor_box_link">
        <visual>
            <geometry>
                <box size="0.05 0.05 0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0" />
            <material name="grey" />
        </visual>
        <collision>
            <geometry>
                <box size="0.05 0.05 0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0" />
        </collision>
        <xacro:box_inertia m="0.2" l="0.5" w="0.5" h="0.5" xyz="0 0 5" rpy="0 0 0" />
    </link>

<joint name="sensor_box" type="fixed">
        <parent link="base_link" />
        <child link="sensor_box_link" />
        <origin xyz="${base_length/2} 0 ${base_height}" rpy="0 0 0" />
    </joint>

Bridge

- topic_name: "/camera"
  ros_type_name: "sensor_msgs/msg/Image"
  gz_type_name: "gz.msgs.Image"
  lazy: true
  direction: GZ_TO_ROS

- topic_name: "/camera_info"
  ros_type_name: "sensor_msgs/msg/CameraInfo"
  gz_type_name: "gz.msgs.CameraInfo"
  lazy: true
  direction: GZ_TO_ROS

Add sensor to xacro/urdf file

<gazebo>
        <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
            <render_engine>ogre2</render_engine>
        </plugin>
    </gazebo>

    <gazebo reference="sensor_box_link">
        <sensor name="camera" type="camera">
            <always_on>true</always_on>
            <visualize>true</visualize>
            <update_rate>30</update_rate>
            <topic>camera</topic>
            <gz_frame_id>sensor_box_link</gz_frame_id>
            <camera name="intel_realsense_r200">
                <camera_info_topic>camera_info</camera_info_topic>
                <horizontal_fov>1.02974</horizontal_fov>
                <image>
                    <width>1920</width>
                    <height>1080</height>
                    <format>R8G8B8</format>
                </image>
                <clip>
                    <near>0.02</near>
                    <far>300</far>
                </clip>
                <noise>
                    <type>gaussian</type>
                    <mean>0.0</mean>
                    <stddev>0.007</stddev>
                </noise>
            </camera>
        </sensor>
    </gazebo>


## 4. robot_lidar_sensor

Bridege

- topic_name: "/lidar"
  ros_type_name: "sensor_msgs/msg/LaserScan"
  gz_type_name: "gz.msgs.LaserScan"
  lazy: true
  direction: GZ_TO_ROS

- topic_name: "/lidar/points"
  ros_type_name: "sensor_msgs/msg/PointCloud2"
  gz_type_name: "gz.msgs.PointCloudPacked"
  lazy: true
  direction: GZ_TO_ROS

Lidar box in URDF/XACRO file

<link name="sensor_box_link">
        <visual>
            <geometry>
                <box size="0.05 0.05 0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0" />
            <material name="grey" />
        </visual>
        <collision>
            <geometry>
                <box size="0.05 0.05 0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0" />
        </collision>
        <xacro:box_inertia m="0.2" l="0.5" w="0.5" h="0.5" xyz="0 0 5" rpy="0 0 0" />
    </link>

<joint name="sensor_box" type="fixed">
        <parent link="base_link" />
        <child link="sensor_box_link" />
        <origin xyz="${base_length/2} 0 ${base_height}" rpy="0 0 0" />
    </joint>

 <gazebo reference="sensor_box_link">
        <sensor name='gpu_lidar' type='gpu_lidar'>"
            <pose>0 0 0 0 0 0</pose>
            <topic>lidar</topic>
            <update_rate>2</update_rate>
            <ray>
                <scan>
                    <horizontal>
                        <samples>360</samples>
                        <resolution>1</resolution>
                        <min_angle>-1.5708</min_angle>
                        <max_angle>1.5708</max_angle>
                    </horizontal>
                    <vertical>
                        <samples>1</samples>
                        <resolution>0.01</resolution>
                        <min_angle>0</min_angle>
                        <max_angle>0</max_angle>
                    </vertical>
                </scan>
                <range>
                    <min>0.08</min>
                    <max>10.0</max>
                    <resolution>0.01</resolution>
                </range>
            </ray>
            <always_on>1</always_on>
            <visualize>true</visualize>
            <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
                <render_engine>ogre2</render_engine>
            </plugin>
        </sensor>
    </gazebo>

In launch file

Chnage Robot spawn position

# Transform from base_footprint to base_link
    tf_base_to_footprint = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link'],
    )

    # Transform from base_link to rrbot/base_link/gpu_lidar
    tf_base_to_lidar = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rrbot/base_link/gpu_lidar'],
    )

Gazebo

Add visualize lidar plugin to see lidar lines

RVIZ

Add pointclod2 or laserScan and set the topic name

## 5. robot_contact_sensor

Method 1: All code in SDF file

Add this to SDF file. 

<plugin filename="gz-sim-contact-system" name="gz::sim::systems::Contact">
            </plugin>

Below code is a wall.

<model name='wall'>
    <static>true</static>
    <pose>5 -10 0 0 0 0</pose><!--pose relative to the world-->
    <link name='box'>
        <visual name='visual'>
            <geometry>
                <box>
                    <size>0.5 10.0 2.0</size>
                </box>
            </geometry>
            <!--let's add color to our link-->
            <material>
                <ambient>0.0 0.0 1.0 1</ambient>
                <diffuse>0.0 0.0 1.0 1</diffuse>
                <specular>0.0 0.0 1.0 1</specular>
            </material>
        </visual>
        <collision name='collision'>
            <geometry>
                <box>
                    <size>0.5 10.0 2.0</size>
                </box>
            </geometry>
        </collision>
        <sensor name='sensor_contact' type='contact'>
            <contact>
                <collision>collision</collision>
            </contact>            
        </sensor>
    </link>
    <plugin filename="gz-sim-touchplugin-system" name="gz::sim::systems::TouchPlugin">
        <target>base_link</target>
        <namespace>wall</namespace>
        <time>0.001</time>
        <enabled>true</enabled>
    </plugin>
    </model>

NOTE: URDF method still not found

## 6. robot_depth_camera_sensor

Add bridge code

- topic_name: '/depth_camera/image'
  ros_type_name: "sensor_msgs/msg/Image"
  gz_type_name: "gz.msgs.Image"
  lazy: true
  direction: GZ_TO_ROS

- topic_name: "/depth_camera/image/points"
  ros_type_name: "sensor_msgs/msg/PointCloud2"
  gz_type_name: "gz.msgs.PointCloudPacked"
  lazy: true
  direction: GZ_TO_ROS

- topic_name: "/depth_camera/camera_info"
  ros_type_name: "sensor_msgs/msg/CameraInfo"
  gz_type_name: "gz.msgs.CameraInfo"
  lazy: true
  direction: GZ_TO_ROS

Add to urdf/xacro file

<gazebo>
        <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
            <render_engine>ogre2</render_engine>
        </plugin>
    </gazebo>

    <gazebo reference="sensor_box_link">
        <sensor name="depth_camera" type="depth">
            <update_rate>30</update_rate>
            <always_on>true</always_on>
            <visualize>true</visualize>
            <topic>depth_camera/image</topic>
            <depth_camera>
                <horizontal_fov>1.047</horizontal_fov>
                <image>
                    <width>640</width>
                    <height>480</height>
                    <format>R8G8B8</format>
                </image>
                <clip>
                    <near>0.1</near>
                    <far>10.0</far>
                </clip>
                <noise>
                    <type>gaussian</type>
                    <mean>0.0</mean>
                    <stddev>0.01</stddev>
                </noise>
            </depth_camera>
        </sensor>
    </gazebo>

Add launch file

# Transform from base_footprint to base_link
    tf_base_to_footprint = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link'],
    )

    # Transform from base_link to rrbot/base_link/depth_camera
    tf_base_to_lidar = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'rrbot/base_link/depth_camera'],
    )


## 7. sdf_robot_description

This use SDF file to bring robot up in gazebo with ROS2.