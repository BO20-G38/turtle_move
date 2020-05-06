import subprocess
import time
import sys

MOVE_DUR = 3
initial_dir = sys.argv[1]

print("running move.py")


def run_script(direction):
    script = ['python', 'move.py', direction]
    process = subprocess.Popen(script)

    delay = direction != "0"
    clear(process, delay)


def clear(process, delay):
    if delay:
        time.sleep(MOVE_DUR)

    process.terminate()


def start():
    run_script(initial_dir)

    # stop movement after each direction passed
    if not initial_dir == "0":
        run_script("0")


start()
print("Done running move.py")
