#!/usr/bin/env python3
import rospy 
import rospkg 
import roslib
import csv
import tf
from geometry_msgs.msg import *
import tf.transformations as tft
from geometry_msgs.msg import Pose, Point, Quaternion
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import *
import random

rospy.init_node('set_obstacle')
rospack = rospkg.RosPack()
ruta=rospack.get_path('SocialTech-Gazebo')

object_pose = Pose()
nombre = 'obstaculo_fijo'
object_pose.position.x = 1
object_pose.position.y = 5
object_pose.position.z = 0.0
object_pose.orientation.x = 0
object_pose.orientation.y = 0
object_pose.orientation.z = 0
object_pose.orientation.w = 0

nObjetos=3
maxObject=10
listaCoordenadas = []

rospy.wait_for_service('/gazebo/spawn_urdf_model')

with open(ruta+'/config/puntosObstaculos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        campos = row[0].split(',')
        listaCoordenadas.append([float(campos[0]),float(campos[1])])


listaCoordenadasObjetos = []
for num in range(nObjetos):
    aleatorio=random.randrange(maxObject-1)
    maxObject=maxObject-1
    punto=listaCoordenadas[aleatorio]
    listaCoordenadasObjetos.append(punto)
    listaCoordenadas.remove(punto)
    object_pose.position.x = float(punto[0])
    object_pose.position.y = float(punto[1])
    try:
        delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
        delete_model_prox(nombre+str(num))
        rospy.sleep(1)
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        file_xml = open(ruta+'/urdf/obstaculo_fijo.urdf')
        xml_string=file_xml.read()
        resp_urdf = spawn_urdf(nombre+str(num), xml_string, "/", object_pose, "world")
    except rospy.ServiceException as e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e)) 
#print(listaCoordenadasObjetos)




#delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
#delete_model_prox(nombre)
#rospy.sleep(1)

