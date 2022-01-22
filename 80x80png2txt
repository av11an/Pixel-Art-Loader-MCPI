from PIL import Image

'''
with open("outfile", "w") as outfile:
    outfile.write("\n".join(itemlist))
'''


def hexcon(num):
    key = "0123456789abcdef"  # hex key
    h = ""
    h16 = int(num / 16)
    h1 = num % 16
    h = key[h16] + key[h1]
    return h


def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return r, g, b


def main():
    skipValue = 16
    print("At this point only an 80x80 pixel image.")
    img_name = input("Input the image name to be processed : ")
    outfilename = img_name + ".txt"
    with open(outfilename, "w") as outfile:
        for y in range(0, 80):
            for x in range(0, 80):
                r, g, b = rgb_of_pixel(img_name, x, y)
                # print(r,g,b," ",end="")
                rhex = hexcon(r);
                ghex = hexcon(g);
                bhex = hexcon(b)
                hexval = rhex + ghex + bhex
                cathexval = "#" + hexval
                print(x, y, cathexval)
                outfile.write(cathexval + "\n")
            outfile.write("endline\n")


main()
