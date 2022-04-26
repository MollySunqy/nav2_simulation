# Author: Addison Sears-Collins
# Date: September 2, 2021
# Description: Launch a basic mobile robot using the ROS 2 Navigation Stack
# https://automaticaddison.com

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  pkg_share = FindPackageShare(package='basic_mobile_robot').find('basic_mobile_robot')


  nav2_params_path = os.path.join(pkg_share, 'params', 'image_scan_node.yaml')



  declare_params_file_cmd = DeclareLaunchArgument(
    name='params_file',
    default_value=nav2_params_path,
    description='Full path to the ROS2 parameters file to use for all launched nodes')
    

  
  # Start converting depth image to laser scan
  start_depthimage_to_laserscan_cmd = Node(
    package='depthimage_to_laserscan',
    executable='depthimage_to_laserscan_node',
    name='image_scan_node',
    # parameters=[{'reliability': 'best_effort'}],
    remappings=[('/depth','/depth_camera/depth/image_raw'),
                ('/depth_camera_info','/depth_camera/depth/camera_info')
    ]

  )

  # Create the launch description and populate
  ld = LaunchDescription()

  # Declare the launch options

  ld.add_action(declare_params_file_cmd)


  ld.add_action(start_depthimage_to_laserscan_cmd)


  return ld

