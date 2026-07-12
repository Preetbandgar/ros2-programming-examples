#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuRobotNode(Node):
    def __init__(self):
        super().__init__('Imu_robot_node')
        self.Imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)
        self.get_logger().info('Robot Imu Node has been started....')

    def imu_callback(self, msg):

        self.angular_vel = msg.angular_velocity.z

        self.get_logger().info(f"Angular velocity of robot is: {self.angular_vel: .2f} m")

def main(args=None):
    rclpy.init(args=args)
    node = ImuRobotNode()
    try:
        rclpy.spin(node)
    except:
        KeyboardInterrupt
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
