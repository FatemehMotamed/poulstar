from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
class Database():
    def __init__(self):
        try:
            self.engine = create_engine(
                'mysql+mysqlconnector://poulstar:poulstar@localhost:3306/ticket_reservation')
            self.Base = declarative_base()

            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        except:
            print("Connect to database failed")

        finally:
            print("Connect to database successful")


    def create_tables(self):
        # class Person(self.Base):
        #     __tablename__ = 'person'
        #
        #     id = Column(Integer(), primary_key=True)
        #     fname = Column(String(50))
        #     lname = Column(String(50))
        #     phone = Column(String(11))
        #     code = Column(String(10),primary_key = True)
        #     address = Column(String(500))
        #     register_ticket = relationship("register_ticket", back_populates="person")

        class Vehicle(self.Base):
            __tablename__="vehicle"

            id=Column(Integer(),primary_key=True)
            name=Column(String(50))
            capacity=Column(Integer())
            company=Column(String(50))
            type=Column(String(50))
            # ticket = relationship("Ticket", back_populates='vehicle')
            airplane = relationship("Airplane", uselist=False ,back_populates='vehicle')
            # buss = relationship("Buss", back_populates='vehicle')
            # train = relationship("Train", back_populates='vehicle')

        class Airplane(self.Base):
            __tablename__="airplane"

            id=Column(Integer(), primary_key=True)
            id_vehicle=Column(Integer(),ForeignKey("vehicle.id"))
            allowed_cargo=Column(Integer())
            model=Column(String(50))
            vehicle = relationship('Vehicle',back_populates='airplane')

        # class Train(self.Base):
        #     __tablename__="train"
        #
        #     id=Column(Integer(),primary_key=True)
        #     hall_type=Column(Integer)
        #     cupe_capacity=Column(Integer)
        #     speed=Column(String(50))
        #     star=Column(String(50))
        #     vehicle = relationship('Vehicle', back_populates='train')
        #
        # class Buss(self.Base):
        #     __tablename__="buss"
        #
        #     id=Column(Integer(),primary_key=True)
        #     type=Column(String(50))
        #     vip_type=Column(String(50))
        #     model=Column(String(50))
        #     vehicle = relationship('Vehicle', back_populates='buss')
        #
        # class Ticket(self.Base):
        #     __tablename__="ticket"
        #
        #     id=Column(Integer(),primary_key=True)
        #     class_travel=Column(String(50))
        #     inventory=Column(Integer)
        #     id_vehicle=Column(Integer,ForeignKey('vehicle.id'))
        #     origin=Column(String(50))
        #     destination=Column(String(50))
        #     time=Column(String(50))
        #     date=Column(String(50))
        #     basic_price=Column(Integer)
        #     vehicle= relationship("Vehicle", back_populates='ticket')
        #
        # class Register_ticket(self.Base):
        #     __tablename__ = "register_ticket"
        #
        #     id = Column(Integer(), primary_key=True)
        #     id_person = Column(Integer(),ForeignKey('person.id'))
        #     id_ticket = Column(Integer(),ForeignKey('ticket.id'))
        #     state = Column(String(50))
        #     ticket_code = Column(String(50))
        #     finish_price = Column(Integer)
        #     register_time = Column(String(50))
        #     register_date = Column(String(50))
        #     person = relationship("Person",back_populates="register_ticket")

        try:

            self.Base.metadata.create_all(self.engine)
        except:
            print("The creation of tables failed")

        finally:
            print("The creation of tables succssful")


Database().create_tables()

