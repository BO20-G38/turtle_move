import subprocess

BASE_CMD = "rostopic pub /cmd_vel geometry_msgs/Twist -- "


def stop():
    linear = [0, 0, 0]
    angular = [0, 0, 0]
    return concat_dir(linear, angular)


def left():
    linear = [1, 0, 0]
    angular = [0, 0, -2]
    return concat_dir(linear, angular)


def right():
    linear = [1, 0, 0]
    angular = [0, 0, 2]
    return concat_dir(linear, angular)


def forward():
    linear = [1, 0, 0]
    angular = [0, 0, 0]
    return concat_dir(linear, angular)


def backward():
    linear = [-1, 0, 0]
    angular = [0, 0, 0]
    return concat_dir(linear, angular)


def stringify(arr):
    return "'" + str(arr) + "'"


def concat_dir(linear, angular):
    return stringify(linear) + " " + stringify(angular)


def move(prediction_index):
    switch = {
        "0": forward,
        "1": right,
        "2": left,
        "3": backward,
        "4": stop,
        "5": stop
    }

    coordinate = switch.get(prediction_index)
    command = BASE_CMD + coordinate()
    process = subprocess.Popen(command, shell=True)
    process.terminate()


class Move:
    def __init__(self, prediction):
        self.prediction = prediction

    def start(self):
        move(self.prediction)
