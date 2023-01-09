# import flet 
from flet import *
from pyjyutping import jyutping as jtc 
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
	page.title = "Warern's App"
	page.vertical_alignment = "center"
	page.window_height = 108*6
	page.window_width = 108*6

	"""events"""
	def get_eng(e):
		try:
			eng_trans.value = trans.translate(e.control.value,'en').text
		except:
			eng_trans.value = "Please try again"
		page.update()

	def get_lang(e):
		result.controls = [TextField(label=lang['dname'][i], value=trans.translate(eng_trans.value,dest=item).text) for i, item in enumerate(lang['code'])]
		page.update()
    

	"""elements"""
	entry = TextField(label = 'Enter text', on_change=get_eng)
	eng_trans = TextField(label='English Translation', multiline=True)
	btn_get_lang = ElevatedButton("Get Language", icon="select_all_rounded", on_click = get_lang)
	# lang_labels = Column()
	result = Column()

	page.add(
		Column(controls = [
			#1st item of the main column
			entry,
			#2nd item of main column
			eng_trans,
			#3rd item of the main column
			btn_get_lang,
			# 4th item of the main column
			# Row(controls=[lang_labels,result])
            result
			]
			)
		)
	
	page.update()

app(target=main, view=WEB_BROWSER)
