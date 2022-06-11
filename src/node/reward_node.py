import time

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image, LaserScan
from src.laserscan import ydLidarPointsCallback
from src.node import config
from src.reward import reward

# initialize reward module nodes
print("[⌛] init memos ...")
reward.init_memos()

class RewardNode:
    def __init__(self):
        rospy.init_node(self.name(), anonymous=False)
        self.pub = rospy.Publisher(self.name(), Float64, queue_size=config.PUBLISH_QUEUE_SIZE)

    def callback(self, msg):
        calc_reward = ydLidarPointsCallback(msg)
        print(f"[✉][{time.time()}] publish score {calc_reward}.")
        self.pub.publish(calc_reward)

    def start(self):
        rospy.Subscriber('diffbot/scan', LaserScan, self.callback)
        rospy.spin()

    @staticmethod
    def name() -> str:
        return 'reward_node'

if __name__ == '__main__':
    print("[⌛] start node ...")
    RewardNode().start()
