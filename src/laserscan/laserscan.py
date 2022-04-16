# LaserScan msg
from src.reward import reward


def ydLidarPointsCallback(msg):
    assert len(msg.ranges) == 719

    for i in range(0, 719):
        print(i, reward.point_reward(i, msg.ranges[i]))
