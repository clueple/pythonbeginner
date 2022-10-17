from pathlib import Path 
import numpy as np 
from tkinter import filedialog 
from tkinter import *
from os.path import splitext, basename, dirname
from pathlib import Path 
from tkinter import scrolledtext

"""Variables"""
title_text = 'Split Script'
win_size = "1280x480"
warn_msg_upload_srt = f"Please upload caption file (.srt)" #warning message when no caption file is uploaded
download_txt = f"Press [Download]"


""" Bssic Settings """
# app = ck.CTk()
app = Tk()
app.title(title_text)
app.geometry(win_size)
app.focus()
label1_default_txt = 'Upload Your Bilingual Script Here'
label2_default_txt = 'Language(Top) Output Text'
label3_default_txt = 'Language(Bottom) Output Text'


"""file type choices"""
open_file_type = [
	("Scripts File", "*.srt"),
	("All Files", "*.*")
	]

save_file_type = [("srt", "*.srt")]

"""Path Info For file opened or saved"""
def file_info(path):
	foldername = dirname(path)
	filename = splitext(basename(path))[0]
	ext = splitext(basename(path))[1]
	fileinfo = f"Folder name: {foldername}\nFile name: {filename}\nextension: {ext}"
	return fileinfo


"""click event"""
def upload():

	path_open = filedialog.askopenfilename(
		title = 'Open SRT file',
		filetypes = open_file_type,
		defaultextension = '.srt'
		)

	open_path_txt = Path(path_open).read_text(encoding='utf-8')

	text_area1.delete(1.0, END)
	text_area1.insert(END, open_path_txt)

	label1_txt.set(f"Source File:\n{file_info(path=path_open)}")

def download():

	save_path = filedialog.askdirectory(
		title = 'Save SRT here'
		)

	top_lang_output = "Top Language Result"
	bottom_lang_output = "Bottom Language Result"

	text_area2.delete(1.0, END)
	text_area2.insert(END, top_lang_output)

	text_area3.delete(1.0, END)
	text_area3.insert(END, bottom_lang_output)



"""  Elements  """
"""label text variables"""
label1_txt = StringVar()
label2_txt = StringVar()
label3_txt = StringVar()

label1 = Label(app, textvariable=label1_txt, justify=CENTER)
label2 = Label(app, textvariable=label2_txt, justify=CENTER)
label3 = Label(app, textvariable=label3_txt, justify=CENTER)


upload_btn = Button(app, text='Upload File', activebackground='white', activeforeground='black', command=upload)
download_btn = Button(app, text='Download File', activebackground='white', activeforeground='black', command=download)

text_area1 = scrolledtext.ScrolledText(app, width = 50, height=50)
text_area2 = scrolledtext.ScrolledText(app, width = 50, height=50)
text_area3 = scrolledtext.ScrolledText(app, width = 50, height=50)

""" binding """
label1_txt.set(label1_default_txt)
label2_txt.set(label2_default_txt)
label3_txt.set(label3_default_txt)


""" layout """
upload_btn.grid(row=1, column=1)
download_btn.grid(row=1,column=2, columnspan=2)

label1.grid(row=2, column=1)
label2.grid(row=2, column=2)
label3.grid(row=2,column=3)

text_area1.grid(row=3, column=1)
text_area2.grid(row=3,column=2)
text_area3.grid(row=3,column=3)



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
#text_area1
# top = split_text(file=b_srt, target_lang='top')
# bottom = split_text(file=b_srt, target_lang='bottom')