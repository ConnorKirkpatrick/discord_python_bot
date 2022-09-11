import asyncio
import os

import discord

from functions import fileOperations
from functions.monitors import monitorTimer
from functions.discordCalls import discordCalls
from functions.miscDiscordOperations import startupRecovery

# Post reduction: Aim to reduce number of net requests made
# currently a new request is made for every single monitor
# Aim is to make 1 request per cycle time and save the request for all requesters to use

runningMonitors = 0


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        runningMonitors += await asyncio.create_task(startupRecovery.startupRecovery(client))
        # await monitorLoop.getDetails(client)

    async def on_message(self, message):
        if message.author == client.user:
            return
        else:
            if message.content.__contains__("kirk-help"):
                await message.reply("Use Commands wit the prefix 'kirk-':\n"
                                    "setChannel [channel]->[monitor]: set the channel to post the status into and the "
                                    "monitor responsible\n"
                                    "setServer [server]->[monitor]: give the full name of the server of the server to "
                                    "monitor and the monitor responsible\n"
                                    "startMonitor [monitor]: Start monitor\n"
                                    "stopMonitor [monitor]: stop monitor\n"
                                    "status: displays the current status of your monitors\n"
                                    "help: Display this message")

            elif message.content.__contains__("kirk-setChannel"):
                await discordCalls.setChannel(message)

            elif message.content.__contains__("kirk-setServer"):
                await discordCalls.setServer(message)

            elif message.content.__contains__("kirk-startMonitor"):
                runningMonitors += await discordCalls.startMonitor(message, client)

            elif message.content.__contains__("kirk-stopMonitor"):
                runningMonitors += await discordCalls.stopMonitor(message)

            elif message.content.__contains__("kirk-status"):
                await message.reply(fileOperations.status(message.guild))

            elif message.content.__contains__("kirk-fileDump"):
                await fileDump.fileDump()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["BOT-TOKEN"])
