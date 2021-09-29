import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#############################
#     USO EN DESARROLLO     #
#############################
'''
os.environ['MYSQL_HOST'] = "192.168.3.250"
os.environ['MYSQL_USER'] = "user"
os.environ['MYSQL_PASS'] = "password"
os.environ['MYSQL_DB'] = "db"
'''
###################################

host = os.environ['MYSQL_HOST']
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASS']
db_name = os.environ['MYSQL_DB']

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" + user + ":" + password + "@" + host + "/" + db_name

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

