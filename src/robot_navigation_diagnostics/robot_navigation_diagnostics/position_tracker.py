#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class PositionTrackerNode(Node):
    def __init__(self):
        super().__init__('position_tracker')
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Odometry Position Tracker Node has been started")

    def odom_callback(self, msg):
        
        y_position = msg.pose.pose.position.y

        self.get_logger().info(f"Current Robot y position: {y_position:.2f} m")

        if abs(y_position) > 2.0:
            self.get_logger().warn(f"Tilt warning! Out of bounds deviation! Y: {y_position:.2f} m")

            safe_twist = Twist()
            safe_twist.linear.y = 1.0
            safe_twist.angular.z = 0.0

            self.cmd_pub.publish(safe_twist)

def main(args=None):
    rclpy.init(args=args)
    node = PositionTrackerNode()
    try:
        rclpy.spin(node)
    except:
        KeyboardInterrupt
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() 