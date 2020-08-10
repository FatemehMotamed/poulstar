from models import Buss
from settings import Session
from vehicle_form import VehicleForm
from tkinter import *
from form_helper import FormHelper

class BussForm(VehicleForm):
    def __init__(self, frame_name, window, model=None):
        super().__init__(frame_name, window)
        self.model = Buss()
        self.model_name = Buss
        self.cabin_classes = ["‌Bed Buss", "Half-Bed Buss"]
        self.cabin_class = StringVar()
        self.cabin_class.set("‌Bed Buss")

    def register_submit(self):
        self.model.name = self.name_entry.get()
        self.model.capacity = self.capacity_entry.get()
        self.model.company = self.company_entry.get()
        self.model.class_cabin = self.cabin_class.get()
        self.model.model = self.model_entry.get()

        session = Session()
        session.add(self.model)
        session.commit()

    def create_register_form(self):
        self.vehicle_frame = Frame(self.frame_name, pady=10)
        self.vehicle_frame.grid(row=8, column=0, columnspan=40, sticky="NWES", pady=10)

        name_label = Label(self.vehicle_frame, text='Name')
        name_label.grid(row=0, column=0)

        self.name_entry = Entry(self.vehicle_frame)
        self.name_entry.grid(row=0, column=1)

        capacity_label = Label(self.vehicle_frame, text='Capacity')
        capacity_label.grid(row=0, column=2, padx=2)

        self.capacity_entry = Entry(self.vehicle_frame)
        self.capacity_entry.grid(row=0, column=3)

        company_label = Label(self.vehicle_frame, text='Company')
        company_label.grid(row=0, column=4, padx=2)

        self.company_entry = Entry(self.vehicle_frame)
        self.company_entry.grid(row=0, column=5)

        self.exclusive_frame.grid(row=9, column=0, columnspan=40, sticky="NWES", pady=5)

        model_label = Label(self.exclusive_frame, text='Model')
        self.model_entry = Entry(self.exclusive_frame)

        model_label.grid(row=1, column=0, padx=2)
        self.model_entry.grid(row=1, column=1)

        class_lable = Label(self.exclusive_frame, text="Class")
        class_lable.grid(row=1, column=2, sticky="WE")
        class_box = OptionMenu(self.exclusive_frame, self.cabin_class, *self.cabin_classes)
        class_box.grid(row=1, column=3, sticky="WE")

        self.vehicle_button = Button(self.exclusive_frame, text="Submit", font=("Times", 10),command=self.register_submit)
        self.vehicle_button.grid(row=8, column=2, columnspan=3, sticky="E", padx=100, pady=20)

    def calculate_finish_price(self,price,ticket_date):
        f = FormHelper()
        data = f.read_json()
        for item in data:
            if item['number'] > 0:
                if item['age'] == "Children (2-12 years)":
                    item['finish_price'] = price / 2
                elif item['age'] == "Baby (-2 years)":
                    item['finish_price'] = 0
                else:
                    item['finish_price']=price
        f.write_json(data)