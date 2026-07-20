#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# 1. Import the specific LaserScan message layout
from sensor_msgs.msg import LaserScan

class FakeLidarPublisher(Node):
    def __init__(self):
        super().__init__('fake_lidar_publisher')
        
        # 2. Setup the publisher targeting the standard '/scan' topic
        self.scan_pub = self.create_publisher(LaserScan, 'scan', 10)
        
        # 3. Create a timer running at 5 Hz (5 times per second)
        self.timer = self.create_timer(0.2, self.timer_callback)
        self.get_logger().info("Fake LiDAR Simulator has started!")

    def timer_callback(self):
        # 4. Create an empty LaserScan message container
        msg = LaserScan()
        
        # 5. Fill out the Passport Metadata (Header)
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'
        
        # 6. Configure the LiDAR properties (Angles in radians)
        msg.angle_min = -1.57    # -90 degrees (Right side view)
        msg.angle_max = 1.57     # +90 degrees (Left side view)
        msg.angle_increment = 0.785 # 45 degrees step between beams
        
        # 7. Set distance thresholds (Meters)
        msg.range_min = 0.1
        msg.range_max = 10.0
        
        # 8. Create the distance data array list (5 fake laser beam distance readings)
        # Beams point at: [-90°, -45°, 0° (Straight Ahead), 45°, 90°]
        msg.ranges = [3.5, 2.8, 0.8, 4.1, 5.0]
        
        # 9. Send the fully populated sensor data over the network
        self.scan_pub.publish(msg)
        self.get_logger().info("Published 5 fake LiDAR sensor points.")

def main(args=None):
    rclpy.init(args=args)
    node = FakeLidarPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()