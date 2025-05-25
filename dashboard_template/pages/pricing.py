import reflex as rx
#
from ..ui.base import base_page
from .. import navigation


@rx.page(route=navigation.routes.PRICING_ROUTE)
def pricing_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("prcing", size="9"),
            rx.text(
                "This is prcing page.",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            id="my-child",
    )
    return base_page(my_child)