#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RobotStatus

class RobotStatePublisher(Node):
    def __init__(self):
        super().__init__('robot_state_publisher')
        self.publisher_ = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.declare_parameter('temperature_threshold', 50.0)
        self.battery = 100
        self.temperature = 25.0

    def timer_callback(self):
        msg = RobotStatus()

        self.battery -= 1
        self.temperature += 2.5

        msg.battery_level = self.battery
        msg.motor_temperature = self.temperature

        current_threshold = self.get_parameter('temperature_threshold').value

    # Quick Evaluation Rule
        if msg.motor_temperature > current_threshold:
            msg.operational_status = "WARNING: OVERHEATING"
        else:
            msg.operational_status = "OPERATIONAL"

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published Status -> Batt: {msg.battery_level}%, Temp: {msg.motor_temperature}°C, State: {msg.operational_status} (Threshold: {current_threshold}°C)")

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()