from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

try:
    engine = create_engine(
        'mysql+mysqlconnector://poulstar:poulstar@localhost:3306/ticket_reservation')
    Base = declarative_base()

    Session = sessionmaker(bind=engine)


except:
    print("Connect to database failed")

finally:
    print("Connect to database successful")