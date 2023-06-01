from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import getpass
import psycopg2

# Optional: tell psycopg2 to cancel the query on Ctrl-C
import psycopg2.extras; psycopg2.extensions.set_wait_callback(psycopg2.extras.wait_select)

USERNAME = "gstoltman"
PASSWORD = getpass.getpass('Password: ')
HOST = "ep-noisy-rice-787875.us-west-2.aws.neon.tech"
PORT = "5432"
PROJECT = "currency"
CONNSTR = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/neondb'

engine = create_engine(CONNSTR)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    league = Column(String)
    get = Column(String)
    pay = Column(String)
    value = Column(Float)

Base.metadata.create_all(engine)