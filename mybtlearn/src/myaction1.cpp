

#include <actions/myaction1.h>
#include <string>


BT::MyAction::MyAction(std::string name) : ActionNode::ActionNode(name)
{
	
    thread_ = std::thread(&MyAction::WaitForTick, this);

}

BT::MyAction::~MyAction(){}

void BT::MyAction::WaitForTick(){
	while (true)
    {
        // Waiting for the first tick to come
        DEBUG_STDOUT(get_name() << " WAIT FOR TICK");

        tick_engine.Wait();
        DEBUG_STDOUT(get_name() << " TICK RECEIVED");

        // Running state
        set_status(BT::RUNNING);
        // Perform action...
        //int i = 0;
        while (get_status() != BT::HALTED)
        {
            DEBUG_STDOUT(" Action " << get_name() << "running! Thread id:" << std::this_thread::get_id());
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
      
    }
}

void BT::MyAction::Halt()
{
    set_status(BT::HALTED);
    DEBUG_STDOUT("HALTED state set!");
}