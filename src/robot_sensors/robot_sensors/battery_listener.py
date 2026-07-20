import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatteryListener(Node):
    def __init__(self):
        super().__init__('battery_listener_node')
        self.subscriber_ = self.create_subscription(Int32, 'battery_level', self.battery_callback, 10)
        self.get_logger().info('Battery Listener Node has been started')

    def battery_callback(self, msg):
        self.get_logger().info(f'Battery: {msg.data}%')


def main(args=None):
    rclpy.init(args=args)
    node = BatteryListener()
    rclpy.spin(node)
    node.destroy._node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()