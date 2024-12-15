import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self,a,b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self,future=self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client_async = MinimalClientAsync()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    response = minimal_client_async.send_request(a,b)
    
    minimal_client_async.get_logger().info('Result of add_two_ints: %d + %d = %d' % (a,b,response.sum))

    minimal_client_async.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()