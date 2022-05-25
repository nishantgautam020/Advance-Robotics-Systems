#!/usr/bin/env python

import rospy
import random
import numpy as np
from ar_week5_test.msg import cubic_traj_params


# MESSAGE PUBLISHING


def points_generator(): 
    pub = rospy.Publisher('params', cubic_traj_params, queue_size=10)  #Topic Defined
    rospy.init_node('generator')                                       #initializing publisher node and appending random integers.
    rate= rospy.Rate(0.05)                                             #printing messages after 20 second
    cubic= cubic_traj_params()
    while not rospy.is_shutdown():
	cubic.p0= np.random.uniform(-10 ,10)
	cubic.pf= np.random.uniform(-10 ,10)
	cubic.v0= np.random.uniform(-10 ,10)
	cubic.vf= np.random.uniform(-10 ,10)
	cubic.t0= 0
	cubic.tf= round(np.random.uniform(5 ,10))
	rospy.loginfo(cubic)     
	pub.publish(cubic)        
	rate.sleep()             

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:                            
        pass
