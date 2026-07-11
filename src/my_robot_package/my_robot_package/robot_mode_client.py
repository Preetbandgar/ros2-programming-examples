#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetRobotMode

class RobotModeClient(Node):
    def __init__(self):
        super().__init__('robot_mode_client')
        self.client = self.create_client(SetRobotMode, 'set_robot_mode')

    def call_set_mode_service(self, mode_name):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service server to become available...')
        request = SetRobotMode.Request()
        request.targeted_mode = mode_name
        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = RobotModeClient()
    node.call_set_mode_service('navigation')
    while rclpy.ok():
        rclpy.spin_once(node)  
        if node.future.done():
            try:
                response = node.future.result()
                node.get_logger().info(f"Service Response -> Success: {response.success}, Message: {response.message}")
            except Exception as e:
                node.get_logger().error(f"Service call failed: {e}")
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()