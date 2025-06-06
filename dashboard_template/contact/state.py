import reflex as rx
import asyncio
from sqlmodel import select
from typing import List
#
from ..models import ContactEntryModel
from ..auth.state import SessionState
#
#
class ContactState(SessionState):
    form_data: dict = {}
    entries: List[ContactEntryModel] = []
    submit_tf: bool = False
    
    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name")
        return f"Thank you {first_name}".strip() + "!"
    
    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        if self.my_user_id is not None:
            data["user_id"] = self.my_user_id
        if self.my_userinfo_id is not None:
            data["userinfo_id"] = self.my_userinfo_id
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            # print(form_data)
            self.submit_tf = True
            yield
        await asyncio.sleep(2)
        self.submit_tf = False
        yield
        
    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            #print(entries)
            self.entries = entries

