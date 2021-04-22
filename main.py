import asyncio
import os

import discord

import fileOperations
import monitorTimer

##duplicating the .txt on the end of the files

async def startupRecovery():
    files = os.listdir("guildSettings")
    for file in files:
        f = open("guildSettings/"+file, "r")
        data = f.readlines()
        f.close()
        file = file[:-4]
        flag = data[0].split(",")[2].split(":")[1]
        if flag == '1':
            print("Starting: "+file)
            await monitorTimer.monitorTimer(client, file, None)

async def fileDump():
    files = os.listdir("guildSettings")
    for file in files:

        f = open("guildSettings/" + file, "r")
        data = f.readlines()
        f.close()
        lineData = []
        for line in data:
            if line.__contains__("\n"):
                line = line[:-1]
            lineData.append(line)
        fileData = [file, lineData]
        print(fileData)

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await startupRecovery()
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
                await message.reply("setting channel to: " + message.content[15:])
                fileOperations.setChannel(message.content[15:], message.guild)
            elif message.content.__contains__("kirk-setServer"):
                await message.reply("setting server to: " + message.content[14:])
                fileOperations.setServer(message.content[14:], message.guild)
            elif message.content.__contains__("kirk-startMonitor"):
                await message.reply("Setting up.......")
                if fileOperations.getFlag(message.guild) == '1':
                    await message.reply("Monitor already running")
                    return
                else:
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
            elif message.content.__contains__("kirk-fileDump"):
                await fileDump()


client = MyClient()
client.run(os.environ["BOT-TOKEN"])
