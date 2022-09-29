# import customtkinter as ck 
# import re 
from tkinter import filedialog 
from tkinter import *
from tkinter import ttk

"""Variables"""
title_text = 'Example App'
win_size = "640x480"


""" Elements """
# app = ck.CTk()
app = Tk()
app.title(title_text)
app.geometry(win_size)

"""click event """
def download():
	entry.delete(0, END)
	entry.insert(END, 'insert video url here')
	label.configure(text=f"You have downloaded from: {entry.get()}")

"""Elements"""

#step 2 --- create entry widget, with the 'url' as the textvariable of entry widget
url=StringVar()
entry = Entry(app, width=50, textvariable=url)   
#step 3 --- create h_scrollbar set command to bind to entry widget
h_scrollbar = Scrollbar(app, orient='horizontal' , command=entry.xview)
#step 6 --- create a button to download video from the link specified in 'entry' widget
button = Button(app, text='Download', activebackground='white', activeforeground='black', command=download)
label = Label(app)


"""teting the entry field """

""" binding """
#step 4 --- bind the entry widget to the h_scrollbar
entry.config(xscrollcommand=h_scrollbar.set)

"""layout"""
#step 5 --- set layout for entry, and h_scrollbar; remember to set the h_scrollbar's position below the entry
entry.grid(row=0,column=0)
h_scrollbar.grid(row=1, column=0, sticky='we')
button.grid(row=2,column=0, sticky='we')
label.grid(row=3,column=0,sticky='nsew')

"""run program"""
app.mainloop()


# url = r"https://youtu.be/00yGusN2-Uw"


# from pytube import YouTube
# vid = YouTube(url)
# file = vid.streams.get_lowest_resolution()
# opath = r'F:/'
# file.download(opath)


