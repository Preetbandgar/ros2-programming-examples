#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotSpeaker(Node):
    def __init__(self):
        super().__init__('robot_speaker_node')
        self.publisher_ = self.create_publisher(String, 'robot_chatter', 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Robot Speaker Node has started broadcasting")
        self.counter_ = 100

    def timer_callback(self):
        msg = String()
        self.counter_ -= 5
        msg.data = f"Robot self-destruct sequence: {self.counter_} seconds remaining!"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = RobotSpeaker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()