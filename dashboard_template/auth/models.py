import reflex as rx
from reflex_local_auth.user import LocalUser
from datetime import datetime
from sqlmodel import Field, Relationship
import sqlalchemy
#
from .. import utils
#
#
class UserInfo(rx.Model, table=True):
    email: str
    user_id: int = Field(foreign_key='localuser.id')
    # user: LocalUser | None = Relationship() # LocalUser instance
    created_at: datetime = Field(
        default_factory=utils.timing.get_kst_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_kst_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )