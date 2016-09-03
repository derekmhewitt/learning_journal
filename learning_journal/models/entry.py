# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import (
    Column,
    Index,
    Integer,
    DateTime,
    Unicode,
    UnicodeText,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(length=255))
    creation_date = Column(DateTime)
    body = Column(UnicodeText)


Index('entries_index', Entry.title, unique=True, mysql_length=255)
