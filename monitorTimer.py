import fileOperations
import monitorLoop
import time
import threading
import asyncio


async def monitorTimer(client, guild,message):
    if fileOperations.getFlag(str(guild)) == "1":
        await monitorLoop.getDetails(client, str(guild),message)
        await asyncio.sleep(10)
        await monitorTimer(client, guild,message)