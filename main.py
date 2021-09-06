import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2
global photo
class GUI(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.place()
        self.createWidget()
    def choosepic(self):
        path = askopenfilename(title='choose a image')
        img = Image.open(path)
        width, height = img.size
        img = img.resize((300, int(300/width*height)))
        global photo
        photo = ImageTk.PhotoImage(img)
        self.label03.configure(image = photo)
        self.label03.image = photo
        self.label04.configure(image = photo)
        self.label04.image = photo

    def createWidget(self):
        global photo
        photo = None
        self.label03 = Label(self, image=photo)
        self.label03.grid(column=0, row=0)
        self.label04 = Label(self, image=photo)
        self.label04.grid(column=1, row=0)
        self.b1 = tk.Button(self, text='input image', command=self.choosepic, bg='white', anchor='s')
        self.b1.grid(column=0, row=1)


def gui_start():
    root = tk.Tk()
    root.title("Medical image SR")
    root.geometry("1024x768")
    app = GUI(master=root)
    root.mainloop()

gui_start()
