#!/usr/bin/env python
import rospy
import time

from basics.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback
import actionlib

def do_timer(goal):
	start_time = time.time()
	update_count = 0

	## GOAL ABORT
	if goal.time_to_wait.to_sec() > 60:
		result = TimerResult()
		result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
		result.updates_sent = update_count
		server.set_aborted(result, "ABORTED BECAUSE TIME TOO LONG")
		return
 

	
	while (time.time() - start_time) < goal.time_to_wait.to_sec():
		
		## GOAL PREEMPT
		if server.is_preempt_requested():
			result = TimerResult()
			result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
			result.updates_sent = update_count
			server.set_preempted(result, "TIME PREEMPTED BY CLIENT")
			return

		## FEEDBACK
		Feedback = TimerFeedback()
		Feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
		Feedback.time_remaining = goal.time_to_wait - Feedback.time_elapsed
		server.publish_feedback(Feedback)

		update_count = update_count + 1
		
		rospy.sleep(1.0)

	## GOAL SUCCESS
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
	result.updates_sent = update_count
	server.set_succeeded(result, 'TIMER COMPLETED')


##    NODE INITIALIZATION
rospy.init_node('simple_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()
