#!/usr/bin/env python3
#
# Copyright 2020, Ben Bongalon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Ben Bongalon (ben.bongalon@gmail.com)

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions.execute_process import ExecuteProcess


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'r2d2.urdf.xml'

    print("urdf_file_name : {}".format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory('urdf_tutorial'),
        urdf_file_name)

    state_publisher = ExecuteProcess(
        cmd=['python3', 'state_publisher.py'],
        output='screen',
        cwd=get_package_share_directory('urdf_tutorial')
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),
        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]
        ),
        #Node(
        #    package='urdf_tutorial',
        #    node_executable='state_publisher',
        #    name='state_publisher',
        #    output='screen'
        #),
        state_publisher
    ])
