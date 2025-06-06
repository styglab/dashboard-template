import reflex as rx
#
from .. import navigation
from ..articles.list import article_public_list_component
#
#
def landing_page() -> rx.Component:
    return rx.vstack(
            #rx.theme_panel(default_open=True),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.divider(),
            rx.heading("Recent Articles", size="5"),
            article_public_list_component(columns=1, limit=1),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            id="my-child",
    )