# rapid package

## ros master (Remote PC)

$ roscore

## joystick (Jetson Xavier AGX board)

$ roslaunch teleop_twist_joy teleop.launch

## Sensor bringup (Jetson Xavier AGX board)

$ roslaunch rapid minirapid_sensor.launch

## SLAM - Cartographer (Remote PC)

$ roslaunch rapid minirapid+imu_cartographer_mapping.launch

## Navigation (Remote PC)

### global path planner --> A* 
### local path planner --> dwa local planner

1) localization - cartographer

   $ roslaunch rapid minirapid_carto_lab_global.launch

2) localization - amcl

   $ roslaunch rapid minirapid_lab_global.launch

3) localization - robot_pose_ekf

   rplidar a3 + zed camera + imu --> odom

   $ roslaunch rapid lab_odom.launch

4) localization - robot_localization


# robot_pose_ekf
sensors: RPLidar a3, gpsimu(imu only), zed camera

odometry --> robot_pose_ekf 이용해서 zed/zed_node/odom + imu = fused odometry (odom)

$ roslaunch rapid rapid_lab_odom.launch
