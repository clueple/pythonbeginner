import flet as ft 
from flet import TextField, GridView, Page, Column, Row, ElevatedButton, Container, Markdown
from deep_translator import GoogleTranslator as gt
from nltk.tokenize import word_tokenize as wt 
import nltk


"""backend stuff"""
trans = gt(source='auto', target='en')

nltk.download('averaged_perception_tagger')

"""available language details"""
lang = {
    'name': ['English', 'Italian', 'German', 'French', 'Japanese', 'Chinese', 'Spanish'],
    "code": ['en', 'it', 'de', 'fr', 'ja', 'zh-CN', 'es'],
    "color": ['red','purple', 'black', 'light blue', 'dark blue', 'green', 'brown'],
    "dname": ['English','Italiano', 'Deutsch', 'Français', '日本語', '廣東話', 'Español']
}

"""element style"""
def txt_area_style() -> dict:
	return {
	'multiline': True,
	'expand': True,
	'border_color': ft.colors.TRANSPARENT,
	}

def md_style() -> dict:
	return {
	'value': 'whatever',
	'selectable': True,
	}

"""main app"""
def main(page:Page):
	# pass

	"""theme settings"""
	page.title = f"Warren's Markdown"
	page.vertical_alignment = 'center'
	page.window_height = 108*6
	page.window_width = 135*6
	page.horizontal_alignment = "stretch"
	page.vertical_alignment = "center" 
	page.theme_mode = 'dark'

	"""events"""
	def show_result(e):
		"""translate the input text area ('inp_txt') and display the result in the 'result' area"""
	
		#sentence list 1 - tokenize the input text, store it in a list, 's_list'
		s_list = wt(inp_txt.value)
		# translate each token in s_list and translate it into target language
		t_list = [i for idx, i in enumerate(s_list)]
		result.value = t_list
		page.update()

	"""elements"""
	inp_txt = TextField(**txt_area_style(), label='Source Text', hint_text='Enter sentence here to be translated', on_change=show_result)
	result = Markdown(**md_style())

	

	"""layout"""
	page.add(
		Row(
			controls=[
			#item 1  - input text area
			inp_txt, 
			#item 2 - vertical divider
			ft.VerticalDivider(color=ft.colors.YELLOW), 
			#item 3 - result
			Container(Column(controls=[result],scroll='hidden'), alignment=ft.alignment.top_left, expand=True) 
			],
			# other row properties
			expand=True,
			vertical_alignment=ft.CrossAxisAlignment.START
			)
		)


"""run the flet app"""
if __name__ == '__main__':
    ft.app(target=main)
