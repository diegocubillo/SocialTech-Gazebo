cmake_minimum_required(VERSION 2.8.3)

project(SocialTech-Gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf worlds models )
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
