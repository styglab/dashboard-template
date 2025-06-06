import reflex as rx
#
from ..ui.base import base_page
from . import state
from ..blog.notfound import blog_post_not_found
#
#
def article_detail_page() -> rx.Component:
    my_child = rx.cond(
        state.ArticlePublicState.post,
        rx.vstack(
            rx.hstack(
                rx.heading("Blog post Detail", size="9"),
                align='end',            
            ),
            rx.text("User info id ", state.ArticlePublicState.post.userinfo_id),
            rx.text("User info: ", state.ArticlePublicState.post.userinfo),
            rx.text("User: ", state.ArticlePublicState.post.userinfo.user),
            rx.text(state.ArticlePublicState.post_id),
            rx.text(state.ArticlePublicState.post.title),
            rx.text(state.ArticlePublicState.post.publish_date),
            rx.text(state.ArticlePublicState.post.created_at),
            rx.text(state.ArticlePublicState.post.content,
                    white_space='pre-wrap'),
            spacing="5",
            min_height="85vh",
            align="center",
            ),
    blog_post_not_found()
    )
    return base_page(my_child)