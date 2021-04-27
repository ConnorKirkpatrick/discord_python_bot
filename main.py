import asyncio
import os

import discord

from functions import startupRecovery, monitorTimer, fileDump, fileOperations


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        asyncio.create_task(startupRecovery.startupRecovery(client))
        # await monitorLoop.getDetails(client)

    async def on_message(self, message):
        if message.author == client.user:
            return
        else:
            if message.content.__contains__("kirk-help"):
                await message.reply("Use Commands wit the prefix 'kirk-':\n"
                                    "setChannel [channel]->[monitor]: set the channel to post the status into and the "
                                    "monitor responsible\n "
                                    "setServer [server]->[monitor]: give the full name of the server of the server to "
                                    "monitor and the monitor responsible\n "
                                    "startMonitor [monitor]: Start monitor\n"
                                    "stopMonitor [monitor]: stop monitor\n"
                                    "status: displays the current status of your monitors\n"
                                    "help: Display this message")

            elif message.content.__contains__("kirk-setChannel"):
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

            elif message.content.__contains__("kirk-setServer"):
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
                    await message.reply("Monitor is not a valid number")

            elif message.content.__contains__("kirk-startMonitor"):
                try:
                    monitor = int(str(message.content[17:]).strip())
                except Exception as e:
                    print(e)
                    await message.reply("No valid monitor specified")
                    return
                if monitor > 5:
                    await message.reply("Monitor out of range")
                elif str(fileOperations.getFlag(message.guild, monitor)) == '1\n':
                    await message.reply("Monitor already running")
                    return
                else:
                    await message.reply("Starting up monitor: " + str(monitor))
                    await asyncio.sleep(2.5)
                    fileOperations.setFlag(1, monitor, message.guild)
                    try:
                        asyncio.create_task(monitorTimer.monitorTimer(client, message.guild, message, monitor))
                    except Exception as e:
                        print(e)
                        message.reply("Monitor failed to start: ", e)

            elif message.content.__contains__("kirk-stopMonitor"):
                try:
                    monitor = int(str(message.content[17:]).strip())
                except Exception as e:
                    print(e)
                    await message.reply("No valid monitor specified")
                    return
                if monitor > 5:
                    await message.reply("Monitor out of range")
                elif str(fileOperations.getFlag(message.guild, monitor)) == '0\n':
                    await message.reply("Monitor not running")
                    return
                else:
                    await message.reply("stopping.....")
                    fileOperations.setFlag(0, monitor, message.guild)

            elif message.content.__contains__("kirk-status"):
                await message.reply(fileOperations.status(message.guild))

            elif message.content.__contains__("kirk-fileDump"):
                await fileDump.fileDump()


client = MyClient()
client.run(os.environ["BOT-TOKEN"])
