#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class NumberPublisherNode : public rclcpp::Node
{
public:
    NumberPublisherNode() : Node("number_publisher")
    {
        RCLCPP_INFO(this->get_logger(), "Hello from %s", this->get_name());

        this->declare_parameter("number_to_publish", 2);
        this->declare_parameter("publish_frequency", 1.0);

        number_ = this->get_parameter("number_to_publish").as_int();
        double publish_frequency = this->get_parameter("publish_frequency").as_double();

        publisher = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds((int)(1000.0 / publish_frequency)),
                                         std::bind(&NumberPublisherNode::publish_number, this));
        RCLCPP_INFO(this->get_logger(), "Number publisher has been started");
    }

private:
    void publish_number()
    {
        auto message = example_interfaces::msg::Int64();
        message.data = number_;
        publisher->publish(message);
    }
    int number_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}