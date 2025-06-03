import reflex as rx
import reflex_local_auth
from rxconfig import config
#
from .backend.state import State
from .ui.base import base_page
from . import blog, pages, navigation, contact
from .auth.pages import (
    my_login_page,
    my_signup_page,
    my_logout_page,
)
from .auth.state import SessionState

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


"""
reflex lcal auth pages
"""
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    my_signup_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)
app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout",
)

"""
my pages
"""
#app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
#app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
app.add_page(
    pages.protected_page,
    route="/protected",
    on_load=SessionState.on_load)
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(blog.blog_post_list_page,
             route=navigation.routes.BLOG_POSTS_ROUTE,
             on_load=blog.BlogPostState.load_posts)
app.add_page(blog.blog_post_add_page,
             route=navigation.routes.BLOG_POST_ADD_ROUTE)
app.add_page(blog.blog_post_detail_page,
             route="/blog/[blog_id]",
             on_load=blog.BlogPostState.get_post_detail)
app.add_page(blog.blog_post_edit_page,
             route="/blog/[blog_id]/edit",
             on_load=blog.BlogPostState.get_post_detail)
app.add_page(contact.contact_entries_list_page,
             route=navigation.routes.CONTACT_ENTRIES_ROUTE,
             on_load=contact.ContactState.list_entries)
