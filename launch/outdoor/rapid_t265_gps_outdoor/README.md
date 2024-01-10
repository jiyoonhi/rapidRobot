[Execution]
(term1) $ gazebo.launch
(term2) $ roslaunch start_navigation_with_gps_ekf.launch

Odometry source <-- robot_localization_with_gps.yaml 

1) wheel odometry
2) imu 
3) gps odometry
4) visual odometry


[visual odometry source]
path: ~/rapid/launch/vio/


[Visual odometry Example]
(1) OPTOR stereo camera + ORB-SLAM2
 - OPTOR stereo camera --> camera/image + imu topic 
 - ORB-SLAM2 --> camera pose + point cloud (map)

 --> imu(optor) + vo(optor+orb-slam2) + gps odom --> fused odom 


