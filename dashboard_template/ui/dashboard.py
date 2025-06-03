import reflex as rx
#
from ..components.sidebar import sidebar

def dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                rx.logo(),
                padding="1em",
                width="100%",
                id="my-content-box",
            ),
        ),
        # rx.color_mode.button(position="bottom-left"),
        id="my-base-container",
    )