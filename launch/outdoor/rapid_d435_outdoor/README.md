(edited by Jiyoon 2021-04-05)

[Execution with gps]
(term1) $ gazebo.launch
(term2) $ roslaunch start_navigation_with_gps_ekf.launch

[Execution with no gps but visual odometry]
(term1) $ gazebo.launch
(term2) $ roslaunch nav.launch

Odometry source <-- robot_localization_with_gps.yaml 

1) wheel odometry
2) imu 
3) gps odometry
4) visual odometry


[visual odometry source]
path: ~/rapid/launch/vio/


[Visual odometry Example]
(1) realsense d435 camera + VINS-FUSION 

(TOPIC) 
/vins_estimator/odometry : visual odometry (world frame)

--> imu(other) + vo(d435+vins-fusion) + gps odom --> fused odom 


(2) realsense d435 camera + ORB-SLAM2
 - OPTOR stereo camera --> camera/image + imu topic 
 - ORB-SLAM2 --> camera pose + point cloud (map)

 --> imu(optor) + vo(optor+orb-slam2) + gps odom --> fused odom 


(TOPIC) 
/orb_slam2_stereo/pose : geometry_msgs/PoseStamped
/odom : nav_msgs/Odometry

- robot_localization pkg : The ekf filter accepts an arbitrary number of inputs from each input message type 
(nav_msgs/Odometry, geometry_msgs/PoseWithCovarianceStamped, geometry_msgs/TwistWithCovarianceStamped, sensor_msgs/Imu).

위에 topic message type이 다른건 문제가 되지 않는듯하다..? 


