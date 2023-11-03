from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv( 'DATABASE_URL',
    'mysql+mysqlconnector://admin:myCloudTec10@cloudevtec.cutenzlzct6y.us-east-1.rds.amazonaws.com:3306/cloudtecrecords')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
