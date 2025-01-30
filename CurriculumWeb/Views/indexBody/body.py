import reflex as rx

def body() -> rx.Component:
    return rx.vstack(
         rx.center(
            rx.vstack(
                rx.text(
                    "Sobre mí", 
                    font_size="40px", 
                    font_weight="bold", 
                    margin_top="20px", 
                    margin_bottom="20px"
                ),
                rx.text(
                    """
                    Hola, soy Pablo Carbonero y nací en el 2003. 
                    Al terminar bachillerato y hacer selectividad decidí cursar un grado superior en 
                    Animación 3D, juegos y entornos interactivos en Campus Cámara de Comercio de Sevilla. 
                    En este grado aprendí muchas cosas como: modelado 3D, iluminación de entornos en 3D, 
                    animación tanto 3D como 2D y muchas otras cosas.
                    
                    Pero lo que más me gustó y en lo que más destaqué fue en el desarrollo de videojuegos 
                    con Unity y C#. Fue así como me di cuenta de que lo que de verdad me gustaba era el 
                    desarrollo de software.
                    
                    En las prácticas de este curso formé parte del equipo de programadores para el desarrollo 
                    de un videojuego actualmente publicado en Steam: "Mencía. A Never Was Tale", en la empresa 
                    Timber Films.
                    
                    Al terminar las prácticas y mi formación sabía que aún tenía mucho que aprender y por eso 
                    decidí cursar el grado superior en Desarrollo de Aplicaciones Multiplataforma.
                    
                    Durante mis estudios en DAM estoy aprendiendo tecnologías como .NET (MAUI, ASP.NET), C#, 
                    Python, Java, Kotlin (Android Studio, Jetpack Compose), SQL Server, JavaScript y Angular, 
                    además de arquitecturas de desarrollo como MVVM y MVC.
                    
                    Mis objetivos son seguir aprendiendo, poner en práctica mis capacidades en proyectos y 
                    demostrar mi potencial como desarrollador de software.""",
                    white_space="pre-wrap", 
                    font_size="16px",
                    line_height="1.5",
                ),
                width="900px",
            )
        )
)