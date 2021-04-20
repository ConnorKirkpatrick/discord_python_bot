import discord
import os
import time
import threading

import fileOperations
import monitorTimer

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        #await monitorLoop.getDetails(client)



    async def on_message(self, message):
        if message.author == client.user:
            return
        else:
            if message.content.__contains__("kirk-help"):
                await message.reply("Use Commands wit hthe prefix 'kirk-':\nsetChannel: set the channel the monitor will post in\nsetServer: give the full name of the server you wish to monitor\nstartMonitor: Start the monito\nstopMonitor: stop the monitor\nhelp:Display this message")
            elif message.content.__contains__("kirk-setChannel"):
                await message.reply("setting chan")
                fileOperations.setChannel(message.content[15:])
            elif message.content.__contains__("kirk-setServer"):
                await message.reply("setting ser")
                fileOperations.setServer(message.content[14:])
            elif message.content.__contains__("kirk-startMonitor"):
                await message.reply("Setting up.......")
                #fileOperations.setFlag(1)
                time.sleep(2.5)
                await monitorTimer.monitorTimer(client)
            elif message.content.__contains__("kirk-stopMonitor"):
                await message.reply("stopping.....")
                fileOperations.setFlag(0)

client = MyClient()
#client.run(os.environ["BOT-TOKEN"])
main = threading.Thread(target=client.run, args=(os.environ["BOT-TOKEN"],))
print(threading.current_thread())


main.start()
#timer.start()

