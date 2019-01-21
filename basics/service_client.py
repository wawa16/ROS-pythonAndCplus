#!/usr/bin/env python
import rospy
from basics.srv import WordCount,WordCountRequest


rospy.init_node('service_client')

rospy.wait_for_service('word_count')

word_count_local = rospy.ServiceProxy('word_count',WordCount)

words = "I am Waleed learning ROS!"
print word_count_local(words).count
rospy.spin()