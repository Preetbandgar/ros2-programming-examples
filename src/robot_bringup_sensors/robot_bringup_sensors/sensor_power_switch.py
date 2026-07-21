#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class SensorPowerSwitchNode(Node):
    def __init__(self):
        super().__init__('sensor_power_switch')
        self.srv = self.create_service(SetBool, '/toggle_sensor_power', self.sensor_power_switch_request)
        self.get_logger().info("Sensor Power Switch server is online")

    def sensor_power_switch_request(self, request, response):
        self.get_logger().info("Sensor power switch request received! Running checks...")
        
        if request.data:
            self.get_logger().info("Primary sensor systems are powered ON.")
            response.success = True
            response.message = "Primary sensor systems are powered ON."
        else:
            self.get_logger().info("Primary sensor systems are powered OFF.")
            response.success = True
            response.message = "Primary sensor systems are powered OFF."
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SensorPowerSwitchNode()
    try:
        rclpy.spin(node)
    except:
        KeyboardInterrupt
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()