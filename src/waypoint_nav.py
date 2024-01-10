#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#waypoints
waypoints = [
        [(0.99217, 3.201625, 0.0), (0.0, 0.0, 0.749677, 0.6618034)], # chang-go dogu moa-non-got
        [(-1.49242, 2.75139, 0.0), (0.0, 0.0, -0.68145, 0.73186)], # sin-kwan moon-zzock
        [(5.8446335, 0.2001, 0.0), (0.0, 0.0, 0.0, 1.0)],  # beside rapid 
        [(-0.05, -0.17, 0.0), (0.0, 0.0, 0.0, 1.0)]]    # initial pose

#change waypoints to move_base goal
def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose

if __name__ == '__main__':
    rospy.init_node('patrol')
    
    #create action library and wait for server
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

     
    #
    i = 0; 
    while True:
        for pose in waypoints:
            goal = goal_pose(pose)
            client.send_goal(goal)
	    i += 1
            print("waypoint =", i)
            client.wait_for_result()

