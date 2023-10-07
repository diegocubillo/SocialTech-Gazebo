# Introducción
Este paquete contiene los ficheros necesarios para sinumar las tres pruebas de la final del SocialTech-Challenge.
Los tres ficheros launch que contiene el paquete sirven para lanzar cada una de las pruebas.
- **prueba1.launch** --> Aranca gazebo con el el escenario que se utilizará en la final de la competición.
- **prueba2.launch** --> Aranca gazebo con el el escenario que se utilizará en la final de la competición y coloca 3 obstaculos de forma aleatoria de entre las 10 posibles ubicaciones.
- **prueba3.launch** --> Aranca gazebo con el el escenario que se utilizará en la final de la competición y hace que un obstaculo recorra el escenario siguiendo una ruta fija.

# Ejecutar escenario de la prueba 1

Para arrancar el entrono que se utilizará en la prueba 1 ejecuta el siguiente comando:

    roslaunch SocialTech-Gazebo prueba1.launch 

Una vez arrancado en otra terminal se puede ejecutar el nodo de teleoperación para comprobar que todo funciona bien. Este nodo permite mover el AGV por el escenario utilizando el teclado.

    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

# Ejecutar escenario de la prueba 1

Para arrancar el entrono que se utilizará en la prueba 1 ejecuta el siguiente comando:

    roslaunch SocialTech-Gazebo prueba2.launch 

Una vez arrancado en otra terminal se puede ejecutar el nodo de teleoperación para comprobar que todo funciona bien. Este nodo permite mover el AGV por el escenario utilizando el teclado.

    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Las 10 coordenadas de los posibles obstaculos se encuentran en el fichero ***config/puntosObstaculos.csv***. Tomando como origen de coordenadas la esquina inferior izquierda las coordenadas de los obstaculos son las siguientes:

| Punto | X | Y |
| ---- | ---- | ---- |
| 1 | 2.00 | 5.50 |
| 2 | 3.50 | 4.50 |
| 3 | 3.50 | 6.50 |
| 4 | 6.75 | 5.50 |
| 5 | 6.75 | 1.50 |
| 6 | 5.00 | 1.50 |
| 7 | 5.00 | 2.50 |
| 8 | 2.50 | 3.75 |
| 9 | 2.50 | 0.25 |
| 10 | 0.50 | 4.50 |

Como se pueden ver en la siguiente imagen.

![alt text](img/obstaculos.png)

En la prueba de obstaculos desconocidos se eligirán aleatoriamente 3 de las 10 posibles ubicaciones. Siendo un posible escenario el de la siguiente imagen.

![alt text](img/posibleEscenario2.png)

# Ejecutar escenario de la prueba 3

Para arrancar el entrono que se utilizará en la prueba 1 ejecuta el siguiente comando:

    roslaunch SocialTech-Gazebo prueba3.launch 

Una vez arrancado en otra terminal se puede ejecutar el nodo de teleoperación para comprobar que todo funciona bien. Este nodo permite mover el AGV por el escenario utilizando el teclado.

    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Las coordenadas de la ruta que seguirá el objeto móvil se encuentran en el fichero ***config/puntos.csv***. T

Siendo la ruta la que se puede ver en la siguiente imagen.

![alt text](img/rutamovil.gif)