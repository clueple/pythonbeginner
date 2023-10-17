import flet as ft
from flet import Page, TextField, Container, Row, Column, ElevatedButton
from deep_translator import GoogleTranslator as gt

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

	"""create events"""

	"""create elements"""
	element1 = TextField(label="element 1", multiline=True)
	element2 = TextField(label="element 2")
	element3 = ElevatedButton(text = "Get Result")

	"""design layout"""
	page.add(
		Container(
			content=Column(
				controls=[
				element1,
				element2,
                element3
				]
				)
			)
		)

# app(target=main, view=WEB_BROWSER)
if __name__ == '__main__':
    ft.app(target=main)
