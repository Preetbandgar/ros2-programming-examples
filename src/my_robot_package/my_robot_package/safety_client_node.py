import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import CheckSafety

class SafetyClient(Node):
    def __init__(self):
        super().__init__('safety_client_node')
        self.client = self.create_client(CheckSafety, 'front_lidar')

    def call_service(self, sensor_to_check):
        while not self.client.wait_for_service(1.0):
            self.get_logger().info('Waiting for service server to become available...')
        request = CheckSafety.Request()
        request.sensor_name = sensor_to_check
        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = SafetyClient()
    node.call_service('Front_Lidar')
    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
                node.get_logger().info(f"Service Response -> Success: {response.is_safe}, Message: {response.status_message}")
            except Exception as e:
                node.get_logger().info(f"Service Response failed: {e}")
            break
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()