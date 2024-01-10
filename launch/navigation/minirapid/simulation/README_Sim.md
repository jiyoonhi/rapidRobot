2021-02-05 jiyoon 

# Gazebo + Map 

(term1)
$ roslaunch sim-gazebo.launch

## (1) cartographer mapping + using wheel odometry 

(term2)
$ roslaunch sim-mapping.launch


## (2) cartographer mapping + publishing odom topic, not using wheel odometry

(term2)
$ roslaunch sim-pub-odom-mapping.launch 



# Gazebo + EKF sensor fusion + Navigation

(term1)
$ roslaunch sim-hec-gazebo.launch

## using wheel_odometry and IMU topics

(term2)
$ roslaunch sim-ekf-nav.launch

You can change options below by changing "sim-ekf-nav.launch" file.

### EKF/UKF sensor fusion 
1. robot_pose_ekf 
2. robot_localization 

### Localization 
1. AMCL
2. Cartographer pure localization mode

### Navigation - Move_base package


# Gazebo + Cartographer(publish odom, not using wheel odom) + Navigation

(term1)
$ roslaunch sim-hec-gazebo.launch

(term2)
$ roslaunch sim-carto-nav.launch


