import fileOperations
import monitorLoop
import time
import threading


async def monitorTimer(client):
    while True:
        if fileOperations.getFlag():
            await monitorLoop.getDetails(client)
        else:
            break
        time.sleep(45)
