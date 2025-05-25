import reflex as rx
import time
import asyncio
#
from ..ui.base import base_page
from .. import navigation
#
#
class ContactState(rx.State):
    form_data: dict = {}
    submit_tf: bool = False
    time_left: int = 5
    
    @rx.var
    def timeleft_label(self) -> str:
        if self.time_left < 1:
            return "No time left."
        return f"{self.time_left} seconds."
    
    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name")
        return f"Thank you {first_name}".strip() + "!"
    
    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(form_data)
        self.submit_tf = True
        yield
        await asyncio.sleep(2)
        self.submit_tf = False
        yield
    
    @rx.event    
    async def start_timer(self):
        while self.time_left > 0:
            await asyncio.sleep(1)
            self.time_left -= 1
            yield

@rx.page(
    on_load=ContactState.start_timer,
    route=navigation.routes.CONTACT_US_ROUTE
)
def contact_page() -> rx.Component:
    my_form = rx.vstack(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",
                        type='text',
                        width='100%',
                    ),  
                    width='100%',                  
                ),
                rx.input(
                    name="email",
                    placeholder='Your email',
                    type="email",
                    width='100%',
                ),
                rx.text_area(
                    name='message',
                    placeholder="Your message",
                    required=True,
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(ContactState.form_data.to_string()),
    )
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.text(ContactState.timeleft_label),
            rx.cond(ContactState.submit_tf, ContactState.thank_you, ""),
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
            #my_form,
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            #id="my-child",
    )
    return base_page(my_child)