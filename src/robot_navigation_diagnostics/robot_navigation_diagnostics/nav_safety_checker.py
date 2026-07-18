#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from nav_msgs.msg import OccupancyGrid

class NavSafetyCheckerNode(Node):
    def __init__(self):
        super().__init__('nav_safety_checker')
        self.path_sub = self.create_subscription(Path, '/plan', self.path_callback, 10)

        self.map_sub = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 10)
        self.get_logger().info('The Navigation safety checker node Initialized.....')

    def path_callback(self, msg):
        count = len(msg.poses)

        if count > 0:
            final_waypoint = msg.poses[-1]

            destination_x = final_waypoint.pose.position.x
            destination_y = final_waypoint.pose.position.y

            self.get_logger().info(f"Path detected! Total waypoints: {count}")
            self.get_logger().info(f"Target Destination - X: {destination_x:.2f}m, Y: {destination_y:.2f}m")
            
            if destination_x > 10.0:
                self.get_logger().warn("Target destination is too far for safe operation!")
        else:
            self.get_logger().info("Receievd an empty path plan") 

    def map_callback(self, msg):
        map_resolution = msg.info.resolution
        map_width = msg.info.width
        map_height = msg.info.height

        self.get_logger().info(f"---- Map Metrics Received----")
        self.get_logger().info(f"Grid Size: {map_width} * {map_height} cells") 
        self.get_logger().info(f"Resolution scale: {map_resolution:.3f} meteres per cell")  

def main(args=None):
    rclpy.init(args=args)
    node = NavSafetyCheckerNode()
    try:
        rclpy.spin(node)
    except:
        KeyboardInterrupt
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()