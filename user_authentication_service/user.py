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
    email = Column(String, null=False)
    hashed_password = Column(String, null=False)
    session_id = Column(String)
    reset_token = Column(String)

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))