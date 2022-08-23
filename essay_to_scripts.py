from tkinter import *
import customtkinter as ck
import re

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


# output_txt = ck.CTkLabel(
# 	master=root,
# 	textvariable=src_txt,
# 	text='Click to Convert'
# 	)
output_txt = Text(root)


### layout  ###
input_txt.pack(pady=10,padx=10)
button1.pack(pady=10, padx=10)
output_txt.pack(pady=10, padx=10)
button2.pack(pady=10,padx=10)




root.mainloop()
