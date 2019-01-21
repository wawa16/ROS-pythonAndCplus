

#ifndef ACTIONS_MYACTION1_H
#define ACTIONS_MYACTION1_H

#include <action_node.h>
#include <string>

namespace BT
{
	class MyAction : public ActionNode
	{
	public:
	
	   explicit MyAction(std::string Name);

	   ~MyAction();
       
       void WaitForTick();
       void Halt();

    private:
    	int time_;
    	bool boolean_value_;

	};
}

#endif