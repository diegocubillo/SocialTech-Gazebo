#!/usr/bin/env python3
import rospy 
import rospkg 
import csv
import tf
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

def main():
    angulo=0.0
    incrementoAngulo=0.012566370614359172953850573533118
    rospy.init_node('set_pose')
    rospack = rospkg.RosPack()
    rate = rospy.Rate(15)
    rospy.sleep(5)
    ruta=rospack.get_path('SocialTech-Gazebo')
    state_msg = ModelState()
    state_msg.model_name = 'obstaculo_movil'
    state_msg.pose.position.x = 0
    state_msg.pose.position.y = 0
    state_msg.pose.position.z = 0.0
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 0
    try:
        rospy.wait_for_service('/gazebo/set_model_state')
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )
        while True:
            with open(ruta+'/config/puntos.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    angulo=angulo+incrementoAngulo
                    campos = row[0].split(',')
                    state_msg.pose.position.x = float(campos[0])
                    state_msg.pose.position.y = float(campos[1])
                    quaternion = tf.transformations.quaternion_from_euler(0, 0, angulo)
                    state_msg.pose.orientation.x = quaternion[0]
                    state_msg.pose.orientation.y = quaternion[1]
                    state_msg.pose.orientation.z = quaternion[2]
                    state_msg.pose.orientation.w = quaternion[3]
                    resp = set_state( state_msg )
                    rate.sleep()

    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass