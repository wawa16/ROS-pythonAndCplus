#include <behavior_tree.h>


int main(int argc, char **argv)
{
    ros::init(argc, argv, "BehaviorTree");
    try
    {
        int TickPeriod_milliseconds = 1000;

        BT::MyAction* action1 = new BT::MyAction("Action 1");
       
        BT::SequenceNode* sequence1 = new BT::SequenceNode("seq1");



        sequence1->AddChild(action1);
        

        Execute(sequence1, TickPeriod_milliseconds);  // from BehaviorTree.cpp
    }
    catch (BT::BehaviorTreeException& Exception)
    {
        std::cout << Exception.what() << std::endl;
    }

    return 0;
}

