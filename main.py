import asyncio
import os

import discord

from functions import fileOperations
from functions.miscDiscordOperations import startupRecovery, fileDump
from functions.discordCalls import discordCalls


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        asyncio.create_task(startupRecovery.startupRecovery(client))

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
                await discordCalls.setChannel(message)

            elif message.content.__contains__("kirk-setServer"):
                await discordCalls.setServer(message)

            elif message.content.__contains__("kirk-startMonitor"):
                await discordCalls.startMonitor(message,client)

            elif message.content.__contains__("kirk-stopMonitor"):
                await discordCalls.stopMonitor(message)

            elif message.content.__contains__("kirk-status"):
                await message.reply(fileOperations.status(message.guild))

            elif message.content.__contains__("kirk-fileDump"):
                await fileDump.fileDump()


client = MyClient()
client.run(os.environ["BOT-TOKEN"])
