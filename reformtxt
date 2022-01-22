import os

textFile = input("name of text file to edit: ")
textFile = textFile + ".png.txt"

newFileName = input("name of new file: ")
placeholder = "placeholder.png.txt"

# create new file
f2 = open(placeholder, "x")
f2 = open(placeholder, "w")

#make all into one line
f1 = open(textFile, "r")

for i, line in enumerate(f1):
    space = " " if i != 0 else ""
    line = line.rstrip('\n')
    f2.write(space + line)

f2.close()
f1.close()

# replace endline with newline
f2 = open(placeholder, "r")
new_file_content = ""
for line in f2:
    strippedline = line.strip()
    new_line = strippedline.replace(" endline", "\n")
    new_file_content += new_line + "\n"
f2.close()


f3 = open(newFileName + ".png.txt", "w")
f3.write(new_file_content)
f3.close()

os.remove("placeholder.png.txt")
