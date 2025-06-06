import reflex as rx
import reflex_local_auth
#
from . import state
from .. import navigation
from ..ui.base import base_page
from ..models import BlogPostModel
#
#
def blog_post_detail_link(child: rx.Component, post: BlogPostModel):
    if post is None:
        return rx.fragment(child)
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    return rx.link(
        child,
        rx.text("by ", post.userinfo.email),
        href=post_detail_url
    )

def blog_post_list_item(post: BlogPostModel) -> rx.Component:
    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            post
        )
    )

@reflex_local_auth.require_login
def blog_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="5"),
            rx.link(
                rx.button("New Post"),
                href=navigation.routes.BLOG_POST_ADD_ROUTE,
            ),
            rx.foreach(state.BlogPostState.posts, blog_post_list_item),
            spacing="5",
            min_height="85vh",
            align="center",
        )
    )