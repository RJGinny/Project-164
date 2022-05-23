#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:08:15 2022

@author: riddhiekajain
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("PROJECT 164")
root.geometry("500x500")
root.configure(background="lightblue")


label_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
img_path=""
def PlanetInfo():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Text File", filetypes=[("Image Files", "*.jpg *.gif *.jpeg *.png *.webp")])
    print(img_path)
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im)
    label_planet_image["image"]=img
    img.close()
    

btn = Button(root, text="OPEN IMAGE", command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()