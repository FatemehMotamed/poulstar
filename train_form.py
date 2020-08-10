from models import Train
from settings import Session
from vehicle_form import VehicleForm
from tkinter import *
from form_helper import FormHelper

class TrainForm(VehicleForm):
    def __init__(self, frame_name, window, model=None):
        super().__init__(frame_name, window)
        self.model = Train()
        self.model_name = Train
        self.cabin_classes = ['Coupe Train', 'Hall Train']
        self.cabin_class = StringVar()
        self.cabin_class.set("Coupe Train")

    def register_submit(self):
        self.model.name = self.name_entry.get()
        self.model.capacity = self.capacity_entry.get()
        self.model.company = self.company_entry.get()
        self.model.class_type = self.class_type.get()
        self.model.cupe_capacity = self.cupe_capacity.get()
        self.model.speed = self.speed.get()
        self.model.class_cabin = self.cabin_class.get()

        session = Session()
        session.add(self.model)
        session.commit()

    def select_ticket_exclusive_frame(self):
        t = self.ticket_type.get()
        if t == "one_way":
            self.return_button.config(state="disabled")
            self.return_entry.config(state="disabled")
            self.return_lable.config(state="disabled")
        elif t == "return":
            self.return_button.config(state="normal")
            self.return_entry.config(state="normal")
            self.return_lable.config(state="normal")


    def create_register_form(self):
        self.exclusive_frame.grid(row=9, column=0, columnspan=40, sticky="NWES", pady=5)

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

        cupe_capacitys = ['4 people', '6 people', '8 people']
        self.cupe_capacity = StringVar()
        self.cupe_capacity.set('4 people')

        speeds = ['High Speed', 'Normal']
        self.speed = StringVar()
        self.speed.set('Normal')

        class_types = ['5 star', '4 star', '3 star', 'Economy']
        self.class_type = StringVar()
        self.class_type.set('Economy')

        type_lable = Label(self.exclusive_frame, text="Cabin Class")
        type_box = OptionMenu(self.exclusive_frame, self.cabin_class, *self.cabin_classes)
        type_lable.grid(row=1, column=0, padx=2, pady=20)
        type_box.grid(row=1, column=1)

        cupe_capacity_label = Label(self.exclusive_frame, text="Cupe Capacity")
        cupe_capacity_label.grid(row=1, column=2, padx=10, sticky="WE")

        cupe_capacity_box = OptionMenu(self.exclusive_frame, self.cupe_capacity, *cupe_capacitys)
        cupe_capacity_box.grid(row=1, column=3, sticky="WE")

        speed_lable = Label(self.exclusive_frame, text="Speed")
        speed_lable.grid(row=1, column=4, sticky="WE")

        speed_box = OptionMenu(self.exclusive_frame, self.speed, *speeds)
        speed_box.grid(row=1, column=5, sticky="WE")

        class_lable = Label(self.exclusive_frame, text="Class Type")
        class_lable.grid(row=2, column=0, sticky="WE")

        class_box = OptionMenu(self.exclusive_frame, self.class_type, *class_types)
        class_box.grid(row=2, column=1, sticky="WE")

        self.vehicle_button = Button(self.exclusive_frame, text="Submit", font=("Times", 10),command=self.register_submit)
        self.vehicle_button.grid(row=2, column=2, columnspan=3, sticky="E", padx=100, pady=20)


    def calculate_finish_price(self,price,ticket_date):
        f = FormHelper()
        data = f.read_json()
        distance_date=self.day_distance(ticket_date)
        food=30000
        price=price+food
        if distance_date<7:
            inc=(price * 10) / 100
            price=price+inc
        for item in data:
            if item['number'] > 0:
                if item['age'] == "Children (2-12 years)":
                    item['finish_price'] = price / 2
                elif item['age'] == "Baby (-2 years)":
                    item['finish_price'] = (price * 10) / 100
                else:
                    item['finish_price']=price

        f.write_json(data)