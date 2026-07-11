import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MotorSafetyGuard(Node):
    def __init__(self):
        super().__init__('motor_safety_guard_node')
        self.subscription_ = self.create_subscription(Int32, 'motor_temperature', self.safety_callback, 10)
        self.get_logger().info("Motor Safety Guard Node has been started")
    
    def safety_callback(self, msg):
        if msg.data <= 70:
            self.get_logger().info(f"[INFO] [Motor Health]: Operational. Temperature: {msg.data}°C")
        else:
            msg.data >=70
            self.get_logger().info(f"[WARN] [EMERGENCY STOP]: Motor Overheating! Core Temp: {msg.data}°C. Shutting down systems!")

def main(args=None):
    rclpy.init(args=args)
    node = MotorSafetyGuard()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()