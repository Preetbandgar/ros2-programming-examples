#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time
from rclpy.action import ActionServer
from my_robot_interfaces.action import MapsArea

class AreaNavigationServer(Node):
    def __init__(self):
        super().__init__('area_navigation_server_node')
        self._action_server = ActionServer(
            self, MapsArea, 'navigate_area', self.execute_callback
        )
        self.get_logger().info("Area Navigation Action Server is online!")
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Unpacking target distance...')
        
        target = goal_handle.request.target_distance

        feedback_msg = MapsArea.Feedback()
        feedback_msg.current_distance = 0.0

        while feedback_msg.current_distance < target:
            feedback_msg.current_distance += 1.0
            self.get_logger().info(f"Robot driving... Progress: {feedback_msg.current_distance}m")
        
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1.0)
        
        goal_handle.succeed()

        result = MapsArea.Result()
        result.reached = True
        return result

def main(args=None):
    rclpy.init(args=args)
    node = AreaNavigationServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()