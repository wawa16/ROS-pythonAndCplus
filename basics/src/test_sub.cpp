#include <ros/ros.h>
#include <std_msgs/Int32.h>


void subCallback(const std_msgs::Int32::ConstPtr &msg){
    if((msg->data)%2 == 0){
       ROS_INFO("EVEN: %d",msg->data);
    } else {
       ROS_INFO("ODD: %d",msg->data);
    }
}

int main(int argc, char **argv){
    
    ros::init(argc, argv, "test_sub");
    ros::NodeHandle nh_;
    ros::Subscriber sub = nh_.subscribe("/random_msgs", 1000, subCallback);
    ros::spin();
}

