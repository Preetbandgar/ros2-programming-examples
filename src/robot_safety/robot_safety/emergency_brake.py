#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class EmergencyBrakeNode(Node):
    def __init__(self):
        super().__init__('emergency_brake_node')
        self.vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('The Emergency Node has been started....')

    def timer_callback(self):
        msg = Twist()

        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.vel_publisher.publish(msg)

        self.get_logger().info(f"[EmergencyBrakeNode]: Sending safe brake command - \n Linear X= {msg.linear.x}, Linear Y= {msg.linear.x}, Linear Z= {msg.linear.y}, \n Angular X={msg.angular.x}, Angular Y={msg.angular.y}, Angular Z={msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyBrakeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()