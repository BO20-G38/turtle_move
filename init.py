import subprocess
import time
import sys
import os

initial_dir = sys.argv[1]
BASE_CMD = "rostopic pub /cmd_vel geometry_msgs/Twist -- "



def stop():
    linear = [0, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)




def left():
    linear = [1, 0, 0]
    angular = [0, 0, -2]
    return stringify(linear) + " " + stringify(angular)



def right():
    linear = [1, 0, 0]
    angular = [0, 0, 2]
    return stringify(linear) + " " + stringify(angular)



def forward():
    linear = [1, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)



def backward():
    linear = [-1, 0, 0]
    angular = [0, 0, 0]
    return stringify(linear) + " " + stringify(angular)



def stringify(arr):
    return "'" + str(arr) + "'"



def move(movement_type):
    switch = {
        "0": forward(),
        "1": right(),
        "2": left(),
        "3": backward(),
        "4": stop(),
        "5": stop()
    }


coordinate = switch.get(movement_type)
command = BASE_CMD + coordinate
print(command)
process = subprocess.Popen(command, shell=True)
time.sleep(1)
process.terminate()


def start():
    move(initial_dir)


start()
sys.stdout.write("1")
