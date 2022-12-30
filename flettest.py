import flet as ft 
from pyjyutping import jyutping as jtc 
import re 
# from tabulate import tabulate as tb
from prettytable import PrettyTable as pt
from googletrans import Translator
from prettytable import HEADER, ALL, FRAME


pat = r"[-a-zA-Z0-9]+|[\S]"
trans = Translator()

def main(page: ft.page):
	def show_element3(e):
		element3.value = f"You are writing this to element3: {e.control.value}"
		page.update()


	element1 = ft.Text('This is element 1')
	element2 = ft.TextField(label='This is element 2', on_change=show_element3)
	element3 = ft.Text()


	page.update()
	page.add(element1, element2, element3)


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
