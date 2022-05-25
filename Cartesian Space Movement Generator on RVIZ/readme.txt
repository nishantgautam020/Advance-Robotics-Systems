STUDENT DETAILS
~~~~~~~~~~~~~~~
* Student Name : NISHANT GAUTAM
* Student ID: 210832761
* Student Email ID: n.gautam@se21.qmul.ac.uk

CONTENTS
~~~~~~~~~~~~~~~~~~~~~~
* Zip pack contains 5 Folders naming src, scripts, launch,  scripts, msg and srv. 
* Scripts comprises of 2 ROS Nodes (.py files) titled "square_size_generator.py" and "move_panda_square.py"

Creating Environment
~~~~~~~~~~~~~~~~~~~~~~~
Download and Install the Repositories ::
git clone -b melodic-devel https://github.com/ros-planning/panda_moveit_config.git
git clone -b melodic-devel https://github.com/ros-planning/Moveit_tutorials.git


How To Run
~~~~~~~~~~~~~~~
unzip ar_week10_test.zip in the src folder of  the catkin workspace.

Build catkin workspace using catkin_make command.

Execute the following 4 commands within separate terminals :

1) roslaunch panda_moveit_config demo.launch: Launches the RVIZ platform for Panda Robot Visuals.
2) rosrun ar_week10_test square_size_generator.py
3) rosrun ar_week10_test move_panda_square.py
4) rosrun rqt_plot rqt_plot

DEPENDENCIES
~~~~~~~~~~~~~~~
* Python ()
* ros-melodic
* catkin
* Rospy
* moveit: commander and msgs.


STEPS
~~~~~~~~
- Creat catkin workspace using catkin_make.
- Create a package titled "ar_week_10_test" and along with the above mentioned dependencies.
- Packege Operations: Customization, Building etc.
- Creating Nodes- 2 nodes
