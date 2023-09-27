import os, time

mX = os.get_terminal_size().columns 
s = 1

while True:
    x, pX = 1, 0
    sX = ''

    while len(sX) < mX:
        x, pX = x + pX, x
        sX = str(x)

        print(sX)
        time.sleep(s * (1 / len(sX)))