import rosbag_parser
import matplotlib.pyplot as plt
from IPython.core.debugger import set_trace
import rosbag
import numpy as np
from collections import namedtuple

def main():

	filename = 'j_pitch_2020-11-18-13-45-05.bag'
	bag = rosbag.Bag('../../../../Downloads/' + filename)

	odom = get_odom(bag)
	set_trace()

def plot_2(fig_num, t_x, x, xlabel, t_y, y, ylabel):

	plt.figure(fig_num)
	plt.plot(t_x, x, label = xlabel)
	plt.plot(t_y, y, label = ylabel)
	plt.legend(loc = "upper right")
	plt.show()


if __name__ == '__main__':
	main()
