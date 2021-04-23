import asyncio
import os

import discord

import fileOperations
import monitorTimer


##duplicating the .txt on the end of the files

async def startupRecovery():
    files = os.listdir("guildSettings")
    for file in files:
        f = open("guildSettings/" + file, "r")
        data = f.readlines()
        f.close()
        file = file[:-4]
        flag = data[0].split(",")[2].split(":")[1]
        if flag == '1':
            print("Starting: " + file)
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
                                    "setChannel [channel]-[monitor]: set the channel to post the status into and the monitor responsible\n"
                                    "setServer [server]-[monitor]: give the full name of the server of the server to monitor and the monitor responsible\n"
                                    "startMonitor [monitor]: Start monitor\n"
                                    "stopMonitor [monitor]: stop monitor\n"
                                    "status: displays the current status of your monitors\n"
                                    "help: Display this message")

            elif message.content.__contains__("kirk-setChannel"):
                messageDetails = str(message.content[15:]).split("-")
                try:
                    if int(messageDetails[1]) > 5:
                        await message.reply("Monitor out of range, max is 5")
                    else:
                        await message.reply("setting channel to: '" + messageDetails[0] + "' on monitor: " + messageDetails[1])
                        fileOperations.setChannel(messageDetails[0], messageDetails[1], message.guild)
                except Exception as e:
                    print(e)
                    await message.reply("Monitor is not a valid number")

            elif message.content.__contains__("kirk-setServer"):
                messageDetails = str(message.content[14:]).split("-")
                try:
                    if int(messageDetails[1]) > 5:
                        await message.reply("Monitor out of range, max is 5")
                    else:
                        await message.reply("setting server to: '" + messageDetails[0] + "' on monitor: "+messageDetails[1])
                        fileOperations.setServer(messageDetails[0], messageDetails[1], message.guild)
                except Exception as e:
                    print(e)
                    await message.reply("Monitor is not a valid number")

# TODO: setup monitor choice for following 2 methods
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
                await message.reply(fileOperations.status(message.guild))

            elif message.content.__contains__("kirk-fileDump"):
                await fileDump()


client = MyClient()
client.run(os.environ["BOT-TOKEN"])
