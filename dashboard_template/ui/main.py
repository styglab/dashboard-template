import reflex as rx

def main_page(child: rx.Component, *args):
    return rx.fragment(
        rx.box(
            child,
            padding="0em",
            width="100%",
            id="my-content-box",
        ),
        id="my-main-container",
    )
    
