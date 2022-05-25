#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float64
import numpy as np


def sq_size_gen():
	pub =   rospy.Publisher('square', Float64, queue_size=10)
	rospy.init_node('sq_size_gen', anonymous=True)
	rate = rospy.Rate(0.05) # 
	
	
	while not rospy.is_shutdown():
        	sq_msg = random.uniform(0.05, 0.20)
        	rospy.loginfo(sq_msg)
        	pub.publish(sq_msg)
        	rate.sleep()
	

if __name__ == '__main__':
    try:
        sq_size_gen()
    except rospy.ROSInterruptException:                            
        pass
