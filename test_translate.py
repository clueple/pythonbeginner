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
# press the translate button to translate whatever entered in entry1 to English
def press_translate():
	# src_text = entry1.get()
	# lang_detected = trans.detect(src_text).lang
	# trans_txt = trans.translate(entry1.get(), dest='en')
	# output1.delete(1.0, END)
	# output1.insert(END, trans_txt.text)
	lang_list = ['it', 'de', 'fr', 'ja', 'zh-TW', 'es']
	color_list = ['purple', 'black', 'light blue', 'dark blue', 'green', 'red']
	d_lang_list = ['Italiano', 'Deutsch', 'Francase', '日本語', '廣東話', 'Espanol']


	src_txt = entry1.get()
	lang_detect = trans.detect(src_txt).lang 
	for i in range(len(lang_list)):
		frame = ctk.CTkFrame(app, fg_color=color_list[i])
		label=ctk.CTkLabel(frame, text=d_lang_list[i], text_color='white')
		output=ctk.CTkTextbox(frame, width=200, height=25)

		frame.pack(padx=20, pady=10, fill=X, expand=True)
		label.pack(padx=10, pady=10, side=LEFT)
		output.pack(padx=10, pady=10, fill=X, expand=True)



# translate whatever entered into the entry widget (entry1) to English
def to_eng(e):
	# entered text
	enter_text = entry1.get()
	enter_lang = trans.detect(enter_text)
	preview_text = trans.translate(enter_text, dest='en')
	output1.delete(1.0, END)
	output1.insert(END, preview_text.text)



# create frames
frame1 = ctk.CTkFrame(app)
frame2 = ctk.CTkFrame(app, fg_color='Red')


# input text area
entry1 = ctk.CTkEntry(frame1, width=600, height=25, placeholder_text='Enter Text Here', border_width=2, corner_radius=10)
button = ctk.CTkButton(frame1, width=100, height=25, text='Translate', command=press_translate)

label1 = ctk.CTkLabel(frame2, text='English', text_color='White')
output1 = ctk.CTkTextbox(frame2, width=200, height=25)

# layout
frame1.pack(padx=20, pady=10, fill=X, expand=True)
button.pack(padx=10, pady=10, side=RIGHT)
entry1.pack(padx=20, pady=10, fill=X, expand=True)

frame2.pack(padx=20, pady=10, fill=X, expand=True)
label1.pack(padx=10, pady=10, side=LEFT)
output1.pack(padx=10, pady=10, fill=X, expand=True)



# bind
entry1.bind('<KeyRelease>', to_eng)



app.mainloop()

