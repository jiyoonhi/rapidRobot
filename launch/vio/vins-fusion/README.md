#test

(optor stereo camera + imu) 
$ rosrun optor_stereo_visensor_ros stereo_visensor_node /home/smarthc/catkin_ws/src/optor_stereo_visensor/optor_VISensor_Setups.txt

$ roslaunch vins vins_rviz.launch
$ (1) rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/optor/optor_stereo_imu_config.yaml   (drift 심각<-- )
$ (2) rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/optor/optor_stereo_config.yaml     (ㄱㅊ)

$ (optional 1) rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/optor/optor_stereo_imu_config.yaml
$ (optional 2) rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/optor/optor_stereo_config.yaml

$ (녹화한 경우)rosbag play YOUR_DATASET_FOLDER/Your_bagfile.bag 
$ (실시간) optor 카메라 켜는 노드

>> 이렇게 하면 visual odometry topic인 /vins_estimator/odometry 나오고, 위치 정보만 알려준다. (twist 속도는 ㄴㄴ) 

## 4. KITTI Example
### 4.1 KITTI Odometry (Stereo)
Download [KITTI Odometry dataset](http://www.cvlibs.net/datasets/kitti/eval_odometry.php) to YOUR_DATASET_FOLDER. Take sequences 00 for example,
Open two terminals, run vins and rviz respectively. 
(We evaluated odometry on KITTI benchmark without loop closure funtion)
```
    roslaunch vins vins_rviz.launch
    (optional) rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/kitti_odom/kitti_config00-02.yaml
    rosrun vins kitti_odom_test ~/catkin_ws/src/VINS-Fusion/config/kitti_odom/kitti_config00-02.yaml YOUR_DATASET_FOLDER/sequences/00/ 
```
### 4.2 KITTI GPS Fusion (Stereo + GPS)
Download [KITTI raw dataset](http://www.cvlibs.net/datasets/kitti/raw_data.php) to YOUR_DATASET_FOLDER. Take [2011_10_03_drive_0027_synced](https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/2011_10_03_drive_0027/2011_10_03_drive_0027_sync.zip) for example.
Open three terminals, run vins, global fusion and rviz respectively. 
Green path is VIO odometry; blue path is odometry under GPS global fusion.
```
    roslaunch vins vins_rviz.launch
    rosrun vins kitti_gps_test ~/catkin_ws/src/VINS-Fusion/config/kitti_raw/kitti_10_03_config.yaml YOUR_DATASET_FOLDER/2011_10_03_drive_0027_sync/ 
    rosrun global_fusion global_fusion_node
```


#ISSUE
##문제점1. imu+STEREO Cam --> drift생김;;) --> 아마 카메라와 imu사이의 좌표변환이 잘못된듯 (optor_stereo_imu_config.yaml)
body_T_cam0: !!opencv-matrix
   rows: 4
   cols: 4
   dt: d
   data: [ 4.2812441490024389e-03, -9.9997001507473682e-01,
       -6.4528985710044385e-03, 5.2583356071589790e-05,
       9.9996900935734523e-01, 4.2384270612576547e-03,
       6.6344601088757426e-03, -4.2174706544162562e-02,
       -6.6069110351583190e-03, -6.4811023350536514e-03,
       9.9995717110239080e-01, 1.9238715201769417e-02, 0., 0., 0., 1. ]


### The coordinate of the IMU packaging center in the "left cmos coordinate system"
x = 70.14mm +- 0.06mm
y = -7.38mm +- 0.06mm
z = -1.4mm +- 0.04mm

### Left camera coordinate system 
origin: CMOS sensor array center (image center)

##문제점2. calibration 후 parameter들을 txt, yaml 파일로 얻었는데 (@ ~/rapid/calibdata) optor_stereo_imu_config.yaml의 paramter와 달라서 
덜고쳤다. 
현재까지 수정한 건: ~/rapid/launch/vio/vins-fusion/optor 에서 left_mei.yaml, right_mei.yaml 파일은 다 수정해줌.  
##문제점3. optor camera의 frame_id를 따로 설정해줬다.

