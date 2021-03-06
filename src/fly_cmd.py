#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty as EmptyMsg
from geometry_msgs.msg import Twist
import time
from std_msgs.msg import Int8

pre_time = 0

pub_takeoff = rospy.Publisher('/ardrone/takeoff', EmptyMsg, queue_size=1)
pub_land = rospy.Publisher('/ardrone/land', EmptyMsg, queue_size=1)
pub_vel_cmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

command = 0

def pub_cmd(data):
    global pre_time, command
    global pub_vel_cmd, pub_takeoff, pub_land
    pre_time = time.time() * 1000  #in milisecond
    command = data.data

def cmd():
    global pre_time, command
    global pub_vel_cmd
    rospy.init_node('cmd', anonymous=True)
    rospy.Subscriber("keyboard_cmd", Int8, callback=pub_cmd)
    rate = rospy.Rate(100) # 100hz
    while not rospy.is_shutdown():
        now_time = time.time() * 1000
        if (now_time - pre_time) > 100:
            vel_msg = Twist()
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0  
            vel_msg.angular.z = 0
            pub_vel_cmd.publish(vel_msg)
        else:
            vel_msg = Twist()
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0  
            vel_msg.angular.z = 0
            velocity = 1
            if command == 116:
                pub_takeoff.publish()
            elif command == 108:
                pub_land.publish()
            elif command == 119:
                vel_msg.linear.x = velocity
                pub_vel_cmd.publish(vel_msg)        
            elif command == 115:
                vel_msg.linear.x = -velocity
                pub_vel_cmd.publish(vel_msg)        
            elif command == 97:
                vel_msg.linear.y = velocity
                pub_vel_cmd.publish(vel_msg)
            elif command == 100:
                vel_msg.linear.y = -velocity
                pub_vel_cmd.publish(vel_msg)
            elif command == 113:
                vel_msg.angular.z = velocity
                pub_vel_cmd.publish(vel_msg)
            elif command == 101:
                vel_msg.angular.z = -velocity
                pub_vel_cmd.publish(vel_msg)
            elif command == 32:
                vel_msg.linear.z = velocity
                pub_vel_cmd.publish(vel_msg)
            elif command == 122:
                vel_msg.linear.z = -velocity
                pub_vel_cmd.publish(vel_msg)

            # print("QQQ\n")

        rate.sleep()

if __name__ == '__main__':
    try:
        cmd()
    except rospy.ROSInterruptException:
        pass