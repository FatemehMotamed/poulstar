import models
from settings import Session


class Ticket():
    def __init__(self,origin,destination,time,depart_date,return_date,basic_price,id_vehicle):
        self.origin = origin
        self.destination = destination
        self.time=time
        self.depart_date=depart_date
        self.return_date=return_date
        self.basic_price=basic_price
        self.id_vehicle=id_vehicle

    def register(self):
        session = Session()
        try:
            ticket=models.Ticket(self.origin,self.destination,self.time,
                                 self.depart_date,self.return_date,self.basic_price,self.id_vehicle)
            session.add(ticket)
        except:
            print("ticket is register")
        finally:
            print("ticket not register")


