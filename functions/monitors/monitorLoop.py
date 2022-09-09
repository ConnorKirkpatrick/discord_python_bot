import serverList
from functions import fileOperations
import datetime


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
            message = "SERVER: " + server['NAME'] + "\nIP: " + server['IP_ADDRESS'] + "\nPORT: " + server[
                'PORT'] + "\nMISSION: " + server['MISSION_NAME'] + "\nPLAYERS: " + server['PLAYERS'] + "\nTIME UP: " + \
                      server['MISSION_TIME_FORMATTED'] + "\nLAST CHECKED: " + str(datetime.datetime.now()).split(".")[0]
            flag = 1
            try:
                await channel.last_message.delete()
            except Exception as e:
                print(e)
            finally:
                await channel.send(message)
                break
    if flag == 0:
        try:
            await channel.last_message.delete()
        except Exception as e:
            print(e)
        finally:
            await channel.send(
                "Server unreachable:" + requestServer + "\nCheck the server name, else it is down.\nLAST CHECKED:" +
                str(datetime.datetime.now()).split(".")[0])
    return 1