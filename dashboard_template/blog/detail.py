import reflex as rx
#
from ..ui.base import base_page
from . import state
from .notfound import blog_post_not_found
#
#
def blog_post_detail_page() -> rx.Component:
    edit_tf = True
    edit_link = rx.link("Edit", href=f"{state.BlogPostState.blog_post_edit_url}")
    edit_link_el = rx.cond(
        edit_tf,
        edit_link,
        rx.fragment("")
    )
    my_child = rx.cond(
        state.BlogPostState.post,
        rx.vstack(
            rx.hstack(
                rx.heading("Blog post Detail", size="9"),
                edit_link_el,
                align='end',            
            ),
            rx.text("User info id ", state.BlogPostState.post.userinfo_id),
            rx.text("User info: ", state.BlogPostState.post.userinfo),
            rx.text("User: ", state.BlogPostState.post.userinfo.user),
            rx.text(state.BlogPostState.blog_post_id),
            rx.text(state.BlogPostState.post.title),
            rx.text(state.BlogPostState.post.publish_date),
            rx.text(state.BlogPostState.post.created_at),
            rx.text(state.BlogPostState.post.content,
                    white_space='pre-wrap'),
            spacing="5",
            min_height="85vh",
            align="center",
            ),
    blog_post_not_found()
    )
    return base_page(my_child)