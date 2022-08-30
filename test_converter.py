from tkinter import *
import tkinter as tk
import customtkinter as ck
from pathlib import Path
import re

### variables ###
title_txt = "Scripts Converter"
win_size = '720x560'
label_txt = 'Label Text'
button_txt = 'Convert'
switch_txt = 'Switch Text'
switch_output_txt = 'The output is already changed'
pattern = "[,.?!;:]"
c_pattern = r"\W"
rep = "\n"

### click event ###
root = ck.CTk() #this is the main window
root.title(title_txt) #the title text of the window element
root.geometry(win_size) #the size of the window element


### Elements ###
element1 = ck.CTkLabel(master = root, text='element1')
element2 = ck.CTkLabel(master = root, text='element2')
element3 = ck.CTkLabel(master = root, text='element3')
element4 = ck.CTkLabel(master = root, text='element4')
element5 = ck.CTkLabel(master = root, text='element5')
element6 = ck.CTkLabel(master = root, text='element6')
element7 = ck.CTkLabel(master = root, text='element7')
element8 = ck.CTkLabel(master = root, text='element8')
element9 = ck.CTkLabel(master = root, text='element9')


### Layout ###
element1.grid(row=0, column=0)
element2.grid(row=0, column=1)
element3.grid(row=0, column=2)
element4.grid(row=1, column=0)
element5.grid(row=2, column=0, columnspan=2)
element6.grid(row=1, column=1)
element7.grid(row=1, column=2)
element8.grid(row=2, column=3, columnspan=2)
element9.grid(row=1, column=3)

root.mainloop()
