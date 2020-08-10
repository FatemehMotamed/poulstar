from models import *
from settings import Session, session
from vehicle_form import VehicleForm
from tkinter import *
from form_helper import FormHelper
from datetime import date, datetime


class AirplaneForm(VehicleForm):
    def __init__(self, frame_name, window,model=None):
        super().__init__(frame_name, window)
        self.model=Airplane()
        self.model_name=Airplane
        self.cabin_classes = ["Economy", "Business", "First Class"]
        self.cabin_class = StringVar()
        self.cabin_class.set("Economy")

    def register_submit(self):
        self.model.name = self.name_entry.get()
        self.model.capacity = self.capacity_entry.get()
        self.model.company = self.company_entry.get()
        self.model.model = self.model_entry.get()
        self.model.allowed_cargo = self.capacity_entry.get()
        self.model.class_cabin = self.cabin_class.get()
        session = Session()
        session.add(self.model)
        session.commit()


    def calculate_finish_price(self,price,ticket_date):
        f = FormHelper()
        data = f.read_json()
        distance_date=self.day_distance(ticket_date)
        if distance_date<7:
            inc=(price * 20) / 100
            price=price+inc
        for item in data:
            if item['number'] > 0:
                if item['age'] == "Children (2-12 years)":
                    item['finish_price'] = price / 2
                elif item['age'] == "Baby (-2 years)":
                    item['finish_price'] = (price * 20) / 100
                else:
                    item['finish_price']=price

        f.write_json(data)


