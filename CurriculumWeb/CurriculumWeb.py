"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from CurriculumWeb.Views.Headre.header import header
from CurriculumWeb.Views.Navbar.Navbar import barra_de_navegacion
from CurriculumWeb.pages.curriculumPage import portfolio
from rxconfig import config
from CurriculumWeb.pages.index import index


class State(rx.State):
    """The app state."""

    ...





app = rx.App()
app.add_page(index)
app.add_page(portfolio)
app._compile()