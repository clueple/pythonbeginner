from pathlib import Path 
import numpy as np 
from tkinter import filedialog 
from tkinter import *
from os.path import splitext, basename, dirname
from pathlib import Path 
from tkinter import scrolledtext

"""Variables"""
title_text = 'Split Script'
win_size = "640x480"


""" Bssic Settings """
# app = ck.CTk()
app = Tk()
app.title(title_text)
app.geometry(win_size)


"""click event"""
def upload():
	label_txt.set( F"Path of your uploaded srt file should appear here")
	preview.delete(1.0, END)
	preivew.insert(END, f"Text from your uploaded srt file should appear here!")


"""  Elements  """
# create a button to upload file
label_txt = StringVar()
label = Label(app, textvariable=label_txt)
button = Button(app, text='Upload File', activebackground='white', activeforeground='black', command=upload)
preview = scrolledtext.ScrolledText(app, width = 50, height=50)


""" binding """


""" layout """
label.grid(row=0, column=1)
button.grid(row=1, column=1)
preview.grid(row=2, column=1)

app.mainloop()




"""
Object for function, 'split_text': 
to split the bilingual script, 'b_srt', into single language srt (either 'top' or 'bottom' language)

An example of a subtitle content

1 ---> this is the script index ('srt_index')
00:00:00,000 --> 00:00:02,233 ---> this is the timecode for 'srt_index == 1'
If you shoot video very often  ---> this is the 'top' language content for 'srt_index==1'
成日拍片嘅你 ---> this is the 'bottom' language content for 'srt_index==1'

Parameters explanation:

b_srt: location of the bilingual script;
step: number of lines for script content in the same language repeats, for a single-lined bilingual script, the step is 5 by default
lang_begin_pos: the top language should start from line index (i == 2) where the bottom language should begin at (i==3)
target_lang: either 'top' or 'bottom' where the 'top' language stacks on top of the 'bottom' lang
index_shift: get the line index of each srt_index
timestamp_shift: get the line index of each timecode (for each srt_index)

"""
# def split_text(file, target_lang): 
	
# 	#bilingual text
# 	b_text = text_obj(src_file=file).splitlines()

# 	lang_begin_pos = {'top':2, 'bottom': 3}
# 	index_shift = {'top': 2, 'bottom': 3}
# 	timestamp_shift = {'top': 1, 'bottom':2}
# 	step = 5
	
# 	for i in range(0, len(b_text)):
# 		if i % step == lang_begin_pos[target_lang]: 
# 			srt_index = b_text[i-index_shift[target_lang]]
# 			timecode_index = b_text[i-timestamp_shift[target_lang]]
# 			content = f"{srt_index}\n{timecode_index}\n{b_text[i]}\n"
# 			print(content)


# bilingual script in srt format
# b_srt = r'G:/pytube_vid/edit3_combine_part5.srt'
#preview
# top = split_text(file=b_srt, target_lang='top')
# bottom = split_text(file=b_srt, target_lang='bottom')