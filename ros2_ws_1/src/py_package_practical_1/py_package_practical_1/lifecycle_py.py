# Start with the lifecycle node - ros2 run py_package_practical_1 lifecycle_py  
# Lifecycle configure - ros2 lifecycle set /number_publisher_node configure
# Lifecycle shutdown - ros2 lifecycle set /number_publisher_node shutdown
# Lifecycle deactivate - ros2 lifecycle set /number_publisher_node deactivate
# Lifecycle activate - ros2 lifecycle set /number_publisher_node activate
# Lifecycle cleanup - ros2 lifecycle set /number_publisher_node cleanup
# Check the topic - ros2 topic echo /number
# Check posible states - ros2 lifecycle list /number_publisher_node 
# Get the state - ros2 lifecycle get /number_publisher_node

import rclpy
from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle.node import LifecycleState, TransitionCallbackReturn
from std_msgs.msg import Int64

class NumberPublisherNode(LifecycleNode):
    def __init__(self):
        super().__init__('number_publisher_node')
        self.get_logger().info('IN constructor')
        self.number = 1
        self.publish_frequency_ = 1.0
        self.number_publisher_ = None
        self.number_timer_ = None

    def on_configure(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_configure')
        self.number_publisher_ = self.create_lifecycle_publisher(Int64, 'number', 10)
        self.number_timer_ = self.create_timer(1.0/self.publish_frequency_, self.publish_number)
        self.number_timer_.cancel()
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_activate')
        self.number_timer_.reset()
        return super().on_activate(previous_state)

    def on_deactivate(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_deactivate')
        self.number_timer_.cancel()
        return super().on_deactivate(previous_state)

    def on_cleanup(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_cleanup')
        self.destroy_lifecycle_publisher(self.number_publisher_)
        self.destroy_timer(self.number_timer_)
        return TransitionCallbackReturn.SUCCESS  # Fixed from Result to Return

    def on_shutdown(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_shutdown')
        self.destroy_lifecycle_publisher(self.number_publisher_)
        self.destroy_timer(self.number_timer_)
        return TransitionCallbackReturn.SUCCESS  # Fixed from Result to Return

    def on_error(self, previous_state: LifecycleState):
        self.get_logger().info('IN on_error')
        self.destroy_lifecycle_publisher(self.number_publisher_)
        self.destroy_timer(self.number_timer_)
        return TransitionCallbackReturn.SUCCESS  # Fixed from Result to Return

    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.number_publisher_.publish(msg)
        self.number += 1

def main(args=None):
    rclpy.init(args=args)
    number_publisher_node = NumberPublisherNode()
    rclpy.spin(number_publisher_node)
    rclpy.shutdown()