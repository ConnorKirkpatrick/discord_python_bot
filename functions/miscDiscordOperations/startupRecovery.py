import asyncio
import os

from functions.monitors import monitorTimer


async def startupRecovery(client, object):
    runningMonitors = 0
    files = os.listdir("./guildSettings")
    for file in files:
        f = open("guildSettings/" + file, "r")
        data = f.readlines()
        f.close()
        tick = 1
        for monitors in data:
            monitors = monitors.split(",")
            flag = monitors[2].split(":")[1]
            if flag == "1\n":
                print("STARTING: " + file[:-4] + " MONITOR: " + str(tick))
                asyncio.create_task(monitorTimer.monitorTimer(client, file[:-4], None, tick, object))
                runningMonitors += 1
            tick += 1
    return runningMonitors
