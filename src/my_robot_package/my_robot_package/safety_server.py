import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import CheckSafety

class SafetyServer(Node):
    def __init__(self):
        super().__init__('safety_server_node')
        self.srv = self.create_service(CheckSafety, 'front_lidar', self.lidar_callback)
        self.get_logger().info("Robot safety server node has been started")

    def lidar_callback(self, request, response):
        requested_mode = request.sensor_name
        self.get_logger().info(f"Received request to lidar to: {requested_mode}")

        valid_sensors = ["FRONT_LIDAR"]

        if requested_mode.upper() in valid_sensors:
            response.is_safe = True
            response.status_message = f"Laser path is clear."

        else:
            response.is_safe = False
            response.status_message = f"Unknown sensor or sensor blocked!"

        return response

def main(args=None):
    rclpy.init(args=args)
    node = SafetyServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()