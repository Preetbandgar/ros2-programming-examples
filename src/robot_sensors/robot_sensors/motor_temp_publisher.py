import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MotorTemperature(Node):
    def __init__(self):
        super().__init__('motor_temperature_node')
        self.publisher_ = self.create_publisher(Int32, 'motor_temperature', 10)
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info("Motor Temperature node has been started")
        self.internal_temp = 30 

    def timer_callback(self):
        msg = Int32()
        self.internal_temp += 4 
        msg.data = self.internal_temp
        self.publisher_.publish(msg)
        self.get_logger().info(f"Current Robot motor temperature is: {msg.data}°C")

def main(args=None):
    rclpy.init(args=args)
    node = MotorTemperature()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__  == '__main__':
    main()