from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
  gazebo_world = PathJoinSubstitution(
    [FindPackageShare("SocialTech-Gazebo"), "worlds", "ICAI_A501.world"]
  )

  gui_launcher = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([FindPackageShare("gazebo_ros"), "/launch/gzclient.launch.py"]),
  )

  server_launcher = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([FindPackageShare("gazebo_ros"), "/launch/gzserver.launch.py"]),
      launch_arguments={
        "world": gazebo_world,
        "paused": "false"
      }.items(),
  )

  tf2_footprint_base = Node(
      package="tf2_ros",
      executable="static_transform_publisher",
      name="tf_footprint_base",
      arguments=["0", "0", "0", "0", "0", "0", "base_link", "base_footprint"],
      output="screen",
  )

  rviz2 = Node(
      package="rviz2",
      executable="rviz2",
      name="rviz2",
      arguments=["-d", PathJoinSubstitution([FindPackageShare("SocialTech-Gazebo"), "rviz", "model_display.rviz"])],
      output="screen",
  )

  return LaunchDescription([
    gui_launcher,
    server_launcher,
    tf2_footprint_base,
    rviz2,
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
    
#   <node
#     name="fake_joint_calibration"
#     pkg="rostopic"
#     type="rostopic"
#     args="pub /calibrated std_msgs/Bool true" />
# </launch>
