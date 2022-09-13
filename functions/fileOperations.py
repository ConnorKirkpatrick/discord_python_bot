import discord


def setupFile(guild):
    guild = str(guild)
    values = open("guildSettings/" + guild + ".txt", "w")
    values.write("channel:,ServerName:,monitorFlag:0\nchannel:,ServerName:,monitorFlag:0\nchannel:,ServerName:,"
                 "monitorFlag:0\nchannel:,ServerName:,monitorFlag:0\nchannel:,ServerName:,monitorFlag:0\n")
    values.close()
    return


def getChannel(guild, monitor):
    guild = str(guild)
    values = ""
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
        channel = content[monitor - 1].split(",")[0].split(":")[1]
        return channel


def setChannel(channel, monitor, guild):
    guild = str(guild)
    monitor = int(monitor)
    channel = channel.strip()
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
        newData = ""
        lineCount = 1
        for lines in content:
            if lineCount == monitor:
                lineChange = content[monitor - 1].split(",")
                newLine = "channel:" + channel + "," + lineChange[1] + "," + lineChange[2]
                newData = newData + newLine
                lineCount += 1
            else:
                newData = newData + lines
                lineCount += 1
        f = open("guildSettings/" + guild + ".txt", "w")
        f.write(newData)
        f.close()
        return


def getServer(guild, monitor):
    guild = str(guild)
    values = ""
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
        server = content[monitor - 1].split(",")[1].split(":")[1]
        return server


def setServer(Server, monitor, guild):
    guild = str(guild)
    Server = Server.strip()
    monitor = int(monitor)
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
        newData = ""
        lineCount = 1
        for lines in content:
            if lineCount == monitor:
                lineChange = content[monitor - 1].split(",")
                newLine = lineChange[0] + ",server:" + Server + "," + lineChange[2]
                newData = newData + newLine
                lineCount += 1
            else:
                newData = newData + lines
                lineCount += 1
        f = open("guildSettings/" + guild + ".txt", "w")
        f.write(newData)
        f.close()
        return


def getFlag(guild, monitor):
    guild = str(guild)
    values = ""
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
        flag = content[monitor - 1].split(",")[2].split(":")[1]
        return flag


def setFlag(flag, monitor, guild):
    guild = str(guild)
    monitor = int(monitor)
    flag = str(flag)
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
        newData = ""
        lineCount = 1
        for lines in content:
            if lineCount == monitor:
                lineChange = content[monitor - 1].split(",")
                newLine = lineChange[0] + "," + lineChange[1] + ",monitorFlag:" + flag + "\n"
                newData = newData + newLine
                lineCount += 1
            else:
                newData = newData + lines
                lineCount += 1
        f = open("guildSettings/" + guild + ".txt", "w")
        f.write(newData)
        f.close()
        return


def status(client, guild):
    guild = str(guild)
    try:
        values = open("guildSettings/" + guild + ".txt", "r")
    except Exception as e:
        print(e)
        setupFile(guild)
    finally:
        values = open("guildSettings/" + guild + ".txt", "r")
        content = values.readlines()
        values.close()
        output = ""
        monitorNo = 1
        for monitor in content:
            output = output + "Monitor " + str(monitorNo) + ":"
            output = output + "\n\tServer Name: " + content[monitorNo - 1].split(",")[1].split(":")[1]
            if content[monitorNo - 1].split(",")[0].split(":")[1] == "":
                output = output + "\n\tChannel: "
            else:
                output = output + "\n\tChannel: " + str(client.get_channel(int(content[monitorNo - 1].split(",")[0].split(":")[1])))
            if content[monitorNo - 1].split(",")[2].split(":")[1]:
                output = output + "\n\tStatus: Running"
            else:
                output = output + "\n\tStatus: Halted"
            output = output + "\n"
            monitorNo += 1
        return output
