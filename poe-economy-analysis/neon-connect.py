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
CONNSTR = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{PROJECT}'

engine = create_engine(CONNSTR)

print(CONNSTR)