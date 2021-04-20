def getChannel():
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    channel = content[0].split(",")[0].split(":")[1]
    return channel


def setChannel(channel):
    channel = channel.strip()
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    content = content[0].split(",")
    new = "channel:" + channel + "," + content[1] + "," + content[2] + ","
    f = open("values.txt", "w")
    f.write(new)
    f.close()


def getServer():
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    server = content[0].split(",")[1].split(":")[1]
    return server


def setServer(Server):
    Server = Server.strip()
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    content = content[0].split(",")
    new = content[0] + ",ServerName:" + Server + "," + content[2] + ","
    f = open("values.txt", "w")
    f.write(new)
    f.close()


def getFlag():
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    flag = content[0].split(",")[2].split(":")[1]
    return flag


def setFlag(flag):
    values = open("values.txt", "r")
    content = values.readlines()
    values.close()
    content = content[0].split(",")
    new = content[0] + ","+content[1]+",monitorFlag:" + str(flag) + ","
    f = open("values.txt", "w")
    f.write(new)
    f.close()
