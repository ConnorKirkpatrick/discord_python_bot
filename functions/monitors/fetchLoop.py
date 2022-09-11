import asyncio
import serverList

async def fetchLoop(object):
    while True:
        if object.runningMonitors > 0:
            object.servers = serverList.getServerList()
        await asyncio.sleep(60)
