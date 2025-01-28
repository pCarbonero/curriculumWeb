import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.hstack(
                rx.text('Datos de contacto'),
            width="600px",
        )
        )
    )