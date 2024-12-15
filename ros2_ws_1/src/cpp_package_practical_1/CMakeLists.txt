cmake_minimum_required(VERSION 3.8)
project(cpp_package_practical_1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED) # < --- Added
find_package(example_interfaces REQUIRED) # < --- Added

add_executable(node_cpp src/node_cpp.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  node_cpp
  "rclcpp"
)

add_executable(topic_cpp_publisher src/topic_cpp_publisher.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  topic_cpp_publisher 
  "rclcpp"
  "example_interfaces"
)

add_executable(topic_cpp_subscriber src/topic_cpp_subscriber.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  topic_cpp_subscriber
  "rclcpp"
  "example_interfaces"
)


add_executable(service_cpp_server src/service_cpp_server.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  service_cpp_server
  "rclcpp"
  "example_interfaces"
)

add_executable(service_cpp_client src/service_cpp_client.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  service_cpp_client
  "rclcpp"
  "example_interfaces"
)

add_executable(parameter_cpp src/parameters_cpp.cpp) # < --- Added
ament_target_dependencies( # < --- Added
  parameter_cpp
  "rclcpp"
  "example_interfaces"
)


target_include_directories(node_cpp PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include/${PROJECT_NAME}>)
target_compile_features(node_cpp PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17

install(TARGETS node_cpp topic_cpp_publisher topic_cpp_subscriber service_cpp_server service_cpp_client parameter_cpp # < --- Added
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
