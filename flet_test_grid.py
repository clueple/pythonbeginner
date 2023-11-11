import flet as ft 
from flet import TextField, GridView, Page, Column, Row, ElevatedButton, Container
from nltk.tokenize import word_tokenize as wt 
from deep_translator import GoogleTranslator as gt 


"""backend stuff"""

"""main app"""
def main(page:Page):

	"""theme settings"""

	"""events"""
	def tok_input1(e):
		try:
			rg2.clean()
			trans_txt = gt(source='auto', target='fr').translate(input1.value)
			tok_txt = wt(trans_txt)
			num_tok = len(tok_txt)
			rg2.max_extent= page.window_width / num_tok

			for i in range(num_tok):
				rg2.controls.append(
					Container(
						TextField(value=tok_txt[i]),
						alignment= ft.alignment.center,
						# bgcolor=ft.colors.BLUE_100,
						border=ft.border.all(1, ft.colors.AMBER_400),
						border_radius=ft.border_radius.all(5),
						)
					)
			page.update()
		except:
			rg2.controls.append(
				TextField(value='Please enter text in Source Text Box')
				)

		

	"""elements"""
	input1 = TextField(label='Source_Text', value='Enter your text here')
	# rg2 is the result in grid format
	rg2 = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
	# btn_rg3 is the ElevatedButton to return the tokenized sentence translated from input1
	btn_rg3 = ElevatedButton('Tokenize', on_click=tok_input1)


	"""layout"""
	page.add(
		Column(
			controls=[
			Row(controls=[input1, btn_rg3]),
			Row(controls=[rg2])
			]
			)
		)

"""run the flet app"""
if __name__ == '__main__':
    ft.app(target=main)
