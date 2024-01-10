#!/usr/bin/env python

import rospy, time
from ackermann_msgs.msg import AckermannDriveStamped

ack_publisher = None
def drive(steer_val, car_run_speed):
    global ack_publisher
    ack_msg = AckermannDriveStamped()
    ack_msg.drive.steering_angle = steer_val
    ack_msg.drive.speed = car_run_speed
    ack_publisher.publish(ack_msg)

rospy.init_node('yolo_stop_node')
rospy.Subscriber('/darknet_ros/bounding_boxes',
        BoundingBoxes,callback)


for i in range(len(boxes.bounding_boxes)):
    if boxes.bounding_boxes[i].Class == 'person':
        nobody = False

    if nobody:
        drive(0, 1)
    else:
        drive(0, 0)
        print "stop! human detected!"
