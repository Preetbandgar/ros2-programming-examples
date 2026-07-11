#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PoseTrackingSubscriber(Node):
    def __init__(self):
        super().__init__('pose_tracking_node')
        self.subscription_ = self.create_subscription(PoseStamped, 'robot_pose', self.timer_callback, 10)
        self.get_logger().info('The pose tracking node has been started')

    def timer_callback(self, msg):
        msg = PoseStamped()
        self.get_logger().info(f"[INFO] [PoseTrackingSubscriber]: Frame: {msg.header.frame_id} | Position: X={msg.pose.position.x}, Y={msg.pose.position.y}")

def main(args=None):
    rclpy.init(args=args)
    node = PoseTrackingSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()