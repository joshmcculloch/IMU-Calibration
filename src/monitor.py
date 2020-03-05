#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu

class Stats(object):

    def __init__(self, count):
        self.data = [[] for i in range(count)]

    def update(self, values):
        for i,v in enumerate(values):
            self.data[i].append(v)

    def report(self):
        for i,values in enumerate(self.data):
            mean = sum(values)/len(values)
            var = sum([(v-mean)**2 for v in values])/len(values)
            print(i,mean, var)


stats = Stats(10)

def callback(data):
    stats.update([data.orientation.x,
    data.orientation.y,
    data.orientation.z,
    data.orientation.w,
    data.angular_velocity.x,
    data.angular_velocity.y,
    data.angular_velocity.z,
    data.linear_acceleration.x,
    data.linear_acceleration.y,
    data.linear_acceleration.z])


    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

def listener():

    rospy.init_node('monitor', anonymous=True)

    rospy.Subscriber("/imu/imu", Imu, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    stats.report()
