from pydoc import text
import tkinter as tk
from tkinter import *
from turtle import right
from unittest import loader
from PIL import ImageTk, Image
import pickle

class Pixelart:
    def __init__(self, name, length, width, ar):
        self.name = name
        self.length = length
        self.width = width
        self.ar = ar

    def set_size(self, length, width):
        self.length = length
        self.width = width

    def get_size(self):
        return self.length, self.width

    def set_array(self, ar):
        self.ar = ar

    def get_array(self):
        return self.ar

    def __str__(self):
        return '\n{} has a length and width of {}, with an array code of {}.'.format(self.name, self.get_size(),
                                                                                     self.get_array())

def addNewPixelArt(name, length, width, array):
    newPixelArt = Pixelart(name, length, width, array)
    with open((name + '.pkl'), 'wb') as save_mcpa:
        pickle.dump(newPixelArt, save_mcpa)

def SaveArt():
    emptyArray = []
    name = input("\nName of Pixel Art [WARNING: If you name the pixel art the same name as one previously saved it will overwrite that pixel art!]: ")
    l = int(input("Length of Pixel Art: "))
    w = int(input("Width of Pixel Art: "))
    for x in range(0, w):
        b = list(map(int, input("Paste row #"+str(x+1)+": ").split(', ')))
        print(b)
        emptyArray.append(b)
    addNewPixelArt(name, l, w, emptyArray)
    emptyArray = []

def load_pixelart(inputed_name):
    print(inputed_name)
    try:
        with open((inputed_name + '.pkl'), 'rb') as load_mcpa:
            pixelArtLoaded = pickle.load(load_mcpa)
            print(pixelArtLoaded)

            # Debug Array
            s = pixelArtLoaded.get_array()
            print("\n")
            print(str(s[0][0]))
    except:
        print("\nNo saved Pixel Art found!")

class MainMenu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nesw')

        self.load_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.width_var = tk.StringVar()
        self.length_var = tk.StringVar()

        self.listing = {}

        for p in (MainPage, LoadPage, SavePage):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky='nesw')
            self.listing[page_name] = frame

        self.up_frame('MainPage')

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()


class MainPage(tk.Frame):
    def displayImg(self):
        global img
        path = r"title_image.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(self, image=img)
        panel.pack(ipadx=10, ipady=10, expand=True)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.displayImg()

        bou = tk.Button(self, text="Load", width="40", command=lambda: controller.up_frame("LoadPage"))
        bou.pack()

        bou2 = tk.Button(self, text="Save", width="40", command=lambda: controller.up_frame("SavePage"))
        bou2.pack()


class LoadPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.load_var = controller.load_var

        text = Label(self, text="Input Name of Pixel Art")
        text.pack(side=TOP)

        bou = tk.Button(self, text="Back", command=lambda: controller.up_frame("MainPage"))
        bou.pack(side=BOTTOM)

        load_input = Entry(self, textvariable=controller.load_var)
        load_input.pack()

        submitBtn = tk.Button(self, text="Input",command=lambda: load_pixelart(controller.load_var.get()))
        submitBtn.pack()

class SavePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.name_var = controller.name_var
        self.width_var = controller.width_var
        self.length_var = controller.length_var

        text_name = Label(self, text="Name of PixelArt").pack()
        name_input = Entry(self, textvariable=controller.name_var)
        name_input.pack()

        text_width = Label(self, text="Width").pack()
        width_input = Entry(self, textvariable=controller.width_var)
        width_input.pack()

        text_length = Label(self, text="Length").pack()
        length_input = Entry(self, textvariable=controller.length_var)
        length_input.pack()

        bou = tk.Button(self, text="Back", command=lambda: controller.up_frame("MainPage"))
        bou.pack(side=BOTTOM)


if __name__ == '__main__':
    app = MainMenu()
    app.geometry('400x100')
    blank_space = " "
    app.title("Pixel Art Loader")
    app.mainloop()

