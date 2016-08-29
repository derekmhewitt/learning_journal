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
    name = Column(Text)
    date = Column(Text)
    content = Column(Text)


Index('my_index', Entry.name, unique=True, mysql_length=255)
