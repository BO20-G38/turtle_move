import subprocess
import time

MOVE_DUR = 1

print("running move.py")

script = ['python', 'move.py', '0']
subprocess = subprocess.Popen(script)

time.sleep(MOVE_DUR)
subprocess.terminate()

print("Done running move.py")
