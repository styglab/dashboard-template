import reflex as rx
from reflex_local_auth.user import LocalUser
from datetime import datetime
from sqlmodel import Field, Relationship
import sqlalchemy
from typing import Optional, List
#
from . import utils
#
#
class UserInfo(rx.Model, table=True):
    email: str
    user_id: int = Field(foreign_key='localuser.id')
    user: LocalUser | None = Relationship() # LocalUser instance
    posts: List['BlogPostModel'] = Relationship(back_populates='userinfo')
    contact_entries: List['ContactEntryModel'] = Relationship(back_populates='userinfo')
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

class BlogPostModel(rx.Model, table=True): #BlogPost
    # user
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="posts")
    title: str
    content: str
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
    publish_active: bool = False
    publish_date: datetime = Field(
        default_factory=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
    )
    # publish_date
    # publish_time
    
class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    # user
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="contact_entries")
    first_name: str
    last_name: str | None = None
    email: str | None = None # same as Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_kst_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )






