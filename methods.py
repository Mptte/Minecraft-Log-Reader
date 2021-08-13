import time
import os

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def logger():
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
    loglines =follow(logfile)
    for line in loglines:
        if "[Render thread/INFO]: [CHAT]" or "[Client thread/INFO]: [CHAT]"  in line:
            print(line)
        else:
            chatLines = None

