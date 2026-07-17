#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import String

class ImuGuard(Node):
    def __init__(self):
        super().__init__('Imu_guard_node')

        self.imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)

        self.alert_pub =  self.create_publisher(String, '/fleet_alerts', 10)
        self.max_linear_speed = 3.0
        self.get_logger().info('Imu tilt guard has been started....')

    def imu_callback(self, msg):
        x_acceleration = msg.linear_acceleration.x

        self.get_logger().info(f"Current linear velocity is : {x_acceleration: .2f} m/s^2")

        if abs(x_acceleration) > self.max_linear_speed:
            self.get_logger().warn(f"[ImuTiltGuardNode]: Tilt warning! Acceleration X: {x_acceleration:.2f} m/s^2")

            alert_msg = String()
            alert_msg.data = f"CRITICAL: Robot moving too fast! Speed: {x_acceleration:.2f} m/s^2"
            self.alert_pub.publish(alert_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ImuGuard()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()