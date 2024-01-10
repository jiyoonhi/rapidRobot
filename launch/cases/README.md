1-1. [sim] AMCL + Localization(predefined map) + Odom(Gazebo ideal encoder) + lidar(gazebo ideal lidar)
1-2. [real] AMCL + Localization(predefined map) + Odom(real encoder) + lidar (real lidar)

2-1. [sim] Carto + Localization(predefined map) + Lidar only (gazebo ideal lidar) 
2-2. [real] Carto + Localization(predefined map) + Lidar only (with real robot)

3-1. [sim] Carto + Localization(predefined map) + Odom(Gazebo ideal encoder) + Lidar only (gazebo ideal lidar) 
3-2. [real] Carto + Localization(predefined map) + Odom(real encoder) + Lidar only (with real robot)

1-3. [sim] AMCL + Localization(predefined map) + Odom(EKF = Gazebo ideal encoder + IMU) + lidar (gazebo ideal lidar)
1-4. [real] AMCL + Localization(predefined map) + Odom(EKF = real encoder + IMU) + lidar (real lidar)
3-3. [sim] Carto + Localization(predefined map) + Odom(EKF = Gazebo ideal encoder + IMU) + lidar (gazebo ideal lidar)
3-4. [real] Carto + Localization(predefined map) + Odom(EKF = real encoder + IMU) + lidar (with real robot)
