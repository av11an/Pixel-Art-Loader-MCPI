from aproxColor import *
from reformtxt import *
import os

file = input("hex file name from png2txt (no extension): ")
file = file + ".png.txt"

file2name = "placeholder"
file2name = file2name + ".mc.txt"
open(file2name, "x")


with open(file, 'r') as f:
    array = [line.strip() for line in f]


for i in range(0, len(array)):
    n = array[i]
    a = colorIdentify(n)
    print(str(i) + ": " + n + " | " + a)
    array[i] = a

print(array)

with open(file2name, "w") as f2:
    for line in array:
        f2.write("".join(line) + "\n")


# Create final file
newfilename = input("Name of new text file (no extension): ")
newfilename = newfilename + ".mcf.txt"
reformTextFile(file2name, newfilename)



