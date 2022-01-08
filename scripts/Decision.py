#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import Int32

rospy.init_node('Decision')
pub = rospy.Publisher('Decision_push', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
	n = random.randint(5,13)
	pub.publish(n)
	rate.sleep()
