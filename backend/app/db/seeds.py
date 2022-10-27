#print('Please fill the seeds file')
# Let’s start with 100 users, 100 products, and 100 comments.
# connect to db
# get settings of the app first
import sys
import pathlib
from sqlalchemy import create_engine
import pandas as pd 

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from app.core.config import get_app_settings


SETTINGS = get_app_settings()
print(SETTINGS)

DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")

print(DATABASE_URL)

target_metadata = None
engine = create_engine(url=DATABASE_URL)

from peewee import *

pg_db = PostgresqlDatabase('anythink-market', user='postgres', password='postgres',
                           host='postgres-python', port=5432)



print(pg_db.execute())
# diy model stuff