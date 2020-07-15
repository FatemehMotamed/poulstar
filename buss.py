import models
from settings import Session
from vehicle import Vehicle


class Buss(Vehicle):
    def __init__(self,name,capacity,company,hall_type,class_cabin,model):
        super().__init__(name,capacity,company)
        self.model=model
        self.hall_type=hall_type
        self.class_cabin=class_cabin

    def register(self):
        session = Session()
        try:
            device = models.Vehicle(self.name, self.capacity, self.company)
            buss = models.Buss(self.hall_type, self.class_cabin,self.model,device)
            session.add(buss)
            session.add(device)
            session.commit()
        except:
            print("register is failed")
        finally:
            print("register is complete")
            session.close()