#!#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotListener(Node):
    def __init__ (self):
        super().__init__('robot_listener_node')
        self.subscription_ = self.create_subscription(
            String, 'robot_chatter', self.listener_callback, 10)
        self.get_logger().info("Robot Listener Node has started listening....")

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = RobotListener()
    rclpy.spin(node)
    rclpy.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()