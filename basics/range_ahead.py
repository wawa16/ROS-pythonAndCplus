#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

def Callback(msg):
  range_ahead = msg.ranges[len(msg.ranges)/2]
  print "range ahead: %0.1f" %range_ahead


rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan',LaserScan,Callback)
rospy.spin()
