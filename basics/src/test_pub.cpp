#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include <stdlib.h>


int main(int argc, char **argv){
    ros::init(argc, argv, "test_pub");
    ros::NodeHandle nh_;
    ros::Publisher pub = nh_.advertise<std_msgs::Int32>("random_msgs",10);
    ros::Rate rate(2);
    while(ros::ok()){
        std_msgs::Int32 msgs;
        msgs.data = rand() % 10;
        pub.publish(msgs);
        rate.sleep();
        ROS_INFO("%d", msgs.data);
    }
}