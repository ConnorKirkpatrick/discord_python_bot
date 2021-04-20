import fileOperations
import monitorLoop
import time
import threading


async def monitorTimer(client):
    while True:
        if fileOperations.getFlag() == "1":
            await monitorLoop.getDetails(client)
        else:
            break
        time.sleep(45)
