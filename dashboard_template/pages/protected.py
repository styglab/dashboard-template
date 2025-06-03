import reflex as rx
import reflex_local_auth
#
from ..ui.base import base_page
from .. import navigation
#
#
@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Protect Page", size="9"),
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



