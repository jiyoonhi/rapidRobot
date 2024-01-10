[Execution]
(term1) $ gazebo2.launch
(term2) $ rs_t265_nav.launch
(term3) $ roslaunch nav_amcl.launch

Odometry source <-- robot_localization_with_gps.yaml 

2) imu 
4) visual odometry

localization: AMCL provides tf transform btw map-odom-base_link

TF tree

map - camera_odom_frame - camera_pose_frame 
                        | 
                        ㄴ base_link - wheel_link, imu_link, lidar_link...
