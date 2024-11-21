import flet as ft

def main(page: ft.Page):
    page.title = "Hello Flet"
    
    # Create a simple Text and Button UI
    def button_clicked(e):
        page.controls.append(ft.Text(f'Hello, {name_input.value}!'))
        page.update()

    # Input field
    name_input = ft.TextField(label="Enter your name")
    
    # Button with an event handler
    hello_button = ft.ElevatedButton(text="Say Hello", on_click=button_clicked)
    
    # Add the controls to the page
    page.controls.append(name_input)
    page.controls.append(hello_button)

    # Update the page
    page.update()

# Start the app with network access
ft.app(target=main, view="web_browser", host="172.31.96.1", port=1000)
