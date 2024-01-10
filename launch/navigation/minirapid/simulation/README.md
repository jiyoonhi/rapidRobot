2021-02-05 jiyoon 

//////////////////////
/// 준비
step 1.  전원
wifi 전원 켜기 (인터넷 필요화면 화웨이도 켜자!!)
PC 켜기 (멀티 부팅 디폴트 우분트 (그냥 놔두면 됨), 로그인 smarthc@asdf8836, wifi iptime으로 잘 잡혔는지 확인)  
자비어 켜기 (화면이 안보이는 상태, PC에서 로그인 방법)

step 2. 접속 

PC에서 터미널 열기 ssh 접속
ssh ryudolf@192.168.0.182
(pass : ryudolf123)

step 3. PC 에서 ROS core 실행
(PC측 terminal) roscore


/////////////////////////




[Remote PC] location: ~/rapid/launch/navigation/minirapid/simulation/
[Jetson xavier AGX] location: anywhere

Remote PC의 경우 이하의 모든 명령은 해당폴더로 이동후 사용
cd ~/catkin_ws/src/rapid/launch/navigation/minirapid/simulation/

# Real robot + Mapping
[Remote PC]
(term1)
$ roscore
## (1) cartographer mapping + using wheel odometry 
[Jetson xavier AGX]
(term1)
$ roslaunch rplidar_ros rplidar_a3.launch
(term2)
$ roslaunch roboclaw_node roboclaw.launch

[Remote PC]
(term2)
$ roslaunch sim-mapping.launch


## (2) cartographer mapping + publishing odom topic, not using wheel odometry
[Jetson xavier AGX]
(term1)
$ roslaunch rplidar_ros rplidar_a3.launch

[Remote PC]
(term2)
$ roslaunch sim-pub-odom-mapping.launch 

<<<강추>>>
# Real robot + Cartographer(publish odom, not using wheel odom) + Navigation
[Jetson xavier AGX]
(term1)
$ roslaunch rplidar_ros rplidar_a3.launch
(term2)
$ roslaunch roboclaw_node roboclaw.launch
//여기서 모터 드라이버 켜기 전에 꼭 바꿔야 할 것//
(vim ~/catkin_ws/src/roboclaw_ros/roboclaw_node/nodes/roboclaw_node.py line 92, 96에서 odom을 odom_carto로 바꾸고 catkin_make 후 launch 파일 실행해야 한다.) 
여기서 실행할 때 빼고는 odom으로 frame_id가 설정되어 있어야 한다...

[Remote PC]
(term2)
$ roslaunch sim-carto-nav.launch

(OLD TF WARNING 발생시 대처) : rviz왼쪽 하단에 reset버튼 누르기

# Real robot + EKF sensor fusion + Navigation

## using wheel_odometry and IMU topics
[Jetson xavier AGX]
(term1)
$ roslaunch rplidar_ros rplidar_a3.launch
(term2)
$ roslaunch roboclaw_node roboclaw.launch
(term3)
$ roslaunch wit_node wit.launch

OR (한번에 다 켜기 스크립트)
(term1)
$ roslaunch rapid minirapid_sensor.launch

(오류발생시 대처)
주원인1 : USB꽂는 순서에 따라 포트 번호 바뀌는 문제 (라이다(/dev/ttyUSB0), IMU(/dev/ttyUSB1) 
 확인해서 ls -l /dev/ttyUSB* 오류나는 경우 포트뒤집기 (vim ~/catkin_ws/src/rplidar_ros/launch/rplidar_a3.launch 수정 vim ~/catkin_ws/src/wit_node/launch/wit.launch)
주원인2 : 하드웨어 권한 부족 >> 해결방법 (usb0, usb1, motor) >> bashrc의 alias 확인
주원인3 : cartographer로 localization하는 경우에는 최대한 mapping할 때 초기위치에 두고 해야 잘된다. 안그러면 라이다가 빙빙 도는 것처럼 rviz 상에서 보인다.


[Remote PC]
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


