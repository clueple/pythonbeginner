import flet as ft 
from flet import TextField, GridView, Page, Column, Row, SearchBar, app, Container, Text

"""backend stuff"""

"""main app"""
def main(page:Page):
	pass

	""" backend """
	all_lang = ['English', 'Japanese', 'Cantonese','English Canadian']

	"""theme settings"""

	"""events"""
	def handle_change(e):
		ele3.value= e.data
		page.update()

	def close_anchor(e):
		text = e.control.data
		ele2.close_view(text)

	"""elements"""
	ele1 = TextField('Element1')
	ele2 = SearchBar(
		divider_color=ft.colors.AMBER,
		bar_hint_text='bar hint text',
		view_hint_text='view hint text',
		on_change = handle_change,
		controls=[ft.ListTile(title=Text(f"{i}"),on_click=close_anchor,data=i) for i in all_lang]
		)
	ele3= TextField('Element3')

	"""layout"""
	page.add(
		ele1,
		ele2,
		ele3
		)

"""run the flet app"""
if __name__ == '__main__':
    app(target=main)
