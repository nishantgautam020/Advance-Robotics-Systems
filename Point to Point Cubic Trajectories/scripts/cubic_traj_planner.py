#!/usr/bin/env python

import rospy
import random
from ar_week5_test.msg import cubic_traj_params
from ar_week5_test.msg import cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
	compute_cubic(data)


def cubic_traj_planner():
	rospy.init_node('planner')    
	rospy.Subscriber("params", cubic_traj_params,callback)
	rospy.spin()

def compute_cubic(data):

	compute = computation_client(data.p0,data.pf,data.v0,data.vf,data.t0,data.tf)
	pub=rospy.Publisher('coeffs',cubic_traj_coeffs,queue_size=10) 
        print(compute)
        computed= cubic_traj_coeffs() 
	computed.a0=compute[0]
	computed.a1=compute[1]
	computed.a2=compute[2]
	computed.a3=compute[3]
	computed.t0=data.t0
	computed.tf=data.tf 
        rospy.loginfo(computed)  
	pub.publish(computed)  

def computation_client(p0,pf,v0,vf,t0,tf):
    rospy.wait_for_service('compute_cubic')
    try:
        computation = rospy.ServiceProxy('compute_cubic', compute_cubic_traj)  
        resp = computation(p0,pf,v0,vf,t0,tf) 
        return resp.a0, resp.a1, resp.a2, resp.a3
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == '__main__':
	cubic_traj_planner()
