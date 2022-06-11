import math
import numpy as np
import rosbag
import cv2
from cv_bridge import CvBridge

from src import reward
from src.reward import point_reward
from src.testdata.min_dst import MinDistance

bag = rosbag.Bag('/mnt/sda1/Projects/RosProjects/rosbag/data/2022-05-27-18-41-23.bag', 'r')

# print(bag.get_type_and_topic_info())
# exit(0)

topics = [
    '/scan',
    '/mike_camera/raw'
]

xs1, ys1 = [], []
xs2, ys2 = [], []

reward.init_memos()

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
RADIUS = 2

CX = int(0.5 * CANVAS_WIDTH)
CY = int(0.5 * CANVAS_HEIGHT)

md = MinDistance(20)

count = 0
msgs_count = bag.get_message_count(topic_filters=topics)

last_img = None
bridge = CvBridge()

for topic, msg, t in bag.read_messages(topics=topics):
    if topic == '/mike_camera/raw':
        last_img = msg
        continue

    canvas = np.ones((CANVAS_WIDTH, CANVAS_HEIGHT, 3), dtype=np.uint8) * 255
    md.clear()

    count += 1
    res = 0

    for phi in range(0, 719, 1):
        r = msg.ranges[phi]

        x = r * math.cos(math.radians(phi / 2)) + 1
        y = r * math.sin(math.radians(phi / 2)) + 1

        x = int(x * CANVAS_WIDTH/2)
        y = int(y * CANVAS_HEIGHT/2)

        rew, ok = point_reward(phi, r)
        if ok:
            res += rew
            cv2.circle(canvas, (x, y), radius=RADIUS, color=(0, 255, 255), thickness=-1)
        else:
            cv2.circle(canvas, (x, y), radius=RADIUS, color=(0, 0, 255), thickness=-1)

        cv2.ellipse(canvas, (CX, CY), (int(reward.A * CANVAS_WIDTH/2), int(reward.B * CANVAS_HEIGHT/2)), 0, 0, 360, (255, 0, 255), 1)
        cv2.circle(canvas, (CX, CY), int(reward.R0 * CANVAS_WIDTH/2), (255, 0, 255))
        cv2.arrowedLine(canvas, (CX, CY), (CX-100, CY), (0, 0, 0), 1)

        if ok and md.add_point(x, y):
            cv2.putText(canvas, f"{rew:.2f}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

    cv2.circle(canvas, (CX, CY), radius=RADIUS, color=(0, 255, 0), thickness=-1)
    cv2.putText(canvas, f"{count}/{msgs_count}", (0, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

    if last_img is not None:
        overlay = bridge.imgmsg_to_cv2(last_img)
        overlay = cv2.resize(overlay, (0, 0), fx=0.2, fy=0.2)
        rows, cols, channels = overlay.shape
        canvas[50:50 + rows, 0:0 + cols] = cv2.addWeighted(canvas[250:250 + rows, 0:0 + cols], 0, overlay, 0.5, 0)

    cv2.imshow("sim", canvas)
    cv2.waitKey(10)
