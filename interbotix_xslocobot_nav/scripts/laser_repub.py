#!/usr/bin/env python

import math
import rospy
from sensor_msgs.msg import LaserScan
import sensor_msgs.msg
import numpy as np

class RepubLaserScan:
    def __init__(self):
        rospy.init_node('revised_scan', anonymous=True)
        # self.scan_topic = rospy.get_param('scan_topic' 'scan')
        # self.scan_topic = '/tb3_0/scan'
      	self.scan_topic = '/locobot/scan'
        self.scan_topic_new = self.scan_topic+"_new"
        sub = rospy.Subscriber( self.scan_topic, LaserScan, self.callback)
        self.pub = rospy.Publisher(self.scan_topic, LaserScan, queue_size = 10)
        self.scann = LaserScan()
        self.scan_data = np.array([])
        rospy.spin()

    def callback(self, msg):
        self.scann = msg
        self.scan_data = np.array(msg.ranges)
        self.scan_data = np.where(np.logical_not(self.scan_data <= 6.0), 5.999999, self.scan_data)
        self.scann.ranges = self.scan_data
        self.pub.publish(self.scann)


if __name__ == '__main__':
    RepubLaserScan()
