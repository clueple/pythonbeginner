import customtkinter as ck 
import re 
from tkinter import filedialog 
import tkinter as tk 


"""Variables"""
title_text = 'Example App'
win_size = "840x480"


""" Elements """
app = ck.CTk()
app.title(title_text)
app.geometry(win_size)

# app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

"""click event - button"""
def open_file():
	textbox1.delete(0.0, tk.END)
	textbox1.insert(1.0,f" You've clicked 'Open File'. ")

def convert():
	textbox2.delete(0.0, tk.END)
	textbox2.insert(1.0, f"You've clicked 'Convert' ")


"""Element - scrollable textbox"""
#label 1 is the 'Preview' text for textbox1, the preview area
label1 = ck.CTkLabel(master=app, text='Preview', text_color="yellow")

#label 2 is the 'Preview' text for textbox2, the out area
label2 = ck.CTkLabel(master=app, text='Result', text_color='light green')

#textbox 1 is the preview text area; scrollbar1 is attached to textbox1
textbox1 = tk.Text(app, highlightthickness=0,height=20, width=50)
scrollbar1 = ck.CTkScrollbar(app, command=textbox1.yview)

#textbox 2 is the output area; scrollbar2 is attached to textbox2
textbox2 = tk.Text(app, highlightthickness=0, height = 20, width=50)
scrollbar2 = ck.CTkScrollbar(app, command=textbox2.yview)

#button1 is the 'Open File Button' that opens a '.srt' file and show in textbox1, the preview text area
button1 = ck.CTkButton(app, text='Open File', fg_color=('blue','yellow'), text_color='blue', hover_color='light blue', command=open_file)

#button2 is the 'Convert Button' that convert the text in textbox1 to the result text
button2 = ck.CTkButton(app, text='Convert', fg_color=('blue','light green'), text_color='brown', hover_color='white', command=convert)


"""Click Event - Scrollbar"""
textbox1.configure(yscrollcommand=scrollbar1.set) #attach scrollbar1 to textbox1
textbox2.configure(yscrollcommand=scrollbar2.set) #attach scrollbar2 to textbox2


"""layout"""
label1.grid(row=0,column=0)
label2.grid(row=0,column=2)

textbox1.grid(row=1, column=0, sticky='nsew')
scrollbar1.grid(row=1, column=1, sticky="ns")

textbox2.grid(row=1, column=2, sticky='nsew')
scrollbar2.grid(row=1, column=3, sticky="ns")

button1.grid(row=2,column=0)
button2.grid(row=2,column=2)


"""execute program"""
app.mainloop()