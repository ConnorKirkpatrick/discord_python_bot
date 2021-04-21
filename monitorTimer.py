import fileOperations
import monitorLoop
import time
import threading


async def monitorTimer(client, guild,message):
    while True:
        if fileOperations.getFlag(str(guild)) == "1":
            await monitorLoop.getDetails(client, str(guild),message)
        else:
            break
        time.sleep(7.5)
