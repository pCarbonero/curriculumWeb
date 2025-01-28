import reflex as rx

from CurriculumWeb.Components.ButtonLink import buttonLink

def buttons() -> rx.Component:
    return rx.vstack(
        buttonLink("Linkedin", "https://www.linkedin.com/in/pablo-carbonero-almellones-2b63a422b", "#0060b5", True),
        buttonLink("GitHub", "https://github.com", "#ff7355", True),
        buttonLink("InfoJobs", "https://Infojobs.com", "#5cabe5", True),
        buttonLink("Curriculum", "", "#a155d3"),
        align="center"  
    )
