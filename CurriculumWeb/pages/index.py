import reflex as rx

from CurriculumWeb.Views.Headre.header import header
from CurriculumWeb.Views.Navbar.Navbar import barra_de_navegacion
from rxconfig import config
from CurriculumWeb.routes import Ruta
from CurriculumWeb.Views.IndexButtons.Buttons import buttons
from CurriculumWeb.Views.Footer.Footer import footer

@rx.page(
    route = Ruta.INDEX.value,
    title = "Pagina principal"
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        barra_de_navegacion(),
        header(),
        buttons(),
        footer(),
        align='center',
        spacing='3'
    )