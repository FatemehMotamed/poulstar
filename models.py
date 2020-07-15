from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from settings import Base,engine

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer(), primary_key=True)
    fname = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(11))
    code = Column(String(10),primary_key = True)
    address = Column(String(500))
    register = relationship("Register", uselist=False ,back_populates='person')

    def __init__(self,fname,lname,phone,code,address):
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.code=code
        self.address=address

class Vehicle(Base):
    __tablename__="vehicle"

    id=Column(Integer(),primary_key=True)
    name=Column(String(50))
    capacity=Column(Integer())
    company=Column(String(50))
    ticket = relationship("Ticket", back_populates='vehicle')
    airplane = relationship("Airplane", uselist=False ,back_populates='vehicle')
    buss = relationship("Buss", uselist=False ,back_populates='vehicle')
    train = relationship("Train", uselist=False ,back_populates='vehicle')

    def __init__(self,name,capacity,company):
        self.name=name
        self.capacity=capacity
        self.company=company


class Airplane(Base):
    __tablename__="airplane"

    id=Column(Integer(), primary_key=True)
    allowed_cargo=Column(Integer())
    model=Column(String(50))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    vehicle = relationship('Vehicle',back_populates='airplane')

    def __init__(self,allowed_cargo,model,vehicle):
        self.allowed_cargo=allowed_cargo
        self.model=model
        self.vehicle=vehicle



class Train(Base):
    __tablename__="train"

    id=Column(Integer(),primary_key=True)
    hall_type=Column(String(50))
    cupe_capacity=Column(String(50))
    speed=Column(String(50))
    class_cabin=Column(String(50))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    vehicle = relationship('Vehicle', back_populates='train')

    def __init__(self,hall_type,cupe_capacity,speed,class_cabin,vehicle):
        self.hall_type=hall_type
        self.cupe_capacity=cupe_capacity
        self.speed=speed
        self.class_cabin=class_cabin
        self.vehicle = vehicle
#
class Buss(Base):
    __tablename__="buss"

    id=Column(Integer(),primary_key=True)
    hall_type=Column(String(50))
    class_cabin=Column(String(50))
    model=Column(String(50))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    vehicle = relationship('Vehicle', back_populates='buss')

    def __init__(self,hall_type,class_cabin,model,vehicle):
        self.hall_type=hall_type
        self.class_cabin=class_cabin
        self.model=model
        self.vehicle = vehicle

class Ticket(Base):
    __tablename__="ticket"

    id=Column(Integer(),primary_key=True)
    class_travel=Column(String(50))
    inventory=Column(Integer)
    origin=Column(String(50))
    destination=Column(String(50))
    time=Column(String(50))
    depart_date=Column(String(50))
    return_date=Column(String(50))
    basic_price=Column(Integer)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle= relationship("Vehicle", back_populates='ticket')
    registers = relationship('Register', backref='ticket')

    def __init__(self,class_travel,inventory,origin,destination,time,depart_date,return_date,basic_price,vehicle):
        self.class_travel=class_travel
        self.inventory=inventory
        self.origin=origin
        self.destination=destination
        self.time=time
        self.depart_date=depart_date
        self.return_date=return_date
        self.basic_price=basic_price
        self.vehicle = vehicle

class Register(Base):
    __tablename__ = "register"
    id = Column(Integer(), primary_key=True)
    state = Column(String(50))
    ticket_code = Column(String(50))
    finish_price = Column(Integer)
    register_time = Column(Integer)
    register_date = Column(Integer)
    ticket_id = Column(Integer, ForeignKey('ticket.id'))
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship('Person', back_populates='register')

    def __init__(self, state, ticket_code, finish_price, register_time, register_date, ticket,person):

        self.state=state
        self.ticket_code=ticket_code
        self.finish_price=finish_price
        self.register_time=register_time
        self.register_date=register_date
        self.ticket=ticket
        self.person=person


class Make_TAbles():
    try:

        Base.metadata.create_all(engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        session = Session()
    except:
        print("The creation of tables failed")

    finally:
        print("The creation of tables succssful")


Make_TAbles()

