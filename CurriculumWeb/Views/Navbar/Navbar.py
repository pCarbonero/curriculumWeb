import reflex as rx
from CurriculumWeb.routes import *

def barra_de_navegacion() -> rx.Component:
    return rx.hstack(
        rx.link("Home", href=Ruta.INDEX.value, height="50px"),
        rx.link("Curriculum", href=Ruta.CURRICULUM.value, height="50px") 
    )