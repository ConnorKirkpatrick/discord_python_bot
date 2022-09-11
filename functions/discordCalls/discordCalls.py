import asyncio

from functions import fileOperations
from functions.monitors import monitorTimer


async def setChannel(message):
    messageDetails = str(message.content[15:]).split("->")
    try:
        if int(messageDetails[1]) > 5:
            await message.reply("Monitor out of range, max is 5")
        else:
            await message.reply(
                "setting channel to: '" + messageDetails[0] + "' on monitor: " + messageDetails[1])
            fileOperations.setChannel(messageDetails[0], messageDetails[1], message.guild)
    except Exception as e:
        print(e)
        await message.reply("Monitor is not a valid number")


async def setServer(message):
    messageDetails = str(message.content[14:]).split("->")
    try:
        if int(messageDetails[1]) > 5:
            await message.reply("Monitor out of range, max is 5")
        else:
            await message.reply(
                "setting server to: '" + messageDetails[0] + "' on monitor: " + messageDetails[1])
            fileOperations.setServer(messageDetails[0], messageDetails[1], message.guild)
    except Exception as e:
        print(e)
        if(int(messageDetails[1]) < 1 or int(messageDetails[1]) > 5):
            await message.reply("Monitor is not a valid number")
        else:
            fileOperations.setupFile(message.guild)



async def startMonitor(message, client, object):
    try:
        monitor = int(str(message.content[17:]).strip())
    except Exception as e:
        print(e)
        await message.reply("No valid monitor specified")
        return 0
    if monitor > 5:
        await message.reply("Monitor out of range")
    elif str(fileOperations.getFlag(message.guild, monitor)) == '1\n':
        await message.reply("Monitor already running")
        return 0
    else:
        await message.reply("Starting up monitor: " + str(monitor))
        await asyncio.sleep(2.5)
        fileOperations.setFlag(1, monitor, message.guild)
        try:
            asyncio.create_task(monitorTimer.monitorTimer(client, message.guild, message, monitor, object))
            return 1
        except Exception as e:
            print(e)
            message.reply("Monitor failed to start: ", e)
            return 0


async def stopMonitor(message):
    try:
        monitor = int(str(message.content[17:]).strip())
    except Exception as e:
        print(e)
        await message.reply("No valid monitor specified")
        return 0
    if monitor > 5:
        await message.reply("Monitor out of range")
    elif str(fileOperations.getFlag(message.guild, monitor)) == '0\n':
        await message.reply("Monitor not running")
        return 0
    else:
        await message.reply("stopping.....")
        fileOperations.setFlag(0, monitor, message.guild)
        return -1
