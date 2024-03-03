from flet import *

def main (page: Page):
    BG = '#041955'
    FWD = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'


    categories_card = Row(
        scroll= 'auto'       
    )

    categories = ['Business', 'Family', 'Friends']
    for category in categories:
        categories_card.controls.append(
            Container (
                border_radius=20,
                bgcolor=FWD, 
                width=170,
                height=110,                
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks', color= 'white'),
                        Text(category, color= 'white'),
                        Container(
                            width=160,
                            height=5,                
                            bgcolor='white12', 
                            border_radius=20,
                            padding=padding.only(right=50),
                                                          
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content = Column (
            controls = [
                Row(alignment='spaceBetween',
                    controls=[
                        Container(content= Icon(
                            icons.MENU, color='white')),
                            
                        Row(
                            controls=[                                
                                Icon(icons.SEARCH, color='white'),
                                Icon(icons.NOTIFICATIONS_OUTLINED, color='white')
                                ],
                            ),
                        ],
                    ),
                Container(height=20),
                Text(
                    value="What's up!",
                    color= 'white'
                ),
                Text(
                    value='CATEGORIES',
                    color= 'white'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20,),
                    content= categories_card
                ),
        ]
    )
)

    page_1 = Container() 
    page_2 = Row(
        controls = [
            Container(
                width = 400,
                height =850,
                bgcolor = FG,
                border_radius = 35,
                padding = padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content = Column (
                    controls = [
                        first_page_contents
                    ]
                )
            )
        ]
    )
    
    container = Container (
    width=400,
    height=850,
    bgcolor=BG,
    border_radius=35,
    content=Stack(
        controls = [
            page_1, 
            page_2 
        ]
    )
    )
    page.add(container)
    

app(target = main)