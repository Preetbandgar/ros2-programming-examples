#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatteryDrain(Node):
    def __init__(self):
        super().__init__('battery_drain_node')
        self.publisher_ = self.create_publisher(Int32, 'battery_level', 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Robot Battery Drain Node has been started")
        self.battery_level = 101

    def timer_callback(self):
        msg = Int32()
        self.battery_level -= 1
        msg.data = self.battery_level
        self.publisher_.publish(msg)
        if self.battery_level < 20:
            self.get_logger().info(f'WARNING: Battery Low! Returning to charging dock...')
        else:
            self.get_logger().info(f'Robots battery percentage is: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryDrain()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()