# import customtkinter as ck 
# import re 
from tkinter import filedialog 
import tkinter as tk 

"""Variables"""
title_text = 'Example App'
win_size = "840x480"


""" Elements """
# app = ck.CTk()
app = tk.Tk()
app.title(title_text)
app.geometry(win_size)


"""click event """
url_input = 'whatever'

"""elements"""
url_entry = ttk.Entry(app, textvariable=url_input, width=20, height=5)

"""layout"""
url_entry.grid(row=0, column=1)


app.mainloop()



# url = r"https://youtu.be/00yGusN2-Uw"


# from pytube import YouTube
# vid = YouTube(url)
# file = vid.streams.get_lowest_resolution()
# opath = r'F:/'
# file.download(opath)


