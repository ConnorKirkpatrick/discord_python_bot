import serverList
import fileOperations
import datetime


async def getDetails(client,guild,message):
    servers = serverList.getServerList()
    requestServer = str(fileOperations.getServer(guild))
    channel = fileOperations.getChannel(guild)
    if channel is None or requestServer is None:
        print("Bad config")
        await message.reply("Check your configuration")
        fileOperations.setFlag(0,guild)
        return
    try:
        channel = int(channel)
    except Exception as e:
        print(e)
        print("Bad config")
        await message.reply("Check your configuration")
        fileOperations.setFlag(0,guild)
        return
    channel = client.get_channel(channel)
    flag = 0
    # print(servers['SERVERS'])
    # name,ip_address,port,mission_name,mission_time,players,players_max,description,mission_time_formatted
    for server in servers['SERVERS']:
        if server['NAME'] == requestServer:
            message = "SERVER: " + server['NAME'] + "\nIP: "+ server['IP_ADDRESS']+ "\nPORT: "+ server['PORT']+ "\nMISSION: "+ server['MISSION_NAME']+ "\nPLAYERS: "+ server['PLAYERS']+ "\nTIME UP: "+ server['MISSION_TIME_FORMATTED']+ "\nLAST CHECKED: "+ str(datetime.datetime.now()).split(".")[0]
            #print(message)
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
            await channel.send("Server unreachable:"+requestServer+"\nCheck the server name, else it is down.\nLAST CHECKED:"+str(datetime.datetime.now()).split(".")[0])
            # print("unreachable")