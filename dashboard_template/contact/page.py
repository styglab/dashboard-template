import reflex as rx
#
from .. import navigation
from ..ui.base import base_page
from . import form, state, model
#
#
def contact_entry_list_item(contact: model.ContactEntryModel) -> rx.Component:
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.created_at),
        rx.text(contact.message),
        padding='1em'
    )

def contact_entries_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            min_height="85vh",
            align="center",
        )
    )

def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            #rx.text(ContactState.timeleft_label),
            rx.cond(state.ContactState.submit_tf, state.ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width='50vw'
                ),
            ),
            rx.tablet_only(
                rx.box(
                    form.contact_form(),
                    width='75vw'
                ),
            ),
            rx.mobile_only(
                rx.box(
                    form.contact_form(),
                    width='95vw'
                ),
            ),  
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            #id="my-child",
    )
    return base_page(my_child)


