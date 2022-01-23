import os

def reformTextFile(textFile, newFileName):
    # create new file
    placeholder = "placeholder.png.txt"
    f2 = open(placeholder, "x")
    f2 = open(placeholder, "w")

    # make everything in file into one line
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

    # create reformatted file
    f3 = open(newFileName, "w")
    f3.write(new_file_content)
    f3.close()

    os.remove("placeholder.png.txt")
    os.remove("placeholder.mc.txt")

if __name__ == "__main__":
    tf = input("Name of text file to reformat with extension: ")
    nfn = input("Input new file name without extension: ")
    reformTextFile(tf, nfn)


