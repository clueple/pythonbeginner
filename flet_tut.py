from flet import *
from pyjyutping import jyutping as jtc 
from pycantonese import segment 
from googletrans import Translator
import re 

pat = r'[-a-zA-Z0-9]+|[\S]'

#translator object for human language translation
trans = Translator()

lang ={
	'code': ['en', 'it', 'de', 'ja', 'fr', 'zh-TW', 'es'],
	'dname': ['English', 'Italiano', 'Deutsch', '日本語', 'Français', '廣東話', 'Español'],
	'name':['English', 'Italian', 'German', 'Japanese', 'French', 'Cantonese', 'Spanish'],
	'color':['red', 'purple', 'black', "#211790", 'blue', 'green', 'brown']
}


def main(page: Page):
	"""background settings"""
	page.window_width = 108*6
	page.window_height = 135*6	

	"""create elements"""
	element1 = TextField(label="element 1")
	element2 = TextField(label="element 2")


	"""design layout"""
	page.add(
		Container(
			content=Column(controls=[element1, element2])
			)
		)


app(target=main, view=WEB_BROWSER)
