from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    creation_date = Column(Text)
    body = Column(Text)


Index('entries', Entry.title, unique=True, mysql_length=255)
