#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *
import numpy as np
import matplotlib.pyplot as plt

#for i in range(3):
time_taken = []
response_number =[]
def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        start_time = rospy.get_time()
        resp1 = add_two_ints(x, y)
        end_time = rospy.get_time()-start_time
        #print time difference
        time_taken.append(end_time)
        print "Time Taken: %s sec" %(end_time)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

for i in range(300):
    if __name__ == "__main__":
        rospy.init_node('node1')

        if len(sys.argv) == 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
        else:
            print usage()
            sys.exit(1)
	response_number.append(i)
        print "Requesting %s+%s"%(x, y)
        print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))

plt.hist(time_taken,bins ='auto')
plt.title('Time taken for client')
plt.xlabel('Time Taken (s)')
plt.ylabel('Recived values frequecny on the given time')
plt.show()
