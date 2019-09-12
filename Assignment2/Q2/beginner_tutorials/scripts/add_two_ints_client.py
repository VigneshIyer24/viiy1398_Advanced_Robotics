#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *
import numpy as np
import matplotlib.pyplot as plt

#for i in range(3):
array1 = []
def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        sending_time = rospy.Time.now()
        resp1 = add_two_ints(x, y)
        lapse_time = rospy.Time.now()-sending_time
        #print lapse_time
        array1.append(1e-6*lapse_time.nsecs)
        print "lapse_time: %s sec %s milliseconds" %(lapse_time.secs,1e-6*lapse_time.nsecs)
        #str(1e-6*lapse_time.nsecs) + "milliseconds"
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
        print "Requesting %s+%s"%(x, y)
        print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
print array1
plt.hist(array1,bins = 'auto')
plt.title('Time taken for client')
plt.xlabel('Recieved server values')
plt.ylabel('Time (ms)')
plt.show()
