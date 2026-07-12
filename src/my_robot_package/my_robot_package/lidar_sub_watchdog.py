#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class FakeLidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_watchdog_node')
        self.scan_sub = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        self.get_logger().info('LiDAR watchdog node has been started...')

    def scan_callback(self, msg):
        
        middle_index = len(msg.ranges) // 2

        reading = msg.ranges[middle_index]

        if reading < 1.0:
            self.get_logger().warning(f"[Warning]:'The distance {reading: .1f} m is less than 1.0 m")


def main(args=None):
    rclpy.init(args=args)
    node = FakeLidarSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node
    rclpy.shutdown()

if __name__ == '__main__':
    main()