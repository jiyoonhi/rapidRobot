#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

class OdomEKF():
   def __init__(self):
       # Give the node a name
       rospy.init_node('odom_ekf', anonymous=False)

       # Publisher of type nav_msgs/Odometry
       self.ekf_pub = rospy.Publisher('odom_ekf', Odometry, queue_size=10)
       
       # Wait for the /odom_combined topic to become available (topic name is robot_pose_ekf/odom_combined. frameid is odom!! don't worry!)
       rospy.wait_for_message('robot_pose_ekf/odom_combined', PoseWithCovarianceStamped)
       
       # Subscribe to the /odom_combined topic
       rospy.Subscriber('robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, self.pub_ekf_odom)
       
       rospy.loginfo("Publishing combined odometry on /odom_ekf")
       
   def pub_ekf_odom(self, msg):
       odom = Odometry()
       odom.header = msg.header
       odom.header.frame_id = 'odom'
       odom.child_frame_id = 'base_link'
       odom.pose = msg.pose
       
       self.ekf_pub.publish(odom)
       
if __name__ == '__main__':
   try:
       OdomEKF()
       rospy.spin()
   except:
       pass
