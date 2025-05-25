import reflex as rx
#
from .. import navigation

class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"
    
    def handle_title_input_change(self, val):
        self.label = val
        
    def did_click(self):
        print("hello reflex!")
        return rx.redirect(navigation.routes.ABOUT_ROUTE)




