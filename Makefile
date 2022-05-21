# start fake laser scan node
start_fake_laser_scan:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)" && python3 src/node/fake_laser_scan.py

# starts reward node
start_node:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)" && python3 src/node/reward_node.py

# install required ros dependencies
deps-ros-install:
	pip3 install --extra-index-url https://rospypi.github.io/simple/ rospy rosbag rospkg roslz4 sensor_msgs geometry_msgs cv_bridge