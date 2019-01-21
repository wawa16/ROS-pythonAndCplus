#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



def scan_callback(msg):
  global range_ahead
  range_ahead = min(msg.ranges)

rospy.init_node('wander')
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

range_ahead = 1
fix_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:
    if (range_ahead < 0.8 or rospy.Time.now() > fix_time):
      driving_forward = False;
      fix_time = rospy.Time.now() + rospy.Duration(1)
  else:
    if (rospy.Time.now() > fix_time):
      driving_forward = True
      fix_time = rospy.Time.now() + rospy.Duration(10)
    
  twist = Twist()
  if driving_forward:
    twist.linear.x = 1.5
  else:
    twist.angular.z = 0.6
  cmd_vel_pub.publish(twist)
  rate.sleep()
