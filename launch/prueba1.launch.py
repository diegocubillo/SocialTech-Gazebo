from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    ExecuteProcess,
    DeclareLaunchArgument,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    PathJoinSubstitution,
    Command,
    LaunchConfiguration
)
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
from pathlib import Path


def generate_launch_description():
    # launch arguments
    x_arg = LaunchConfiguration("x")
    y_arg = LaunchConfiguration("y")
    yaw_arg = LaunchConfiguration("yaw")

    # default values
    x_arg = DeclareLaunchArgument(
        "x",
        default_value="-1.0",
        description="X coordinate of the robot spawn position",
    )
    y_arg = DeclareLaunchArgument(
        "y",
        default_value="2.0",
        description="Y coordinate of the robot spawn position",
    )

    yaw_arg = DeclareLaunchArgument(
        "yaw",
        default_value="1.570796",
        description="Yaw angle of the robot spawn position",
    )

    gazebo_world = PathJoinSubstitution(
        [FindPackageShare("SocialTech-Gazebo"), "worlds", "ICAI_A501.world"]
    )

    path_to_xacro = (
        Path(get_package_share_directory('SocialTech-Gazebo'))
        / 'urdf'
        / 'tracer2.xacro'
    )

    path_to_urdf = (
        Path(get_package_share_directory('SocialTech-Gazebo'))
        / 'urdf'
        / 'tracer2.urdf'
    )

    create_urdf = ExecuteProcess(
        cmd=[
            'xacro',
            str(path_to_xacro),
            '-o',
            str(path_to_urdf)
        ],
    )

    gui_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("gazebo_ros"), "/launch/gzclient.launch.py"]
        ),
    )

    server_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("gazebo_ros"), "/launch/gzserver.launch.py"]
        ),
        launch_arguments={
            "world": gazebo_world,
            "pause": "false",
            "verbose": "true"
        }.items(),
    )

    tf2_footprint_base = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="tf_footprint_base",
        arguments=[
            "--frame-id", "base_link",
            "--child-frame-id", "base_footprint",
        ],
        output="screen",
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(
                Command(['xacro ', str(path_to_xacro)]), value_type=str
            )
        }]
    )

    # spawn_model node allows obtaining the xml from the following sources:
    # -file is a string containing xml file path
    # -topic is a string containing the name of the topic to get the xml from
    # -database is a string containing the name of the model if within
    #     GAZEBO_MODEL_PATH
    # -stdin is a string containing the xml data from stdin
    spawn_model = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="spawn_model",
        arguments=[
            "-x", "-1.0",
            "-y", "2.0",
            "-z", "0.0",
            "-Y", "1.570796",
            "-entity", "tracer2",
            "-file", str(path_to_urdf)
        ],
        output="screen",
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=[
            "-d",
            PathJoinSubstitution([
                FindPackageShare("SocialTech-Gazebo"),
                "rviz",
                "model_display.rviz"
            ])
        ],
        output="screen",
    )

    fake_calibration = ExecuteProcess(
        cmd=[
            "ros2",
            "topic",
            "pub",
            "--once",
            "/calibrated",
            "std_msgs/msg/Bool",
            "{data: true}"
        ],
        output="screen",
    )

    return LaunchDescription([
        x_arg,
        y_arg,
        yaw_arg,
        gui_launcher,
        server_launcher,
        create_urdf,
        tf2_footprint_base,
        robot_state_publisher_node,
        spawn_model,
        rviz2,
        fake_calibration
    ])



# <launch>
#   <arg name="world_name" default="$(find SocialTech-Gazebo)/worlds/ICAI_A501.world"/>
#       <arg name="x" default="-1.0"/>
#     <arg name="y" default="2.0"/>
#     <arg name="z" default="0.0"/>
#     <arg name="yaw" default="1.570796"/>
    
    
#     <include file="$(find gazebo_ros)/launch/empty_world.launch">
#         <arg name="world_name" value="$(arg world_name)"/>
#         <arg name="paused" value="false"/>
#         <arg name="use_sim_time" value="true"/>
#         <arg name="gui" value="true"/>
#         <arg name="headless" value="false"/>
#         <arg name="debug" value="false"/>
#     </include>
    
#   <node
#     name="tf_footprint_base"
#     pkg="tf"
#     type="static_transform_publisher"
#     args="0 0 0 0 0 0 base_link base_footprint 40" />

#     <param
#     name="robot_description"
#    command="$(find xacro)/xacro '$(find SocialTech-Gazebo)/urdf/tracer2.xacro'" />
    
#   <node
#     name="spawn_model"
#     pkg="gazebo_ros"
#     type="spawn_model"
#     args="-x $(arg x)
#               -y $(arg y)
#               -z $(arg z)
#               -Y $(arg yaw) 
#               -param robot_description -urdf -model tracer2"
              
#     output="screen" />
    


#   <node
#     name="robot_state_publisher"
#     pkg="robot_state_publisher"
#     type="robot_state_publisher" />
 
#  <node
#     name="joint_state_publisher"
#     pkg="joint_state_publisher"
#     type="joint_state_publisher" />
      
#         <node name="rviz" pkg="rviz" type="rviz" args="-d $(find SocialTech-Gazebo)/rviz/model_display.rviz" />
