import flet as ft
from time import sleep
from pyjyutping import jyutping as jtc 
from tabulate import tabulate as tb 
from tabulate import tabulate_formats
import re 
from googletrans import Translator
from flet import colors


#pattern to split words
pat = "[-a-zA-Z0-9]+[\S]|[,:'?!.]"

"""translator object"""
trans = Translator()

"""backend setting """
title_txt = "Warren's Translator"

lang = {
    'name': ['English', 'Italian', 'German', 'French', 'Japanese', 'Chinese', 'Spanish'],
    "code": ['en', 'it', 'de', 'fr', 'ja', 'zh-CN', 'es'],
    "color": ['red','purple', 'black', 'light blue', 'dark blue', 'green', 'brown'],
    "dname": ['English','Italiano', 'Deutsch', 'Français', '日本語', '廣東話', 'Español']
}


def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.window_width = 600

    def get_result(e):
        eng_trans.value = trans.translate(src_text.value , dest='en').text
        bot_list = re.findall(pat, src_text.value)
        top_list = [ trans.translate(bot_list[i], dest='en').text  for i in range(len(bot_list))]
        table = [top_list, bot_list]
        result = tb(table, tablefmt='tsv')
        result_txt.value = result

        src_lang = trans.detect(src_text.value).lang
        src_lang_idx = lang['code'].index(src_lang)
        result_txt.label = lang['dname'][src_lang_idx]

        page.update()

    eng_trans = ft.Text()


    # result_txt = ft.Text()
    result_txt = ft.TextField(label='Result',multiline=True, text_align='right')
    src_text = ft.TextField(label='Enter Text', on_change=get_result)



    """translation result"""    
    
    """layout"""
    page.add(src_text, eng_trans, result_txt)
    

# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)
