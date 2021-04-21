import threading

def setupFile(guild):
    guild = str(guild)
    values = open("guildSettings/"+guild+".txt", "w")
    values.write("channel:,ServerName:,monitorFlag:0,guild:")
    values.close()


def getChannel(guild):
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
        channel = content[0].split(",")[0].split(":")[1]
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


def getServer(guild):
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
        server = content[0].split(",")[1].split(":")[1]
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
        values = open(guild+".txt", "r")
        content = values.readlines()
        values.close()
        content = content[0].split(",")
        new = content[0] + ",ServerName:" + Server + "," + content[2] + ","
        f = open("guildSettings/"+guild+".txt", "w")
        f.write(new)
        f.close()


def getFlag(guild):
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
        flag = content[0].split(",")[2].split(":")[1]
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

def getGuild():
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    guild = content[0].split(",")[3].split(":")[1]
    return guild

def setGuild(guild):
    guild = str(guild)
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    content = content[0].split(",")
    new = content[0] + ","+content[1]+",monitorFlag:" + content[2] + ",guild:" + guild
    f = open("values.txt", "w")
    f.write(new)
    f.close()