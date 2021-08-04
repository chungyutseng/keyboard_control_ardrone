#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty as EmptyMsg
from geometry_msgs.msg import Twist
import time
# import keyboard

def sender_cmd():
    pub_take_off = rospy.Publisher('/ardrone/takeoff', EmptyMsg, queue_size=1)
    pub_land = rospy.Publisher('/ardrone/land', EmptyMsg, queue_size=1)
    pub_vel_cmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # if keyboard.read_key() == "p":
        # if keyboard.is_pressed('g'):
            # print("1")
        # else:
        #     print("0")
        # vel_msg = Twist()
        # vel_msg.linear.x = 0
        # vel_msg.linear.y = 0
        # vel_msg.linear.z = 0
        # vel_msg.angular.x = 0
        # vel_msg.angular.y = 0  
        # vel_msg.angular.z = 0
        # input_key = 0

        ########################################
        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0  
        vel_msg.angular.z = 0
        input_key = input()
        if input_key == 1:
            pub_take_off.publish()
        elif input_key == 0:
            pub_land.publish()
        elif input_key == 8:
            vel_msg.linear.x = 0.2
            pub_vel_cmd.publish(vel_msg)
            time.sleep(6)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0  
        vel_msg.angular.z = 0
        pub_vel_cmd.publish(vel_msg)
        ########################################
        
        # a = raw_input()
        # print a

        # print(input_key)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('Keyboard_Control_Tello', anonymous=True)
    # pub_take_off = rospy.Publisher('/ardrone/takeoff', EmptyMsg, queue_size=1)
    # pub_land = rospy.Publisher('/ardrone/land', EmptyMsg, queue_size=1)
    # pub_vel_cmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sender_cmd()