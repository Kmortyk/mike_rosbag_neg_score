from src.reward import reward


def ydLidarPointsCallback(msg) -> float:
    assert len(msg.ranges) == 719

    res = 0

    for phi in range(0, 719, 1):
        r = msg.ranges[phi]
        rew, ok = reward.point_reward(phi, r)
        if ok:
            res += rew

    return res
