import rclpy
from rclpy.node import Node

class ParameterNode(Node):
    def __init__(self):
        super().__init__('Parameter_node')
        self.declare_parameter('param1', 'default value Indramal')
        self.declare_parameter('param2', 'default value Wansekara')
        self.get_logger().info('Hi from Parameter_node.')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        param1 = self.get_parameter('param1').get_parameter_value().string_value
        param2 = self.get_parameter('param2').get_parameter_value().string_value
        self.get_logger().info('param1: %s' % param1)
        self.get_logger().info('param2: %s' % param2)

        my_new_param = rclpy.parameter.Parameter('param1',rclpy.Parameter.Type.STRING, 'Thilanka')
        self.set_parameters([my_new_param])

def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    rclpy.spin(node)
    
if __name__ == '__main__':
    main()