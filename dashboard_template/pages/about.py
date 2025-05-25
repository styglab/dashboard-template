import reflex as rx
#
from ..ui.base import base_page
from .. import navigation


@rx.page(route=navigation.routes.ABOUT_US_ROUTE)
def about_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "This is about page.",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            id="my-child",
    )
    return base_page(my_child)



