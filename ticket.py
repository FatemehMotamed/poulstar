from form_helper import FormHelper
from models import Ticket, Airplane,Buss,Train
from settings import session
from tkinter import *

from vehicle_form import VehicleForm


class TicketForm(VehicleForm):
    def __init__(self, frame_name, window, model=None):
        super().__init__(frame_name, window)
        self.model = Ticket()


    def create_table(self):
        self.table_frame.destroy()
        self.table_frame = Frame(self.win)
        self.table_frame.grid(row=1, column=0)
        self.model = Airplane
        if self.vehicle_type.get() == "airplane":
            self.model_name = Airplane
        elif self.vehicle_type.get() == "buss":
            self.model_name = Buss
        elif self.vehicle_type.get() == "train":
            self.model_name = Train

        # table_head = FormHelper().list_attribute(model)
        # print(table_head)

        self.table=FormHelper(self.win,self.table_frame)
        table_data = self.select_data()
        result=self.table.create_table(table_data)
        if result==0:
            self.win.withdraw()
        self.model_name=Ticket()


    def register_vehicle_id(self):

        self.item_id = self.table.item_id
        # self.item = self.table.item
        self.v_box.set(self.item_id)
        self.v_name.set(self.vehicle_type.get())
        self.win.withdraw()

    def select_vehicle(self):
        self.win=Toplevel()
        self.vehicle_type = StringVar()
        self.vehicle_type.set("airplane")
        select_frame = Frame(self.win)
        select_frame.grid(row=0, column=0)

        airplane_radio = Radiobutton(select_frame, text="Airplane", variable=self.vehicle_type, value="airplane",
                                     state="normal", font=("Times", 12), fg="blue",command=self.create_table)
        airplane_radio.grid(row=0,column=0)

        train_radio = Radiobutton(select_frame, text="Train", variable=self.vehicle_type, value="train",
                                  font=("Times", 12),
                                  fg="blue",command=self.create_table)
        train_radio.grid(row=0,column=1)

        bus_radio = Radiobutton(select_frame, text="Bus", variable=self.vehicle_type, value="buss",
                                font=("Times", 12),
                                fg="blue",command=self.create_table)
        bus_radio.grid(row=0,column=2)

        self.table_frame = Frame(self.win)
        self.table_frame.grid(row=1, column=0)
        btn=Button(self.win,text="Select",command=self.register_vehicle_id)
        btn.grid(row=50, column=0)

        self.create_table()


    def register_submit(self):

        if self.v_name.get()=="airplane":
            vehicle=self.select_vehicle_with_id(Airplane,self.item_id)
            self.model_name.airplane=vehicle
        elif self.v_name.get()=="train":
            vehicle = self.select_vehicle_with_id(Train, self.item_id)
            self.model_name.train = vehicle
        elif self.v_name.get()=="buss":
            vehicle = self.select_vehicle_with_id(Buss, self.item_id)
            self.model_name.buss = vehicle

        self.model_name.origin=self.origin_city.get()
        self.model_name.destination=self.destination_city.get()
        self.model_name.basic_price=self.basic_price_entry.get()
        self.model_name.depart_date=self.depart_entry.get()
        self.model_name.return_date=self.return_entry.get()
        self.model_name.time=self.time_entry.get()


        session.add(self.model_name)
        session.commit()

    def create_register_form(self):
        operator_frame = Frame(self.frame_name)
        operator_frame.grid(row=9, column=0, columnspan=40, sticky="NWES", pady=20)
        self.ticket_type = StringVar()
        self.ticket_type.set("return")


        self.return_radio = Radiobutton(operator_frame, text="Return", variable=self.ticket_type, value="return",
                                        font=("Times", 12),
                                        command=lambda: FormHelper(self.window).radio_on_off(self.ticket_type,self.return_button,self.return_entry,self.return_lable))
        self.return_radio.grid(row=0, column=0)

        self.one_way_radio = Radiobutton(operator_frame, text="One Way", variable=self.ticket_type,
                                         value="one_way",
                                         font=("Times", 12),command=lambda: FormHelper(self.window).radio_on_off(self.ticket_type,self.return_button,self.return_entry,self.return_lable))
        self.one_way_radio.grid(row=0, column=1)

        date_frame = Frame(operator_frame)
        date_frame.grid(row=2, column=0, columnspan=40, sticky="NWES", pady=20)

        depart_lable = Label(date_frame, text="Depart Date ", font=("Times", 12), fg="blue")
        depart_lable.grid(row=0, column=0, padx=5)

        self.depart_entry = Entry(date_frame)
        self.depart_entry.grid(row=0, column=1)

        depart_button = Button(date_frame, text="Select", font=("Times", 10),
                               command=lambda: FormHelper(self.window).calendar(self.depart_entry))
        depart_button.grid(row=0, column=2, padx=5)

        self.return_lable = Label(date_frame, text="Return Date ", font=("Times", 12), fg="blue")
        self.return_lable.grid(row=0, column=3, padx=5)

        self.return_entry = Entry(date_frame)
        self.return_entry.grid(row=0, column=4)

        self.return_button = Button(date_frame, text="Select", font=("Times", 10),
                                    command=lambda: FormHelper(self.window).calendar(self.return_entry))
        self.return_button.grid(row=0, column=5, padx=5)



        basic_price_lable = Label(operator_frame, text="Price", font=("Times", 12), fg="blue")
        basic_price_lable.grid(row=3, column=0, padx=5)

        self.basic_price_entry = Entry(operator_frame)
        self.basic_price_entry.grid(row=3, column=1)


        time_label = Label(operator_frame, text="Time", font=("Times", 12), fg="blue")
        time_label.grid(row=3, column=2, padx=5, pady=20)

        self.time_entry = Entry(operator_frame)
        self.time_entry.grid(row=3, column=3)

        times = ['AM', 'PM']
        time = StringVar()
        time.set('AM')
        time_option = OptionMenu(operator_frame, time, *times)
        time_option.grid(row=3, column=4)

        self.vehicle_radio = StringVar()
        self.vehicle_radio.set("airplane")

        citys = ['tehran', 'rasht', 'shiraz']
        self.origin_city = StringVar()
        self.origin_city.set("tehran")
        self.destination_city = StringVar()
        self.destination_city.set("tehran")

        origin_lable = Label(operator_frame, text="Origin", font=("Times", 12), fg="blue")
        origin_lable.grid(row=4, column=0, padx=10)

        origin_box = OptionMenu(operator_frame, self.origin_city, *citys)
        origin_box.grid(row=4, column=1)

        destination_lable = Label(operator_frame, text="Destination", font=("Times", 12), fg="blue")
        destination_lable.grid(row=4, column=2, padx=5)

        destination_box = OptionMenu(operator_frame, self.destination_city, *citys)
        destination_box.grid(row=4, column=3)

        vehicle_lable = Label(operator_frame, text="Vehicle id", font=("Times", 12), fg="blue")
        vehicle_lable.grid(row=5, column=0, sticky="WE")

        self.v_box=StringVar()
        vehicle_box = Entry(operator_frame,textvariable=self.v_box)
        vehicle_box.grid(row=5, column=1, sticky="W",pady=20)

        vehicle_select = Button(operator_frame, text="Select", font=("Times", 10),command=self.select_vehicle)
        vehicle_select.grid(row=5, column=2, padx=5, sticky="W")

        vehicle_name_lable = Label(operator_frame, text="Vehicle Type", font=("Times", 12), fg="blue")
        vehicle_name_lable.grid(row=5, column=3, sticky="WE")

        self.v_name = StringVar()
        vehicle_name = Entry(operator_frame, textvariable=self.v_name)
        vehicle_name.grid(row=5, column=4, sticky="W", pady=20)

        vehicle_button = Button(operator_frame, text="Submit", font=("Times", 10), command=self.register_submit)
        vehicle_button.grid(row=6, column=1, columnspan=3, sticky="E", padx=100, pady=20)




