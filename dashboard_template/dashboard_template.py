import reflex as rx
from rxconfig import config
#
from .backend.state import State
from .ui.base import base_page
from . import pages, navigation


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(rx.button("Go to about page"), href=navigation.routes.ABOUT_US_ROUTE),
            rx.input(
                default_value=State.label,
                on_change=State.handle_title_input_change,
                on_click=State.did_click),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            id="my-child",
    )
    return base_page(my_child)


app = rx.App()
app.add_page(index)
#app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
#app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)

