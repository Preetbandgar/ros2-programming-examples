#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class GoalMarker(Node):
    def __init__(self):
        super().__init__('goal_marker_publisher')
        self.marker_pub = self.create_publisher(Marker, '/visual_goal_marker', 10)
        self.timer = self.create_timer(1.0, self.publish_marker)
        self.get_logger().info("Goal Marker publisher node has been started...")

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = 'map'
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = 'target_goal'
        marker.id = 100
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        
        marker.pose.position.x = 5.0
        marker.pose.position.y = 3.0
        marker.pose.position.z = 0.0
        marker.pose.orientation.w = 1.0
        
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        self.marker_pub.publish(marker) 

        self.get_logger().info(
            f"Published goal marker at x={marker.pose.position.x:.2f},"
            f"Published goal marker at y={marker.pose.position.y:.2f},"
            f"Published goal marker at z={marker.pose.position.z:.2f}"
            )

def main(args=None):
    rclpy.init(args=args)
    node = GoalMarker()
    try:
        rclpy.spin(node)
    except:
        KeyboardInterrupt
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()