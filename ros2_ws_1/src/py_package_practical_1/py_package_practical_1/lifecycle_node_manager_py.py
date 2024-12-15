import rclpy
import time
from rclpy.node import Node
from lifecycle_msgs.srv import ChangeState
from lifecycle_msgs.msg import Transition

class LifecycleNodeManager(Node):
    def __init__(self):
        super().__init__('lifecycle_node_manager')
        self.declare_parameter('managed_node_name', rclpy.Parameter.Type.STRING)
        node_name = self.get_parameter('managed_node_name').value
        service_change_state_name = "/" + node_name + "/change_state"
        self.client = self.create_client(ChangeState, service_change_state_name)

    def change_state(self, transition: Transition):
        self.client.wait_for_service()
        req = ChangeState.Request()
        req.transition = transition
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)

    def initialization_sequence(self):
        self.get_logger().info('Trying to switch to configured state')
        transition = Transition()
        transition.id = Transition.TRANSITION_CONFIGURE
        transition.label = "configure"
        self.change_state(transition)
        self.get_logger().info('Confiurring Ok, now inactive')

        time.sleep(3)

        self.get_logger().info('Trying to switch to activated state')
        transition = Transition()
        transition.id = Transition.TRANSITION_ACTIVATE
        transition.label = "activate"
        self.change_state(transition)
        self.get_logger().info('Activated Ok, now active')

        # time.sleep(3)

        # self.get_logger().info('Trying to switch to deactivated state')
        # transition = Transition()
        # transition.id = Transition.TRANSITION_DEACTIVATE
        # transition.label = "deactivate"
        # self.change_state(transition)
        # self.get_logger().info('Deactivated Ok, now inactive')

def main(args=None):
    rclpy.init(args=args)
    node = LifecycleNodeManager()
    node.initialization_sequence()
    rclpy.shutdown()

if __name__ == '__main__':
    main()