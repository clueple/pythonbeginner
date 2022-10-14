from pathlib import Path 
import numpy as np 
from tkinter import filedialog 
from tkinter import *
from os.path import splitext, basename, dirname
from pathlib import Path 
from tkinter import scrolledtext

"""Variables"""
title_text = 'Split Script'
win_size = "840x480"


""" Bssic Settings """
# app = ck.CTk()
app = Tk()
app.title(title_text)
app.geometry(win_size)
app.focus()


"""click event"""
def upload():
	filetype = [
	("Scripts File", "*.srt"),
	("All Files", "*.*")
	]

	path_open = filedialog.askopenfilename(
		title = 'Open SRT file',
		filetypes = filetype,
		defaultextension = '.srt'
		)

	open_dirname = dirname(path_open)
	open_basename = splitext(basename(path_open))[0]
	open_ext = splitext(basename(path_open))[1]

	open_file_info = f"path open: {path_open}\npath dir: {open_dirname}\nbasename: {open_basename}\nextension: {open_ext}"

	label_txt.set(f"You've uploaded the srt file from {path_open}")

	open_path_txt = Path(path_open).read_text(encoding='utf-8')

	preview.delete(1.0, END)
	# preview.insert(END, f"Your script prview here")
	preview.insert(END, open_path_txt)

	dir_txt.set(open_file_info)

def download():
	filetype = [
	("Scripts File", "*.srt"),
	("All Files", "*.*")
	]

	save_path = filedialog.askdirectory(
		title = 'Save SRT here'
		)
	output.delete(1.0, END)
	output.insert(END, f"Your saved file path is as follows:\n{save_path}_eng.srt and {save_path}_can.srt")


"""  Elements  """
# create a upload_btn to upload file
label_txt = StringVar()
label_txt.set(f"Your uploaded srt file should appear here")

dir_txt = StringVar()
dir_txt.set(f"Your uploaded path info should appear here")
output_dir_txt = StringVar()
output_dir_txt.set(f"Your output text should appear here")

label = Label(app, textvariable=label_txt, justify=CENTER)

upload_btn = Button(app, text='Upload File', activebackground='white', activeforeground='black', command=upload)
download_btn = Button(app, text='Download File', activebackground='white', activeforeground='black', command=download)

preview_dir = Label(app, textvariable=output_dir_txt, justify=LEFT)

preview = scrolledtext.ScrolledText(app, width = 50, height=50)
output = scrolledtext.ScrolledText(app, width = 50, height=50)


""" binding """

""" layout """
label.grid(row=2, column=1)
upload_btn.grid(row=1, column=1)
download_btn.grid(row=1,column=2)
preview.grid(row=3, column=1)
preview_dir.grid(row=2, column=2)
output.grid(row=3,column=2)



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