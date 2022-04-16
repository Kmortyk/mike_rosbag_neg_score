import rosbag
from src.config import config
from src.laserscan import ydLidarPointsCallback

bag = rosbag.Bag(config.ROS_BAG_PATH, 'r')

topics = [
    '/diffbot/scan',
]

for _, msg, t in bag.read_messages(topics=topics):
    ydLidarPointsCallback(msg)
