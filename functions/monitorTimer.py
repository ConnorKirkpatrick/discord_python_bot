from functions import monitorLoop, fileOperations
import asyncio


async def monitorTimer(client, guild, message, monitor):
    while True:
        if fileOperations.getFlag(str(guild), monitor) == "1\n":
            status = await monitorLoop.getDetails(client, str(guild), message, monitor)
            await asyncio.sleep(30)
            if status != 1:
                break
        else:
            break
