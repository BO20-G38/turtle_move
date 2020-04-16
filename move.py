import random
import decimal
import os

BASE_CMD = "rostopic pub /cmd_vel geometry_msgs/Twist -- "


def get_coordinate():
    rnd_range = random.randrange(100, 500)
    coord = decimal.Decimal(rnd_range) / 100
    return float(coord)


def generate_coordinates():
    linear = []
    angular = []

    for i in range(3):
        linear.append(get_coordinate())
        angular.append(get_coordinate())

    return stringify(linear) + " " + stringify(angular)


def stringify(arr):
    return "'" + str(arr) + "'"


def move():
    os.system(BASE_CMD + generate_coordinates())


move()