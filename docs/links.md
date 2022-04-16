http://wiki.ros.org/rosbag/Cookbook

http://docs.ros.org/en/lunar/api/geometry_msgs/html/msg/Twist.html
http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html
http://docs.ros.org/en/api/tf2_msgs/html/msg/TFMessage.html
http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Image.html

- Только точки, которые образуют опасны для движения
- Самые ближние точки
- Где на каком расстоянии, какая точка находится
- Не обсчитывал лишние точки, децимацию
- Интегральная функция штрафов (векторная функция штрафов?)

https://github.com/Kmortyk/vanilla.robotix.MikeCore/blob/173d0ad6c471b65293376c617a00038234d1187c/src/movement/src/move_v1.cpp#L132