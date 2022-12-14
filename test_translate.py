import pyjyutping as jtc 
from tabulate import tabulate 
import customtkinter as ctk 
from tkinter import *
from googletrans import Translator

""" Backend Settings """
# pattern to be used:
pat = "[-a-zA-Z0-9]+|[\S]"
title_txt = "Warren's Translation"
win_size = "720x640"
label_select_font_txt = "Select Font"

ctk.set_appearance_mode("system") # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green") # Themes: "blue" (standard), "green", "dark-blue"

# create a google translator
trans = Translator()

app = ctk.CTk()
app.geometry(win_size)
app.title(title_txt)

# functions
def press_translate():
	src_text = entry1.get()
	lang_detected = trans.detect(src_text).lang
	trans_txt = trans.translate(entry1.get(), dest='en')
	output1.delete(1.0, END)
	output1.insert(END, trans_txt.text)


# create frames
frame1 = ctk.CTkFrame(app)
frame2 = ctk.CTkFrame(app)

# input text area
entry1 = ctk.CTkEntry(frame1, width=600, height=25, placeholder_text='Enter Text Here', border_width=2, corner_radius=10)
button = ctk.CTkButton(frame1, width=100, height=25, text='Translate', command=press_translate)

output1 = ctk.CTkTextbox(frame2, width=200, height=25)

# layout
frame1.pack(padx=20, pady=10, fill=X, expand=True)
button.pack(padx=10, pady=10, side=RIGHT)
entry1.pack(padx=20, pady=10, fill=X, expand=True)

frame2.pack(padx=20, pady=10, fill=X, expand=True)
output1.pack(padx=10, pady=10, fill=X, expand=True)


app.mainloop()

