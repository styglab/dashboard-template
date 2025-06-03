import reflex as rx
#
from ..ui.base import base_page
from . import forms
from .state import BlogEditFormState
#
#
# class EditExampleState(rx.State):
#     title: str = "Hello World"
#     content: str = "This is my blog post"
    
#     def handle_submit(self, form_data):
#         print(form_data)
    
#     def handle_content_change(self, value):
#         self.content = value


def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.vstack(
            rx.heading("Editing ", post.title, size="5"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                ),
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width='75vw'
                ),
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width='95vw'
                ),
            ),  
            spacing="5",
            min_height="95vh",
            align="center",
    )
    return base_page(my_child)

