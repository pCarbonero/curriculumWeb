import reflex as rx

def buttonLink(texto, url, color = "", is_external=False) -> rx.Component:
    return rx.link(
        rx.button(
            texto,
            height="50px",
            width="150px",
            bg = color
        ),
        href=url,
        is_external = is_external        
    )  
