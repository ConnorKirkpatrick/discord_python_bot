import fileOperations
import monitorLoop
import time
import threading
import asyncio


async def monitorTimer(client, guild,message):
    if fileOperations.getFlag(str(guild)) == "1":
        status = await monitorLoop.getDetails(client, str(guild),message)
        await asyncio.sleep(30)
        if status == 1:
            await monitorTimer(client, guild,message)