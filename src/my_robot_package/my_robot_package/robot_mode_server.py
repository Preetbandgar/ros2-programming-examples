#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetRobotMode

class RobotModeServer(Node):
    def __init__(self):
        super().__init__('robot_mode_server')
        self.srv = self.create_service(SetRobotMode, 'set_robot_mode', self.set_mode_callback)
        self.get_logger().info("Robot Mode Service Server has been started.")

    def set_mode_callback(self, request, response):
        requested_mode = request.targeted_mode
        self.get_logger().info(f"Received request to change mode to: {requested_mode}")

        valid_modes = ["MAPPING", "NAVIGATION", "DOCKING"]

        if requested_mode.upper() in valid_modes:
            response.success = True
            response.message = f"Robot mode successfully changed to {requested_mode}."
        else:
            response.success = False
            response.message = f"Failed: '{requested_mode}' is not a valid operating mode."

        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = RobotModeServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()