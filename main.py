import asyncio
import os

import discord

from functions import fileOperations
from functions.monitors import monitorTimer
from functions.discordCalls import discordCalls
from functions.miscDiscordOperations import startupRecovery
from functions.miscDiscordOperations import fileDump
from functions.monitors import fetchLoop


# IntelligentEditing: We will try to allow all monitors to be present in one channel
# make request for last 5 messages, check the embed names for a match to the current monitor server
# if match is found, edit that message


class MyClient(discord.Client):
    async def on_ready(self):
        self.runningMonitors = 1    #set to 1 so we can perform an inital request to populate any monitors that need started
        self.servers = ""
        print('Logged on as {0}!'.format(self.user))
        asyncio.create_task(fetchLoop.fetchLoop(self))
        self.runningMonitors += await asyncio.create_task(startupRecovery.startupRecovery(client, self))


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
                self.runningMonitors += await discordCalls.startMonitor(message, client, self)

            elif message.content.__contains__("kirk-stopMonitor"):
                self.runningMonitors += await discordCalls.stopMonitor(message)

            elif message.content.__contains__("kirk-status"):
                await message.reply(fileOperations.status(client,message.guild))

            elif message.content.__contains__("kirk-fileDump"):
                await fileDump.fileDump()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["BOT-TOKEN"])

