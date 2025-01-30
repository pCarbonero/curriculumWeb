import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="https://media.licdn.com/dms/image/v2/D4D03AQF4y-Ajzh4VVw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1729798941612?e=2147483647&v=beta&t=NF8yz6R1LU60rrcTI-iGTWAsTIDv79ATDoeYhtXH-sE",
                width="100px",
                height="auto",
                border_radius="10px 20px",
                border="5px solid #555",
            ),
            rx.text('Pablo Carbonero Almellones', font_size="40px", font_weight="bold", margin_top="20px", margin_bottom="20px")
        )
    )