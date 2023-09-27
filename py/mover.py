import os, time, shutil

org, dest = "C:/Users/Vistor/Downloads", "D:/"

off = .5

while True:
    time.sleep(off)

    o = os.listdir(org)
    d = os.listdir(dest)

    if len(o <= 0):
        pass

    for ide in d:
        os.remove(dest + d)

    for io in o:
        shutil.move(org + io, dest + io)
        os.remove(org + io)
