import random
import time

import rospy
from sensor_msgs.msg import LaserScan
from src.node import config

class FakeLaserScan:
    def __init__(self):
        rospy.init_node(self.name(), anonymous=False)
        self.pub = rospy.Publisher(self.topic(), LaserScan, queue_size=config.PUBLISH_QUEUE_SIZE)

    def start(self):
        while not rospy.is_shutdown():
            msg_scan = LaserScan()
            msg_scan.ranges = [random.randint(0, 100) for _ in range(719)]

            print(f"[✉][{time.time()}] publish fake scan data.")
            self.pub.publish(msg_scan)
            rospy.sleep(1)

    @staticmethod
    def name() -> str:
        return config.TOPIC_FIRST_PART

    @staticmethod
    def topic() -> str:
        return config.TOPIC_LAST_PART

if __name__ == '__main__':
    FakeLaserScan().start()
