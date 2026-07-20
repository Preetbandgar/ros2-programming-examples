#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PoseTrackingSubscriber(Node):
    def __init__(self):
        super().__init__('pose_tracking_node')
        self.subscription_ = self.create_subscription(PoseStamped, 'robot_pose', self.pose_callback, 10)
        self.get_logger().info('The pose tracking node has been started')

    def pose_callback(self, msg):
        frame = msg.header.frame_id
        x_pos = msg.pose.position.x
        y_pos = msg.pose.position.y

        self.get_logger().info(f"[INFO] [PoseTrackingSubscriber]: Frame: {frame} | Position: X={x_pos:.2f}, Y={y_pos: .2f}")

def main(args=None):
    rclpy.init(args=args)
    node = PoseTrackingSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()