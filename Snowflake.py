import copy
import random
import shutil
import time
import os

cols, rows  = shutil.get_terminal_size()

def create_lineofsnow(cols, x=0):
    lineofsnow = []
    for i in range(random.randint(x, cols)):
        rand_a = random.randint(0,2)
        if rand_a == 0:
            lineofsnow.append("*")
        elif rand_a == 1:
            lineofsnow.append("+")
        else:
            lineofsnow.append(" ")
    for _ in range(cols-len(lineofsnow)):
        lineofsnow.append(" ")
    random.shuffle(lineofsnow)
    return copy.deepcopy(lineofsnow)

def makeitsnow():
    os.system('cls')
    screenofsnow = []
    while True:
        os.system('cls')
        screenofsnow.insert(0, create_lineofsnow(cols))
        if len(screenofsnow) > rows:
            screenofsnow.pop()
        for line in screenofsnow:
            for chars in line:
                print(chars, end="")
            print("")
        time.sleep(0.5)

makeitsnow()