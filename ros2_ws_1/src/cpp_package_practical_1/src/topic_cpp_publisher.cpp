#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node
{
public:
    RobotNewsStationNode() : Node("robot_news_station"), robot_name_("R202")
    {
        robot_news_publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&RobotNewsStationNode::publish_news, this));
        RCLCPP_INFO(this->get_logger(), "Robot news station has been started");
    }

private:
    void publish_news()
    {
        auto message = example_interfaces::msg::String();
        message.data = std::string("Hello ") + robot_name_;
        // RCLCPP_INFO(this->get_logger(), "Publishing news: '%s'", message.data.c_str());
        robot_news_publisher_->publish(message);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr robot_news_publisher_;
    std::string robot_name_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}