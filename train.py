import models
from settings import Session
from vehicle import Vehicle


class Train(Vehicle):
    def __init__(self,name,capacity,company,hall_type, cupe_capacity, speed, class_cabin):
        super().__init__(name,capacity,company)
        self.hall_type=hall_type
        self.class_cabin=class_cabin
        self.speed=speed
        self.cupe_capacity=cupe_capacity

    def register(self):
        session = Session()
        try:
            device = models.Vehicle(self.name, self.capacity, self.company)
            train = models.Train(self.hall_type, self.cupe_capacity,self.speed,self.class_cabin,device)
            session.add(train)
            session.add(device)
            session.commit()
        except:
            print("register is failed")
        finally:
            print("register is complete")
            session.close()