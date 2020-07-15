from settings import Session,engine,Base
from vehicle import Vehicle
import models
class Airplane(Vehicle):
    def __init__(self,name,capacity,company,cargo,model):
        super().__init__(name,capacity,company)
        self.model=model
        self.allowed_cargo=cargo

    def register(self):
        session = Session()
        try:
            device=models.Vehicle(self.name,self.capacity,self.company)
            air = models.Airplane(self.allowed_cargo,self.model,device)
            session.add(air)
            session.add(device)
            session.commit()
        except:
            print("register is failed")
        finally:
            print("register is complete")
            session.close()

