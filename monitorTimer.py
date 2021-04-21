import fileOperations
import monitorLoop
import time
import threading


async def monitorTimer(client, guild,message):
        if fileOperations.getFlag(str(guild)) == "1":
            await monitorLoop.getDetails(client, str(guild),message)
        else:
            threading.current_thread().join()
