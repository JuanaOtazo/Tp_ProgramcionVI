import flet as ft

def main(page: ft.Page):
    page.title = "Lista de compras"
    page.window_width = 600  # Cambié el ancho a 600
    page.window_height = 400

    new_task = ft.TextField(
        hint_text="¿Qué necesitas comprar?",
        width=300,
        border=ft.InputBorder.OUTLINE,
        border_radius=10,
        filled=True,
        fill_color=ft.colors.BLACK,  # Usar un color 
        hint_style=ft.TextStyle(color=ft.colors.GREY, italic=True),
        text_style=ft.TextStyle(font_family="Verdana", size=14, weight=ft.FontWeight.NORMAL)
        
    )

    def add_clicked(e):
        if new_task.value:
            tasks_container.controls.append(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            page.update()
    
    def delete_clicked(e):
        tasks_container.controls = [task for task in tasks_container.controls if not isinstance(task, ft.Checkbox) or not task.value]
        page.update()

    def modify_clicked(e):
        for task in tasks_container.controls:
            if isinstance(task, ft.Checkbox) and task.value:
                task.label = new_task.value
                task.update()
        new_task.value = ""
        new_task.focus()
        page.update()

    tasks_container = ft.Column()

    # Crear el encabezado con un color de fondo y tamaño de letra
    header = ft.Container(
        bgcolor=ft.colors.BLUE,
        height=50,
        content=ft.Row(
            [
                ft.Text("Bienvenidos a la App de Lista de Compras", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, font_family="Times New Roman")
            ],
            alignment="center"
        )
    )

    # Crear un contenedor principal para toda la aplicación
    app_container = ft.Container(
        expand=True,
        content=ft.Stack([
            ft.Container(
                expand=True,
                image_src="C:\\Users\\juani\\Desktop\\pg6\\fondo.png",
                image_fit=ft.ImageFit.COVER,
            ),
            ft.Container(
                content=ft.Column([
                    header,
                    ft.Divider(height=10),
                    ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)]),
                    ft.Row([ft.ElevatedButton("Eliminar", on_click=delete_clicked), ft.ElevatedButton("Modificar", on_click=modify_clicked)]),
                    tasks_container
                ], alignment="center", spacing=10)
            )
        ])
    )

    page.add(app_container)

ft.app(target=main)
