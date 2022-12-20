import pyjyutping as jtc 
from tabulate import tabulate 
# import customtkinter as ctk 
from tkinter import *
# import tkinter as tk 
from googletrans import Translator

import ttkbootstrap as btk
from ttkbootstrap.constants import *  

""" Backend Settings """
# pattern to be used:
pat = "[-a-zA-Z0-9]+|[\S]"
title_txt = "Warren's Translation"
win_size = "720x640"
label_select_font_txt = "Select Font"

# ctk.set_appearance_mode("system") # Modes: "System" (standard), "Dark", "Light"
# ctk.set_default_color_theme("green") # Themes: "blue" (standard), "green", "dark-blue"

# create a google translator
trans = Translator()

app = btk.Window()
# app = btk.Window(themename='minty')
# app = ctk.CTk()
app.geometry(win_size)
app.title(title_txt)

lang = {
	'name': ['English', 'Italian', 'German', 'French', 'Japanese', 'Chinese', 'Spanish'],
	"code": ['en', 'it', 'de', 'fr', 'ja', 'zh-TW', 'es'],
	"color": ['red','purple', 'black', 'light blue', 'dark blue', 'green', 'brown'],
	"dname": ['English','Italiano', 'Deutsch', 'Français', '日本語', '廣東話', 'Español']
}


my_themes=app.style.theme_names() #list of themes available

"""create style selection"""
r,c = 0,0 #row, 'r', column, 'c' equals 0
my_str = btk.StringVar(value= app.style.theme_use())

for values in my_themes: #list of all the themes
	radio_btn = btk.Radiobutton(app, text=values, variable=my_str, value=values, command= lambda:my_update())
	radio_btn.grid(row=r, column=c, padx=5, pady=20)
	c = c+1 #increase column by 1
	if c>8:
		r,c = r+1, 0

c,r = 0, r+1
for my_style in app.style.colors: # list of styles
	btn = btk.Button(app, text=my_style, bootstyle=my_style)
	btn.grid(row=r, column=c, padx=1, pady=20)
	c = c+1

def my_update():
	app.style.theme_use(my_str.get())

"""create elements"""
entry_list = []
entry_txt = StringVar(value='Enter text here')
for i in range(len(lang['code'])):
	label = btk.Label(app, text=f"{lang['name'][i]}")
	label.grid(row=i+20, column=0, padx=10, pady=5)

	entry = btk.Entry(app, font=20)
	entry.grid(row=i+20 , column=1, pady=5, sticky=NE)

	entry_list.append(entry)

# bind


"""create layout"""



app.mainloop()

