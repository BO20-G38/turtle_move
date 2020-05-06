import os
import sys

direction = int(sys.argv[1])
BASE_CMD = "rostopic pub /cmd_vel geometry_msgs/Twist -- "


def stop():
    linear = [0, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)


def left():
    linear = [1, 0, 0]
    angular = [0, 0, -5]
    return stringify(linear) + " " + stringify(angular)


def right():
    linear = [1, 0, 0]
    angular = [0, 0, 5]
    return stringify(linear) + " " + stringify(angular)


def forward():
    linear = [2, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)


def backward():
    linear = [-2, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)


def stringify(arr):
    return "'" + str(arr) + "'"


def move(movement_type):
    switch = {
        0: stop(),
        1: right(),
        2: left(),
        3: forward(),
        4: backward()
    }

    coordinate = switch.get(movement_type)
    os.system(BASE_CMD + coordinate)


move(direction)
