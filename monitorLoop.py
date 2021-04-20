import serverList
import fileOperations
import datetime


async def getDetails(client):
    servers = serverList.getServerList()
    requestServer = str(fileOperations.getServer())
    channel = client.get_channel(int(fileOperations.getChannel()))
    flag = 0
    # print(servers['SERVERS'])
    # name,ip_address,port,mission_name,mission_time,players,players_max,description,mission_time_formatted
    for server in servers['SERVERS']:
        if server['NAME'] == requestServer:
            message = "SERVER: " + server['NAME'] + "\nIP: "+ server['IP_ADDRESS']+ "\nPORT: "+ server['PORT']+ "\nMISSION: "+ server['MISSION_NAME']+ "\nPLAYERS: "+ server['PLAYERS']+ "\nTIME UP: "+ server['MISSION_TIME_FORMATTED']+ "\nLAST CHECKED: "+ str(datetime.datetime.now()).split(".")[0]
            print(message)
            flag = 1
            await channel.last_message.delete()
            if channel:
                await channel.send(message)
                break
    if flag == 0:
        try:
            await channel.last_message.delete()
            if channel:
                await channel.send("Server unreachable:"+requestServer+"\nCheck the server name, else it is down.\nLAST CHECKED:"+str(datetime.datetime.now()).split(".")[0])
                print("unreachable")
        except Exception as e:
            print(e)