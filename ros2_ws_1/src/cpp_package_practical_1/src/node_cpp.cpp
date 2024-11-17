#include <cstdio>
#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node
{
public:
  MyNode() : Node("my_node")
  {
    RCLCPP_INFO(this->get_logger(), "Hi from cpp_package_practical_1 package");
  }
};

int main(int argc, char **argv)
{
  (void)argc;
  (void)argv;

  rclcpp::init(argc, argv);
  auto node = std::make_shared<MyNode>();

  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;
}
