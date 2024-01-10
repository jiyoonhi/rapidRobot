(edited by Jiyoon 2021-03-30)

[Execution]
(term0) $ rosrun optor_stereo_sensor_ros stereo_visensor_node /home/smarthc/catkin_ws/src/optor_stereo_visensor/optor_VISensor_Setups.txt
(term1) $ gazebo.launch
(term2-1) $ rosrun vins vins_node ~/catkin_ws/src/rapid/launch/vio/vins-fusion/optor/optor_stereo_config.yaml
(term2-2) $ roslaunch rapid orb_slam2_optor_stereo.launch
(term3) $ roslaunch start_navigation_with_gps_ekf.launch
(term-option) $ rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/optor/optor_stereo_config.yaml

Odometry source <-- robot_localization_with_gps.yaml 

1) wheel odometry
2) imu 
3) gps odometry
4) visual odometry


[visual odometry source]
path: ~/rapid/launch/vio/


[Visual odometry Example]
두 가지 방법이 있으니 둘 중 하나로 바꿀 때마다 start_navsat.launch 파일과 ekf~~.yaml 파일에서 visual odometry 소스 바꿔라.

1) OPTOR stereo camera + ORB-SLAM2
 - OPTOR stereo camera --> camera/image + imu topic 
 - ORB-SLAM2 --> camera pose + point cloud (map)

 --> imu(optor) + vo(optor+orb-slam2) + gps odom --> fused odom 

$ roslaunch rapid orb_slam2_optor_stereo.launch

(TOPIC) 
/orb_slam2_stereo/pose : geometry_msgs/PoseStamped
/odom : nav_msgs/Odometry

- robot_localization pkg : The ekf filter accepts an arbitrary number of inputs from each input message type 
(nav_msgs/Odometry, geometry_msgs/PoseWithCovarianceStamped, geometry_msgs/TwistWithCovarianceStamped, sensor_msgs/Imu).

위에 topic message type이 다른건 문제가 되지 않는듯하다..? --> 아님. 문제됨. start_navsat.launch에서 문제됨.

2) OPTOR stereo camera + VINS-FUSION

 --> imu(optor) + vo(optor+VINS-FUSION) + gps odom --> fused odom 

$ rosrun vins vins_node ~/catkin_ws/src/rapid/launch/vio/optor/optor_stereo_config.yaml

(TOPIC) 
/vins_estimator/odometry : nav_msgs/Odometry


