import math

# define minecraft wool hex colors
hexWoolColors = ['e4e4e4', 'ea7e35', 'be49c9', '6387d2', 'c2b51c',
                 '39ba2e', 'd98199', '414141', 'a0a7a7', '267191',
                 '7e34bf', '253193', '56331c', '364b18', '9e2b27', '181414']

WoolColorsName = ['White', 'Orange', 'Magenta', 'Light Blue', 'Yellow',
                  'Lime', 'Pink', 'Gray', 'Light Gray', 'Cyan', 'Purple',
                  'Blue', 'Brown', 'Green', 'Red', 'Black']

WoolColorsPI = ['0', '1', '2', '3', '4',
                '5', '6', '7', '8', '9', 'A',
                'B', 'C', 'D', 'E', 'F']


def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def aproxColor(hexVal, aprox_val):
    aprox_val = []
    a = hex_to_rgb(hexVal)
    for i in range(0, len(hexWoolColors)):
        b = math.sqrt(pow(a[0] - hex_to_rgb(hexWoolColors[i])[0], 2) +
                      pow(a[1] - hex_to_rgb(hexWoolColors[i])[1], 2) +
                      pow(a[2] - hex_to_rgb(hexWoolColors[i])[2], 2))
        aprox_val.append(b)
    return aprox_val


def colorIdentify():
    array = []
    hexColorInput = input("Input Hex Color without #, example ffffff: ")
    c = aproxColor(hexColorInput, array)
    b = c.index(min(c))
    n = WoolColorsName[b]
    r = WoolColorsPI[b]
    print(n+" "+r)
    return r

colorIdentify()
