# import flet as ft
# from flet import TextField, ListView, Page, ListTile, app, SearchBar,Text

# def main(page: Page):
#     # Define the list of languages
#     all_lang = ['English', 'Japanese', 'Cantonese', 'English Canadian']

#     # Function to handle search bar input changes
#     def handle_change(e):
#         # Clear the current list view
#         lv.controls.clear()
#         # Filter and append languages that contain the search query
#         search_query = e.control.value.lower()
#         for lang in all_lang:
#             if search_query in lang.lower():
#                 lv.controls.append(ListTile(title=ft.Text(lang), on_click=close_anchor, data=lang))
#         # Update the list view to show the filtered results
#         lv.update()

#     # Function to handle selection from the list view
#     def close_anchor(e):
#         # Get the selected language
#         selected_lang = e.control.data
#         # Set the search bar text to the selected language
#         ele2.close_view(selected_lang)
#         # Update the search bar to reflect the selected language
#         ele2.update()

#     # Create a list view for displaying the search results
#     lv = ListView()

#      # Populate the list view with all languages as default selection choices
#     for lang in all_lang:
#         lv.controls.append(ListTile(title=ft.Text(lang), on_click=close_anchor, data=lang))

#     # Create a search bar element
#     ele2 = SearchBar(
#         bar_hint_text="Type to search...",
#         on_change=handle_change,
#         controls=[lv]
#     )

#     # Add the search bar to the page
#     page.add(ele2)

# # Run the Flet app
# if __name__ == '__main__':
#     app(target=main)


from dataclasses import dataclass, field
import flet as ft
from flet import ListView, Page, ListTile, app, SearchBar, Text

@dataclass
class SearchableDropdown:
    items: list[str] = field(default_factory=list)
    lv: ListView = field(default_factory=ListView)
    search_bar: SearchBar = field(init=False)

    def __post_init__(self):
        self.search_bar = SearchBar(
            bar_hint_text="Type to search...",
            on_change=self.handle_change,
            controls=[self.lv]
        )
        self.populate_list_view()

    def populate_list_view(self):
        for item in self.items:
            self.lv.controls.append(ListTile(title=ft.Text(item), on_click=self.close_anchor, data=item))

    def handle_change(self, e):
        self.lv.controls.clear()
        search_query = e.control.value.lower()
        for item in self.items:
            if search_query in item.lower():
                self.lv.controls.append(ListTile(title=ft.Text(item), on_click=self.close_anchor, data=item))
        self.lv.update()

    def close_anchor(self, e):
        selected_item = e.control.data
        self.search_bar.close_view(selected_item)
        self.search_bar.update()

def main(page: Page):
    all_lang = ['English', 'Japanese', 'Cantonese', 'English Canadian']
    diff_list = ['abc','abcdef','def', 'xyz']
    searchable_dropdown = SearchableDropdown(all_lang)
    new_dropdown = SearchableDropdown(diff_list)

    page.add(
        searchable_dropdown.search_bar,
        new_dropdown.search_bar
        )

if __name__ == '__main__':
    app(target=main)
