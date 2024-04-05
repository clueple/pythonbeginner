import flet as ft
from flet import TextField, ListView, Page, ListTile, app, SearchBar

def main(page: Page):
    # Define the list of languages
    all_lang = ['English', 'Japanese', 'Cantonese', 'English Canadian']

    # Function to handle search bar input changes
    def handle_change(e):
        # Clear the current list view
        lv.controls.clear()
        # Filter and append languages that contain the search query
        search_query = e.control.value.lower()
        for lang in all_lang:
            if search_query in lang.lower():
                lv.controls.append(ListTile(title=ft.Text(lang), on_click=close_anchor, data=lang))
        # Update the list view to show the filtered results
        lv.update()

    # Function to handle selection from the list view
    def close_anchor(e):
        # Get the selected language
        selected_lang = e.control.data
        # Set the search bar text to the selected language
        ele2.value = selected_lang
        # Update the search bar to reflect the selected language
        ele2.update()

    # Create a list view for displaying the search results
    lv = ListView()

    # Create a search bar element
    ele2 = SearchBar(
        bar_hint_text="Type to search...",
        on_change=handle_change,
        controls=[lv]
    )

    # Add the search bar to the page
    page.add(ele2)

# Run the Flet app
if __name__ == '__main__':
    app(target=main)
