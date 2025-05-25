import reflex as rx
#
from ..components.navbar import navbar_buttons

def base_page(child: rx.Component, *args):
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
        id="my-base-container",
    )
    
