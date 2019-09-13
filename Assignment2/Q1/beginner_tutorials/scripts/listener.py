#!/usr/bin/env python


## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import matplotlib.pyplot as plt
import pylab

from std_msgs.msg import String

message =[]
time_comp = []
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Heard %s', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
	plt.ylabel('Message No')
	plt.xlabel('Time (seconds)')
	for x in range(300):
    		rospy.init_node('listener', anonymous=True)
    		start=rospy.get_time()
		rospy.Subscriber('chatter', String, callback)
		end=rospy.get_time()
		end=end-start
		message.append(x)
		time_comp.append(end)
	
	plt.hist(time_comp,bins =100)
	plt.show()

if __name__ == '__main__':
    listener()
