#!/usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_coeffs
from std_msgs.msg import Float64

def callback(data):
    # publishing initialised
    pub1 = rospy.Publisher('trajpos', Float64, queue_size=0)
    pub2 = rospy.Publisher('trajVel', Float64, queue_size=0)
    pub3 = rospy.Publisher('trajAccel', Float64, queue_size=0)
    
    rate = rospy.Rate(30)

    time = data.t0
    while time < data.tf:
        # calculate trajectories
        pos = data.a0 + data.a1 * time + data.a2 * (time**2) + data.a3 * (time**3)
        vel = data.a1 + 2 * data.a2 * time + 3 * data.a3 * (time**2)
        accel = 2 * data.a2 + 6 * data.a3 * time
    

        # publish messages
        print('Publishing trajectories %d, %d, %d' % (pos, vel, accel))

        pub1.publish(pos)
        pub2.publish(vel)
        pub3.publish(accel)

        time += 0.3
        rate.sleep()

def plot_cubic_traj():
    # initialising new node
    rospy.init_node('plotter')
    # subscribe to cubic_traj_params
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)
    # prevent it from dying
    rospy.spin()

if __name__ == "__main__":
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass
