import sys
from textwrap import wrap

global surface
global buffer
global position
global bufferposition
global lpst

surface = [0 for i in range(0, 255)]
buffer = []
position = 0
bufferposition = 0
lpst = 0

def decrement():
    surface[position] = surface[position]-1
    return "-"
    
def increment():
    surface[position] = surface[position]+1
    return "+"
    
def beginloop():
    lpst = bufferposition
    return "{"
    
def endloop():
    if (surface[position] == 0):
        bufferposition = bufferposition + 1
    else:
        bufferposition = lpst
    return "}"
    
def moveleft():
    position = position - 1
    return "<"
    
def moveright():
    position = position + 1
    return ">"
    
def out():
    print(chr(surface[position]))
    return "o"

cmd = {
    "hhh" : decrement(),
    "HHH" : increment(),
    "Hhh" : beginloop(),
    "hhH" : endloop(),
    "hHH" : moveleft(),
    "HHh" : moveright(),
    "hHh" : out()
}

with open(sys.argv[1], 'r') as H:
    ext = H.name.split(".")
    extension = ext[-1]
    if (extension != ("hflat" or "hft")):
        sys.exit(f"Invalid file type {extension}")
    active = H.read()

active = active.replace("\n", "")
buffer = wrap(active, 3)

for i in range(0, len(buffer)):
    bufferposition = i
    # print(cmd[buffer[i]], end='')
    cmd[buffer[i]]
    i = bufferposition

print(surface)