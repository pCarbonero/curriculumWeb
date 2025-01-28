import reflex as rx

def barra_de_navegacion() -> rx.Component:
    return rx.hstack(
        rx.link("Home", height="50px"),
        rx.link("Curriculum", href="/curriculum", height="50px") 
    )