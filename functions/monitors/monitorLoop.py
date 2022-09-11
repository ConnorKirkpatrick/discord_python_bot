import serverList
from functions import fileOperations
import datetime
import discord

async def getDetails(client, guild, message, monitor):

    servers = serverList.getServerList()
    requestServer = str(fileOperations.getServer(guild, monitor))
    channel = fileOperations.getChannel(guild, monitor)

    if channel is None or requestServer is None:
        print("Bad config: bad names")
        try:
            await message.reply("Check your configuration")
        except Exception as e:
            print(e)
        finally:
            fileOperations.setFlag(0, guild, monitor)
            return 0
    try:
        channel = int(channel)
    except Exception as e:
        print(e)
        print("Bad config: bad channel format")
        try:
            await message.reply("Check your configuration")
        except Exception as e:
            print(e)
        finally:
            fileOperations.setFlag(0, guild, monitor)
            return 0
    channel = client.get_channel(channel)
    flag = 0
    # print(servers['SERVERS'])
    # name,ip_address,port,mission_name,mission_time,players,players_max,description,mission_time_formatted
    for server in servers['SERVERS']:
        if server['NAME'] == requestServer:
            embed = discord.Embed(title="Staus for: "+server['NAME'], color=0x336EFF)
            embed.add_field(name="Mission Name", value=server['MISSION_NAME'], inline=False)
            embed.add_field(name="Active players", value=int(server['PLAYERS'])-1, inline=False)
            embed.add_field(name="Last checked", value=str(datetime.datetime.now()).split(".")[0], inline=False)
            flag = 1
            messages = [message async for message in channel.history(limit=1)]
            if len(messages) == 0:
                await channel.send(embed=embed)
                break
            else:
                await messages[0].edit(embed=embed)
                break

    if flag == 0:
        embed = discord.Embed(title="Staus for: " + server['NAME'], color=0x336EFF)
        embed.add_field(name="Mission Name", value="None", inline=False)
        embed.add_field(name="Active players", value=0, inline=False)
        embed.add_field(name="Last checked", value=str(datetime.datetime.now()).split(".")[0], inline=False)
        embed.add_field(name="Status", value="Server unreachable, check name else down", inline=False)
        messages = [message async for message in channel.history(limit=1)]
        if len(messages) == 0:
            await channel.send(embed=embed)
        else:
            await messages[0].edit(embed=embed)
    return 1