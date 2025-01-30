import reflex as rx

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi3m0oFY2kO57TYU9ayw8oj1fwLKC3ALA5Qw&s",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Reflex",
                            size="7",
                            weight="bold",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "© 2024 Reflex, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="4",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%",
                ),
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
        padding="1em",  # Añade un poco de espacio para que no se vea apretado
        box_shadow="0 -2px 10px rgba(0, 0, 0, 0.1)",  # Sombra ligera arriba
    )