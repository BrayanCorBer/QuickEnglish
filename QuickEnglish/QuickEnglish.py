import reflex as rx

# --- ESTADO (Lógica del formulario) ---
class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario."""
        self.form_data = form_data
        return rx.window_alert(f"¡Mensaje enviado! Gracias {form_data['nombre']}")

# --- COMPONENTES DE UI ---

def navbar():
    """Barra de navegación con logo."""
    return rx.hstack(
        # Logo (usando un icono o imagen placeholder)
        rx.hstack(
            rx.icon(tag="graduation-cap", size=30, color="white"),
            rx.text("QuickEnglish", font_size="1.5em", font_weight="bold", color="white"),
            spacing="3",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Inicio", href="#", color="white", _hover={"color": "orange"}),
            rx.link("Planes", href="#planes", color="white", _hover={"color": "orange"}),
            rx.link("Contacto", href="#contacto", color="white", _hover={"color": "orange"}),
            spacing="5",
        ),
        width="100%",
        padding="1em 2em",
        background_color="#0EA5E9",  # Color primario
        position="sticky",
        top="0",
        z_index="999",
    )

def hero_banner():
    """Banner full width con foto de fondo."""
    return rx.box(
        rx.vstack(
            rx.heading("A tu ritmo y en tu tiempo", font_size="3em", color="white", text_align="center"),
            rx.text("Aprende el Inglés que necesitas para tus metas", font_size="1.2em", color="white"),
            rx.link(
                rx.button(
                    "Empezar Ahora",
                    background_color="orange",
                    color="white",
                    padding="1em 2em",
                    border_radius="full",
                    _hover={"background_color": "#e65100"}, # Naranja más oscuro
                ),
                href="#planes",
            ),
            spacing="4",
            align_items="center",
            justify_content="center",
            height="100%",
            background_color="rgba(0, 0, 0, 0.5)", # Overlay oscuro para legibilidad
        ),
        # Imagen de fondo (usando una de stock de Unsplash)
        background_image="url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80')",
        background_size="cover",
        background_position="center",
        width="100%",
        height="500px",
    )

def about_section():
    """Párrafo de información."""
    return rx.container(
        rx.heading("Sobre Nosotros", color="#0EA5E9", margin_bottom="1em"),
        rx.text(
            """Somos un instituto dedicado a la enseñanza práctica del idioma inglés.
            Nuestra metodología se centra en la conversación real y el uso de herramientas
            modernas para acelerar tu aprendizaje.""",
            font_size="1.1em",
            line_height="1.6",
            text_align="justify",
        ),
        padding="4em 2em",
    )

def plan_card(title, price, features, payment_link):
    """Componente reutilizable para las tarjetas de planes con link de pago."""
    return rx.box(
        rx.vstack(
            rx.heading(title, size="5", color="#0EA5E9"),
            rx.heading(price, size="7", color="orange"),
            rx.divider(margin_y="1em"),
            rx.vstack(
                *[rx.hstack(rx.icon(tag="check", color="green"), rx.text(feature, color="black")) for feature in features],
                align_items="start",
                width="100%"
            ),
            rx.link(
                rx.button("Elegir Plan", width="100%", margin_top="1em", background_color="orange", color="white"),
                href=payment_link,
                is_external=True,
                width="100%",
            ),
            spacing="3",
            align_items="center",
        ),
        border="1px solid #e2e8f0",
        padding="2em",
        border_radius="lg",
        shadow="lg",
        width=["100%", "30%"], # Responsivo: 100% en móvil, 30% en escritorio
        _hover={"transform": "scale(1.05)", "transition": "0.3s"},
    )

def plans_section():
    """Sección de 3 opciones de planes."""
    return rx.box(
        rx.heading("Nuestros Planes", text_align="center", color="#0EA5E9", margin_bottom="2em"),
        rx.flex(
            plan_card(
                "Convenios", 
                "$75.000/anual", 
                ["Para instituciones", "Acceso a plataforma", "Material digital"],
                "https://link-de-pago-convenios.com" # TODO: Reemplazar con el link real
            ),
            plan_card(
                "Inicios", 
                "$80.000/mensual", 
                ["2 clases semanales", "Acceso a plataforma", "Material digital"],
                "https://link-de-pago-inicios.com" # TODO: Reemplazar con el link real
            ),
            plan_card(
                "Refuerzos", 
                "$120.000/mensual", 
                ["2 Clases conversacionales", "Tutoría 1 a 1", "Preparación TOEFL"],
                "https://link-de-pago-refuerzos.com" # TODO: Reemplazar con el link real
            ),
            flex_direction=["column", "row"], # Columna en móvil, fila en escritorio
            gap="2em",
            justify="center",
            width="100%",
        ),
        id="planes",
        padding="4em 2em",
        background_color="#f7fafc",
    )

def contact_form():
    """Formulario de contacto rediseñado y prominente."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "¡Empieza tu viaje hoy!", 
                size="8", 
                color="#0EA5E9", 
                text_align="center",
                margin_bottom="0.5em"
            ),
            rx.text(
                "Déjanos tus datos y un asesor te contactará para crear tu plan personalizado.",
                font_size="1.2em",
                color="black",
                text_align="center",
                margin_bottom="2em",
                max_width="600px"
            ),
            rx.card(
                rx.form(
                    rx.vstack(
                        rx.box(
                            rx.text("Nombre Completo", font_weight="bold", margin_bottom="0.5em", color="black"),
                            rx.input(
                                placeholder="Ej: Juan Pérez", 
                                id="nombre", 
                                size="3", 
                                border_color="gray", 
                                background_color="white",
                                color="black",
                                border_radius="md",
                                width="100%"
                            ),
                            width="100%"
                        ),
                        rx.box(
                            rx.text("Correo Electrónico", font_weight="bold", margin_bottom="0.5em", color="black"),
                            rx.input(
                                placeholder="Ej: juan@email.com", 
                                id="email", 
                                type="email", 
                                size="3",
                                border_color="gray", 
                                background_color="white",
                                color="black",
                                border_radius="md",
                                width="100%"
                            ),
                            width="100%"
                        ),
                        rx.box(
                            rx.text("Cuéntanos tus metas", font_weight="bold", margin_bottom="0.5em", color="black"),
                            rx.text_area(
                                placeholder="Quiero mejorar mi speaking para el trabajo...", 
                                id="mensaje", 
                                border_color="gray", 
                                background_color="white",
                                color="black",
                                border_radius="md",
                                min_height="150px",
                                width="100%"
                            ),
                            width="100%"
                        ),
                        rx.button(
                            "Enviar Solicitud", 
                            type="submit", 
                            size="4",
                            background_color="orange", 
                            color="white", 
                            width="100%", 
                            margin_top="1em",
                            _hover={"background_color": "#e65100", "transform": "scale(1.02)"},
                            transition="0.2s"
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    on_submit=ContactState.handle_submit,
                    width="100%",
                ),
                padding="3em",
                width="100%",
                max_width="800px",
                background_color="white",
                box_shadow="0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
                border_radius="1.5em",
                border="1px solid #E2E8F0"
            ),
            align_items="center",
            width="100%",
            padding_y="5em",
            padding_x="2em",
        ),
        id="contacto",
        width="100%",
        background_color="white", 
    )

def footer_contact():
    """Banner sólido con información de contacto."""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("¿Tienes dudas? ¡Hablemos!", size="4", color="white", margin_bottom="0.5em"),
                rx.hstack(
                    rx.icon(tag="mail", color="white"),
                    rx.text("contacto@englishinstitute.com", color="white", font_weight="bold"),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon(tag="phone", color="white"),
                    rx.text("+57 300 123 4567 (WhatsApp)", color="white", font_weight="bold"),
                    spacing="2",
                ),
                spacing="3",
            ),
        ),
        background_color="#0EA5E9",
        padding="3em 1em",
        width="100%",
    )

# --- PÁGINA PRINCIPAL ---

def index():
    return rx.box(
        navbar(),
        hero_banner(),
        about_section(),
        plans_section(),
        contact_form(),
        footer_contact(),
        font_family="system-ui",
    )

# Configuración de la App
app = rx.App()
app.add_page(index, title="English Institute App")