#!/usr/bin/env python3
'''
    User authentication service module for database
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    '''class User'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)
