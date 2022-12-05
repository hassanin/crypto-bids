# coding: utf-8
from sqlalchemy import Column, Integer, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Person(Base):
    __tablename__ = 'person'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column(Text)
    age = Column(Integer)
