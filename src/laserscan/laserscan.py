# LaserScan msg
from src.reward import reward


def ydLidarPointsCallback(msg):
    assert len(msg.ranges) == 719

    for phi in range(0, 719):
        r = msg.ranges[phi]

        rew, _ = reward.point_reward(phi, r)

        print(rew)
