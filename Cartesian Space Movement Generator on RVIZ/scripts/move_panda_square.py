#!/usr/bin/env python

import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from std_msgs.msg import Int64, Float64


def move_panda_square():
	rospy.init_node('move_panda_square', anonymous=True)
	print('-----------Waiting For The Square Size-------------')
	rospy.Subscriber('square', Float64, callback)
	rospy.spin()

def callback(data):
	    try:
        	# Building robot's starting configuration
        	start_conf = [0, -pi / 4, 0, -pi / 2, 0, pi / 3, 0]

        	# Moving the robot to the starting configuration
        	group.go(start_conf, wait=True)

		# stop function (for no residual mmovement)
        	group.stop()

        	# initialise an empty array for the positions
        	way_pts = []

        	# Defining current group positions
        	pos = group.get_current_pose().pose
		
		
		pos.position.z -= data.data
#		way_pts.append(copy.deepcopy(pos))

		pos.position.y += data.data  # First Motion
		way_pts.append(copy.deepcopy(pos))
		
		pos.position.x += data.data  # Second Motion
		way_pts.append(copy.deepcopy(pos))

		pos.position.y -= data.data  # Third Motion
		way_pts.append(copy.deepcopy(pos))

		pos.position.x -= data.data  # Final Motion
		way_pts.append(copy.deepcopy(pos))


		# Computing the path to follow on the cartesian space
		(plan,fraction) = group.compute_cartesian_path(way_pts,0.01,0.0)  

		# Trajectory Planner
		disp_traj = moveit_msgs.msg.DisplayTrajectory()
		disp_traj.trajectory_start = robot.get_current_state()
		disp_traj.trajectory.append(plan)
		
		print '------------------- Planned Trajectory Preview -------------------'
		display_trajectory_publisher.publish(disp_traj)
		time.sleep(5)

		# Executing the planned trajectory
		print '------------------- Executing the Trajectory -------------------'
		group.execute(plan, wait=True)

	    except rospy.ServiceException, e:
	        print("Service call failed: %s" % e)


if __name__ == "__main__":

    moveit_commander.roscpp_initialize(sys.argv)
    # initialise robot commander
    robot = moveit_commander.RobotCommander()

    # initialise scene planning interface
    scene = moveit_commander.PlanningSceneInterface()

    # initialise move group commander
    group = moveit_commander.MoveGroupCommander('panda_arm')

    # initialise display trajectory publisher
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=0)
    move_panda_square()


#if __name__ == '__main__':
#    try:
#        move_panda_square()
#    except rospy.ROSInterruptException:
#        pass
