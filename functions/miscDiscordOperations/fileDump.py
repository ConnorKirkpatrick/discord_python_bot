import os


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
