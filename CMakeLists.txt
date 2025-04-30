cmake_minimum_required(VERSION 3.5)
project(SocialTech-Gazebo)

find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)

foreach(dir config launch meshes urdf worlds models )
	install(DIRECTORY ${dir}/
		DESTINATION share/${PROJECT_NAME}/${dir})
endforeach(dir)

ament_package()