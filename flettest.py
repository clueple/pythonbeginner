import flet as ft 
from pyjyutping import jyutping as jtc 
from googletrans import Translator
import re 

#translator object for human language translation
trans = Translator

lang ={
	'code': ['en', 'it', 'de', 'ja', 'fr', 'zh-TW', 'es'],
	'dname': ['English', 'Italiano', 'Deutsch', '日本語', 'Français', '廣東話', 'Español'],
	'name':['English', 'Italian', 'German', 'Japanese', 'French', 'Cantonese', 'Spanish'],
	'color':['red', 'purple', 'black', "#211790", 'blue', 'green', 'brown']
}

def main(page: ft.Page):
	"""basic settings"""
	page.title = "Warren's app"
	page.window_width = 108*6 #desktop app only
	page.window_height = 135*6 #desktop app only
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.bgcolor='white'

	"""events"""
	
	def items(count):
		"""create containers that hold all the languages"""
		items = []
		for i in range (0, count):
			items.append(
				ft.Container(
					content = ft.TextField(label=lang['dname'][i]),
					alignment = ft.alignment.center,
					width = 300,
					height = 70,
					bgcolor = lang['color'][i],
					border_radius = ft.border_radius.all(5),
					padding =20,
					margin=10,
					gradient = ft.LinearGradient(
						begin=ft.alignment.top_center, 
						end=ft.alignment.bottom_center,
						colors=[lang['color'][i], ft.colors.YELLOW ]
						)
					)
				)
		return items

	"""elements"""
	container = ft.Column(spacing=0, controls=items(len(lang['code'])))
	main_container = ft.Container(content=container, bgcolor='Black', border_radius=20)

	page.update()

	"""layout"""
	page.add(main_container)

ft.app(target=main)