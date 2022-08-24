from tkinter import *
import customtkinter as ck
import re
from tkinter import filedialog

#### Variables  ##
title_txt = 'Scripts Converter'
win_size = '640x480'
label_txt = 'Label Text'
button_txt = 'Convert'
switch_txt = 'Switch text'
switch_output_txt = 'The output is already changed.'
pattern = "[.,?!;:]"
# pattern = r"\W"
rep = r"\n"


### click event  ###
def convert():
	result = re.sub(pattern, rep, input_txt.get(1.0, END))
	# update_result = src_txt.set(f'{result}')
	output_txt.delete('1.0', "end")
	# print(output_txt.insert(END, result))
	output_txt.insert(END,result)

def save_file():
	result = re.sub(pattern, rep, input_txt.get(1.0, END))
	file = filedialog.asksaveasfilename(
		filetypes=[('text file', '*.txt'), ('CSV file', '*.csv')],
		defaultextension= '.txt',
		#initialdir = r'D:/',
		title = 'Save As'
		)
	fob = open(file,'w')
	fob.write(f"{result}")
	fob.close()


#### Elements  ##
root = ck.CTk()
root.title(title_txt)
root.geometry(win_size)

src_txt = StringVar()

input_txt = Text(
	master=root,
	height=10,
	width=80
	)

button1 = ck.CTkButton(
	master = root,
	command= convert,
	text = button_txt
	)
button2 = ck.CTkButton(
	master = root,
	command = lambda: input_txt.delete(1.0, END),
	text = 'Clear'
	)
button3 = ck.CTkButton(
	master = root,
	command = save_file
	,
	text = 'Export To File'
	)

output_txt = Text(root)



### layout  ###
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
input_txt.grid(row=1, columnspan=3)
output_txt.grid(row=2, columnspan=3)





root.mainloop()
