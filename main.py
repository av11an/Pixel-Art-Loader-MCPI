import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class MainMenu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nesw')

        self.listing = {}

        for p in (MainPage, LoadPage):
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


class LoadPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bou = tk.Button(self, text="Back", command=lambda: controller.up_frame("MainPage"))
        bou.pack(side=BOTTOM)


if __name__ == '__main__':
    app = MainMenu()
    app.geometry('325x100')
    blank_space = " "
    app.title(70 * blank_space + "Pixel Art Loader")
    app.resizable(False, False)
    app.mainloop()

