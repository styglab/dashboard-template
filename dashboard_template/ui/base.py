import reflex as rx
#
from ..components.navbar import navbar_buttons
from .dashboard import dashboard_page
from ..auth.state import SessionState
#
#
def hello_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar_buttons(),
        rx.box(
            child,
            padding="1em",
            width="100%",
            id="my-content-box",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )
    

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    is_logged_in = True

    return rx.cond(
        SessionState.is_authenticated,
        dashboard_page(child, *args, **kwargs),
        hello_page(child, *args, **kwargs),
    )

