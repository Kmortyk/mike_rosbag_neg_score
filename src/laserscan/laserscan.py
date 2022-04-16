# LaserScan msg
def ydLidarPointsCallback(msg):
    assert len(msg.ranges) == 719

    

    print(len(msg.ranges))
