import threading

def setupFile(guild):
    guild = str(guild)
    values = open("guildSettings/"+guild+".txt", "w")
    values.write("channel:,ServerName:,monitorFlag:0,guild:")
    values.close()


def getChannel(guild, monitor):
    guild = str(guild)
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        channel = content[monitor-1].split(",")[0].split(":")[1]
        return channel


def setChannel(channel, guild):
    guild = str(guild)
    channel = channel.strip()
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        content = content[0].split(",")
        new = "channel:" + channel + "," + content[1] + "," + content[2] + ","
        f = open("guildSettings/"+guild+".txt", "w")
        f.write(new)
        f.close()


def getServer(guild, monitor):
    guild = str(guild)
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        server = content[monitor-1].split(",")[1].split(":")[1]
        return server


def setServer(Server, guild):
    guild = str(guild)
    Server = Server.strip()
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        content = content[0].split(",")
        new = content[0] + ",ServerName:" + Server + "," + content[2] + ","
        f = open("guildSettings/"+guild+".txt", "w")
        f.write(new)
        f.close()


def getFlag(guild,monitor):
    guild = str(guild)
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        flag = content[monitor-1].split(",")[2].split(":")[1]
        return flag


def setFlag(flag, guild):
    guild = str(guild)
    values = ""
    try:
        values = open("guildSettings/"+guild+".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/"+guild+".txt", "r")
        content = values.readlines()
        values.close()
        content = content[0].split(",")
        new = content[0] + ","+content[1]+",monitorFlag:" + str(flag) + ","
        f = open("guildSettings/"+guild+".txt", "w")
        f.write(new)
        f.close()

def status(guild):
    guild = str(guild)
    try:
        values = open("guildSettings/" + guild + ".txt", "r")
    except Exception as e:
        print(e)
        setup = threading.Thread(target=setupFile, args=(guild,))
        setup.start()
        setup.join()
    finally:
        values = open("guildSettings/" + guild + ".txt", "r")
        content = values.readlines()
        values.close()
        output = ""
        monitorNo = 1
        for monitor in content:
            output = output + "Monitor " + str(monitorNo) + ":"
            output = output + "\n\tServer Name: " + content[monitorNo-1].split(",")[1].split(":")[1]
            output = output + "\n\tChannel: " + content[monitorNo-1].split(",")[0].split(":")[1]
            output = output + "\n\tStatus: " + content[monitorNo-1].split(",")[2].split(":")[1]
            output = output + "\n"
            monitorNo += 1
        return output
