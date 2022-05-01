import rosbag
from src.config import config
from src.laserscan import ydLidarPointsCallback
from src.reward import reward

bag = rosbag.Bag(config.ROS_BAG_PATH, 'r')

topics = [
    '/diffbot/scan',
]

reward.init_memos()

for _, msg, t in bag.read_messages(topics=topics):
    ydLidarPointsCallback(msg)
