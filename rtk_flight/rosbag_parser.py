#!usr/bin/env python3
#be sure to specify filename in this file

#from IPython.core.debugger import set_trace
import rosbag
import pickle
from collections import namedtuple
import numpy as np
from geometry_msgs.msg import Pose


def get_odom(bag):
	drone_sec = []
	drone_nsec = []
	drone_x = []
	drone_y = []
	drone_z = []
	drone_orientation = []

	for topic, msg, t in bag.read_messages(topics=['/ragnarok_ned']):
		drone_sec.append(msg.header.stamp.secs)
		drone_nsec.append(msg.header.stamp.nsecs)
		drone_x.append(msg.pose.position.x)
		drone_y.append(msg.pose.position.y)
		drone_z.append(msg.pose.position.z)
		drone_orientation.append(msg.pose.orientation)

	drone = nedTime(drone_sec, drone_nsec, drone_x, drone_y, drone_z)

	return drone

class nedTime:
	def __init__(self, sec, nsec, north, east, down):

		self.time = np.array(sec)+np.array(nsec)*1E-9

		self.n = north
		self.e = east
		self.d = down
