
import flet
from flet import Page, AppBar, TextField, Image, Divider, colors, Column, Container, ElevatedButton, Text, alignment, FontWeight, TextAlign, MainAxisAlignment, CrossAxisAlignment, FilledButton, ButtonStyle, MaterialState

list_contact = []

def test(page: Page):
    page.title= "Guess the price"
    # page.scroll = "adaptive"
    page.window_width = 800
    page.window_height = 800
    # page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER


    def btn_clicked(e):
        page.clean()

    page.appbar = AppBar(title=Text("[Guess the price] "), bgcolor=colors.BLACK, center_title=True, color=colors.WHITE)
    page.add(Text(
            "Luxurious furniture edition ",
            size=40,
            color=colors.BLACK,
            # bgcolor=colors.GREEN_700,
            weight=FontWeight.BOLD,
            italic=False,
            text_align= TextAlign.CENTER,
            # alignment= alignment.center
            # text_align= TextAlign.CENTER
            
            
        ))
    x = 0
    

    # Add a Divider below the AppBar
    page.add(Divider(height=1, color=colors.BLACK))
    page.add(Text(""))
    page.add(Text(""))
    page.add(Text(""))
    # page.add(Text(
    #         x,
    #         size=40,
    #         color=colors.BLACK,
    #         # bgcolor=colors.GREEN_700,
    #         weight=FontWeight.BOLD,
    #         italic=False,
            
    #         # alignment= alignment.center
    #         # text_align= TextAlign.CENTER
    #         text_align=TextAlign.RIGHT,
            
            
    # )
    
    # )

            

    # img = Image(src="/Users/mbm/Desktop/Xperiences_Flet/FigmaTry.png")

    register = TextField(label="pseudo", hint_text="enter a pseudonyme")
    

    content=ElevatedButton(text="Elevated Button in Container", on_click=btn_clicked, style= ButtonStyle(
        color= colors.WHITE,
        bgcolor=colors.BLACK,),

       
       
        
        )

    # submit_btn = FilledButton(text="Submit", width=700, height=100, icon="add")

    password = TextField(label="Password", password=True, can_reveal_password=True, hint_text="enter a password")

    page.add(
        Container(
            content=Column([

                # img,
                register,
                password,
                #   btn
                content,
                # submit_btn,
            ], spacing=20)
        )
    )

flet.app(target=test)



