#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RobotStatus

class RobotStateSubscriber(Node):
    def __init__(self):
        super().__init__('robot_state_subscriber')
        self.subscription_ = self.create_subscription(RobotStatus, 'robot_status', self.status_callback, 10)
        self.get_logger().info('Robot State Subscriber Node has been started')

    def status_callback(self, msg):
        self.get_logger().info(f"Received status: battery: {msg.battery_level}%, Temperature: {msg.motor_temperature}°C, State: {msg.operational_status}")

def main(args=None):
    rclpy.init(args=args)
    node = RobotStateSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()