cmake_minimum_required(VERSION 2.8.3)
project(imu_calibration)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
)
