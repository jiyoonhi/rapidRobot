#!/usr/bin/env python

# Import geonav transformation module
import geonav_transform.geonav_conversions as gc
reload(gc)
#import Alvinxy transformation module
import alvinxy.alvinxy as axy
reload(axy)
import rospy
import tf
from nav_msgs.msg import Odometry

def get_xy_based_on_lat_long(lat, lon, name):
   #Define a local origin, latitude and longitude
   olat = 36.8;
   olon = 127.1;

   xg2, yg2 = gc.ll2xy(lat, lon, olat, olon)
