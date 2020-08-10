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
    code = Column(String(10))
    register = relationship("Register", uselist=False ,back_populates='person')

    def __init__(self,fname=None,lname=None,phone=None,code=None):
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.code=code

# class Vehicle(Base):
#     __tablename__="vehicle"
#
#     id=Column(Integer(),primary_key=True)
#     name=Column(String(50))
#     capacity=Column(Integer())
#     company=Column(String(50))
#     ticket = relationship("Ticket", back_populates='vehicle')
#     airplane = relationship("Airplane", uselist=False ,back_populates='vehicle')
#     buss = relationship("Buss", uselist=False ,back_populates='vehicle')
#     train = relationship("Train", uselist=False ,back_populates='vehicle')
#
#     def __init__(self,name,capacity,company):
#         self.name=name
#         self.capacity=capacity
#         self.company=company


class Airplane(Base):
    __tablename__="airplane"

    id=Column(Integer(), primary_key=True)
    name = Column(String(50))
    capacity = Column(Integer())
    company = Column(String(50))
    allowed_cargo=Column(Integer())
    model=Column(String(50))
    class_cabin = Column(String(50))
    ticket = relationship("Ticket", back_populates='airplane')

    def __init__(self,name=None,capacity=None,company=None,allowed_cargo=None,model=None,class_cabin=None):
        self.name = name
        self.capacity = capacity
        self.company = company
        self.allowed_cargo=allowed_cargo
        self.model=model
        self.class_cabin=class_cabin

class Train(Base):
    __tablename__="train"

    id=Column(Integer(),primary_key=True)
    name = Column(String(50))
    capacity = Column(Integer())
    company = Column(String(50))
    class_type=Column(String(50))
    cupe_capacity=Column(String(50))
    speed=Column(String(50))
    class_cabin=Column(String(50))
    ticket = relationship("Ticket", back_populates='train')

    def __init__(self,name=None,capacity=None,company=None,class_type=None,cupe_capacity=None,speed=None,class_cabin=None,vehicle=None):
        self.name = name
        self.capacity = capacity
        self.company = company
        self.class_type_type=class_type
        self.cupe_capacity=cupe_capacity
        self.speed=speed
        self.class_cabin=class_cabin
        self.vehicle = vehicle

class Buss(Base):
    __tablename__="buss"

    id=Column(Integer(),primary_key=True)
    name = Column(String(50))
    capacity = Column(Integer())
    company = Column(String(50))
    class_cabin=Column(String(50))
    model=Column(String(50))
    ticket = relationship("Ticket", back_populates='buss')

    def __init__(self,name=None,capacity=None,company=None,class_cabin=None,model=None):
        self.name = name
        self.capacity = capacity
        self.company = company
        self.class_cabin=class_cabin
        self.model=model


class Ticket(Base):
    __tablename__="ticket"

    id=Column(Integer(),primary_key=True)
    origin=Column(String(50))
    destination=Column(String(50))
    time=Column(String(50))
    depart_date=Column(String(50))
    return_date=Column(String(50))
    basic_price=Column(Integer)
    airplane_id = Column(Integer, ForeignKey('airplane.id'))
    airplane= relationship("Airplane", back_populates='ticket')
    train_id = Column(Integer, ForeignKey('train.id'))
    train = relationship("Train", back_populates='ticket')
    buss_id = Column(Integer, ForeignKey('buss.id'))
    buss = relationship("Buss", back_populates='ticket')
    registers = relationship('Register', backref='ticket')

    def __init__(self,origin=None,destination=None,time=None,depart_date=None,return_date=None,basic_price=None,airplane=None,train=None,buss=None):
        self.origin=origin
        self.destination=destination
        self.time=time
        self.depart_date=depart_date
        self.return_date=return_date
        self.basic_price=basic_price
        self.airplane = airplane
        self.train = train
        self.buss = buss

class Register(Base):
    __tablename__ = "register"
    id = Column(Integer(), primary_key=True)
    finish_price = Column(Integer)
    register_time = Column(String(50))
    register_date = Column(String(50))
    ticket_id = Column(Integer, ForeignKey('ticket.id'))
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship('Person', back_populates='register')

    def __init__(self, finish_price, register_time, register_date, ticket,person):
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

