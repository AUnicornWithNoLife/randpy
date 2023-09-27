import os, time

s = 1

while True:
    mX = os.get_terminal_size().columns 
    x, pX = 1, 0
    sX = ''

    while len(sX) < mX:
        x, pX = x + pX, x
        sX = str(x)

        print(sX)
        time.sleep(s * (1 / len(sX)))