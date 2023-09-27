import os, time, shutil

org, dest = "C:/Users/Vistor/Downloads", "D:/"

while True:
    o = os.listdir(org)
    d = os.listdir(dest)

    if len(o <= 0):
        pass

    for ide in d:
        os.remove(dest + d)

    for io in o:
        shutil.move(org + io, dest + io)
        os.remove(org + io)
