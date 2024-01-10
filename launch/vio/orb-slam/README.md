1. (term1) roscore
2. (term2) 
   $ sudo -s
   $ rosrun optor_stereo_visensor_ros stereo_visensor_node /home/smarthc/catkin_ws/src/optor_stereo_visensor/optor_VISensor_Setups.txt

(deprecated) 3. (term3) roslaunch rapid orb_slam2_optor_stereo.launch


published topic: /orb_slam2_stereo/pose --> camera trajectory (visual odom) data 얻을 수 있음.

save map at ~/.ros
4. (term4) rosservice call /orb_slam2_stereo/save_map map.bin


### camera_link 를 base_link로 해놨는데 이걸 바꾸삼..! ㅋ.. minirapid1.urdf.xacro랑도 충돌하니께롱 바꼬야함

### Camera calibration한 결과 ~/rapid/calibrationdata 에 있으니까 txt yaml 파일 참조해서 orb slam2 launch 파일 parameter 바꿨다. 알고보니 ORB-SLAM2 잘못 소스 다운받음 --> 다시 /home/smarthc/ORB-SLAM2에 다운받음. WORD 설명 읽어보삼(OPTOR camera + ORB-SLAM2)

Localization Mode

This mode can be used when you have a good map of your working area. In this mode the Local Mapping and Loop Closing are deactivated. The system localizes the camera in the map (which is no longer updated), using relocalization if needed.
