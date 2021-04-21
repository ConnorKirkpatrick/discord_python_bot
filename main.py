import asyncio
import os

import discord

import fileOperations
import monitorTimer

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        # await monitorLoop.getDetails(client)

    async def on_message(self, message):
        if message.author == client.user:
            return
        else:
            if message.content.__contains__("kirk-help"):
                await message.reply("Use Commands wit the prefix 'kirk-':\n"
                                    "setChannel: set the channel the monitor will post in\n"
                                    "setServer: give the full name of the server you wish to monitor\n"
                                    "startMonitor: Start the monitor\n"
                                    "stopMonitor: stop the monitor\n"
                                    "status: displays the current set values for server, channel and flag\n"
                                    "help: Display this message")
            elif message.content.__contains__("kirk-setChannel"):
                await message.reply("setting channel to: "+message.content[15:])
                fileOperations.setChannel(message.content[15:], message.guild)
            elif message.content.__contains__("kirk-setServer"):
                await message.reply("setting server to: "+message.content[14:])
                fileOperations.setServer(message.content[14:], message.guild)
            elif message.content.__contains__("kirk-startMonitor"):
                await message.reply("Setting up.......")
                # add a check to see if the monitor is running first
                fileOperations.setFlag(1, message.guild)
                await asyncio.sleep(2.5)
                try:
                    asyncio.run(await monitorTimer.monitorTimer(client, message.guild, message))
                except Exception as e:
                    print(e)
            elif message.content.__contains__("kirk-stopMonitor"):
                await message.reply("stopping.....")
                fileOperations.setFlag(0, message.guild)
            elif message.content.__contains__("kirk-status"):
                await message.reply("Server: " + fileOperations.getServer(message.guild) + "\nChannel: " +
                                    fileOperations.getChannel(message.guild) + "\nMonitor (1 is yes): " +
                                    fileOperations.getFlag(message.guild))


client = MyClient()
client.run(os.environ["BOT-TOKEN"])

def startupRecovery():
    print("TESTING")
    # check all files inside of guildSettings
    # if file flag is true, start a monitor for it