import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2
root = Tk()

root.geometry('800x500') ##这个小了一点，不知道怎么自适应
root.title('图片处理')

def choosepic():
    path_ = askopenfilename()
    img= cv2.imread(path_ )
    current_image = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=current_image)
    image_label.config(image=imgtk)
    image_label.image = imgtk # keep a reference



path = StringVar()
Button(root, text='选择图片', command=choosepic).pack()
file_entry = Entry(root, state='readonly', text=path)
#file_entry.pack()
image_label = Label(root)
image_label.pack()
root.mainloop()