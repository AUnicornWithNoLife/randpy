import os, time, shutil

org, dest = "C:/Users/Visitor/Downloads/", "D:/"

off = .5

while True:
    time.sleep(off)

    o = os.listdir(org)
    d = os.listdir(dest)

    if len(o) <= 0:
        continue

    for ide in d:
        try:
            os.remove(dest + ide)
        except e:
            print(e)

    for io in o:
        try:
            shutil.move(org + io, dest + io)
        except e:
            print(e)
