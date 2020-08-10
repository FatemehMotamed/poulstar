from datetime import datetime, date
from tkinter import *

from sqlalchemy import inspect

# from form_helper import FormHelper
from form_helper import FormHelper
from models import *
from person_form import PersonForm
from settings import session


class VehicleForm():

    def __init__(self, frame_name=None, window=None,model=None):
        self.window = window
        self.frame_name = frame_name
        self.model=model
        self.model_name=""
        self.exclusive_frame = Frame(self.frame_name)

    def convert_data_to_dictionary(self,data):
        dic = {}
        i = 0
        for row in data:
            item = {c.key: getattr(row, c.key)
                    for c in inspect(row).mapper.column_attrs}
            dic.update({i: item})
            i = i + 1
        return dic

    # select all data
    def select_data(self):

        result = session.query(self.model_name).all()
        dic=self.convert_data_to_dictionary(result)
        return dic

    def select_vehicle_with_id(self,mdl,id):

        vehicle = session.query(mdl).filter(mdl.id == id).one()
        return vehicle

    def select_data_ticket(self):
        result=[]
        condition=""
        if self.model_name==Airplane:
            condition=self.model_name.id==Ticket.airplane_id
        elif self.model_name==Buss:
            condition = self.model_name.id == Ticket.buss_id
        elif self.model_name == Train:
            condition = self.model_name.id == Ticket.train_id

        for c, i in session.query(Ticket, self.model_name).filter(
                Ticket.origin==self.origin_city.get(),
                Ticket.destination==self.destination_city.get(),
                Ticket.depart_date==self.depart_entry.get(),
                Ticket.return_date==self.return_entry.get(),
                condition
        ).all():

            if not c in result and i.capacity>int(self.number_passenger_entry.get()) and i.class_cabin==self.cabin_class.get():
                result.append(c)

        tickets = self.convert_data_to_dictionary(result)

        return tickets

    def create_table(self):

        # self.table_frame = Frame(self.win)
        # self.table_frame.grid(row=1, column=0)

        self.table=FormHelper(self.window,self.result_frame)
        table_data = self.select_data_ticket()
        result=self.table.create_table(table_data)
        if result==0:
            self.result_label.set("Ticket not found")
            # self.win.withdraw()
            return 0
        else:
            self.result_label.set("")

        buy_btn=Button(self.result_frame,text="Buy",command=self.buy)
        buy_btn.grid(row=100,column=0)

    def day_distance(self,ticket_date):
        date_now = datetime.now()
        date_now = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
        date_now = date_now.split("-")
        ticket_date = ticket_date.split("-")
        ticket_date = date(int(ticket_date[0]), int(ticket_date[1]), int(ticket_date[2]))
        date_now = date(int(date_now[0]), int(date_now[1]), int(date_now[2]))
        delta = ticket_date - date_now
        return delta.days

    def bill(self,ticket,vehicle_info):
        f=FormHelper()
        data=f.read_json()
        total_price=0

        item_label=["Ticket info","Number of Traveller","Price","Total price"]

        item=["Path: "+ticket.origin+"-"+ticket.destination,"Date: " + ticket.depart_date,"Vehicle name: " + vehicle_info.name,"Company: " + vehicle_info.company,"Class: " + vehicle_info.class_cabin]

        for i in range(0,4):
            ticket_label=Label(self.buy_window,text=item_label[i],width=20,height=2,font=("Times", 12), fg="white",bg="blue")
            ticket_label.grid(row=i,column=0)

        for i in range(0,5):
            ticket_label = Label(self.buy_window, text=item[i],width=20,height=2,font=("Times", 10),bg="#D2FAF9")
            ticket_label.grid(row=0, column=i+1)

        j=1
        for i in data:
            total_price+=i["finish_price"]
            ticket_label = Label(self.buy_window, text=i["age"]+" : "+str(i["number"]), width=20, height=2, font=("Times", 10), bg="#D2FAF9")
            ticket_label.grid(row=1, column=j)

            ticket_label = Label(self.buy_window, text=i["finish_price"] , width=20, height=2,
                                 font=("Times", 10), bg="#D2FAF9")
            ticket_label.grid(row=2, column=j)
            j+=1

        ticket_label = Label(self.buy_window, text=total_price, width=20, height=2,
                             font=("Times", 10), bg="#A7F77B")
        ticket_label.grid(row=3, column=1)


    def buy(self):

        self.item_id = self.table.item_id
        self.buy_window=Toplevel()
        id_v=""

        ticket=self.select_vehicle_with_id(Ticket,self.item_id)

        if self.model_name==Airplane:
            id_v=ticket.airplane_id
        elif self.model_name==Train:
            id_v = ticket.train_id
        elif self.model_name==Buss:
            id_v = ticket.buss_id
        vehicle_info=self.select_vehicle_with_id(self.model_name,id_v)
        self.calculate_finish_price(ticket.basic_price,ticket.depart_date)
        self.bill(ticket,vehicle_info)
        p=PersonForm(None,self.buy_window,ticket)
        p.create_person_info_form(self.number_passenger_entry.get())

    def create_search_form(self):
        self.vehicle_radio = StringVar()
        self.vehicle_radio.set("airplane")

        citys = ['tehran', 'rasht', 'shiraz']
        self.origin_city = StringVar()
        self.origin_city.set("tehran")
        self.destination_city = StringVar()
        self.destination_city.set("tehran")

        form_fram = Frame(self.frame_name, pady=5)
        form_fram.grid(row=0, column=0, columnspan=40, sticky="NWES")

        origin_lable = Label(form_fram, text="Origin", font=("Times", 12), fg="blue")
        origin_lable.grid(row=0, column=0, padx=5)

        origin_box = OptionMenu(form_fram, self.origin_city, *citys)
        origin_box.grid(row=0, column=1)

        destination_lable = Label(form_fram, text="Destination", font=("Times", 12), fg="blue")
        destination_lable.grid(row=0, column=2, padx=5)

        destination_box = OptionMenu(form_fram, self.destination_city, *citys)
        destination_box.grid(row=0, column=3)

        number_passener_label = Label(form_fram, text="Travellers", font=("Times", 12), fg="blue")
        number_passener_label.grid(row=0, column=4, padx=10)

        self.number_passenger_entry = Entry(form_fram)
        self.number_passenger_entry.grid(row=0, column=5)

        number_passenger_button = Button(form_fram, text="Select", font=("Times", 10),
                                         command=lambda: FormHelper(self.window).travellers("show",
                                                                                            self.number_passenger_entry))
        number_passenger_button.grid(row=0, column=6, padx=3)


        self.ticket_type = StringVar()
        self.ticket_type.set("return")
        # cabin_classes = ["Economy", "Business", "First Class"]
        # cabin_class = StringVar()
        # cabin_class.set("Economy")
        # exclusive_frame = Frame(self.frame_name)
        # exclusive_frame.grid(row=1, column=0, columnspan=40, sticky="NWES", pady=20)

        self.exclusive_frame.grid(row=1, column=0, columnspan=40, sticky="NWES", pady=5)


        self.return_radio = Radiobutton(self.exclusive_frame, text="Return", variable=self.ticket_type, value="return",
                                        font=("Times", 12),
                                        command=lambda: FormHelper(self.window).radio_on_off(self.ticket_type,self.return_button,self.return_entry,self.return_lable))
        self.return_radio.grid(row=0, column=0)

        self.one_way_radio = Radiobutton(self.exclusive_frame, text="One Way", variable=self.ticket_type, value="one_way",
                                         font=("Times", 12), command=lambda: FormHelper(self.window).radio_on_off(self.ticket_type,self.return_button,self.return_entry,self.return_lable))
        self.one_way_radio.grid(row=0, column=1)

        class_label = Label(self.exclusive_frame, text="Cabin Class", font=("Times", 12), fg="blue")
        class_label.grid(row=0, column=2, padx=20)

        class_option = OptionMenu(self.exclusive_frame, self.cabin_class, *self.cabin_classes)
        class_option.grid(row=0, column=3)

        date_frame = Frame(self.exclusive_frame)
        date_frame.grid(row=2, column=0, columnspan=40, sticky="NWES",pady=10)

        depart_lable = Label(date_frame, text="Depart Date ", font=("Times", 12), fg="blue")
        depart_lable.grid(row=0, column=0, padx=5)

        self.depart_entry = Entry(date_frame)
        self.depart_entry.grid(row=0, column=1)

        depart_button = Button(date_frame, text="Select", font=("Times", 10), command=lambda: FormHelper(self.window).calendar(self.depart_entry))
        depart_button.grid(row=0, column=2, padx=5)

        self.return_lable = Label(date_frame, text="Return Date ", font=("Times", 12), fg="blue")
        self.return_lable.grid(row=0, column=3, padx=5)

        self.return_entry = Entry(date_frame)
        self.return_entry.grid(row=0, column=4)

        self.return_button = Button(date_frame, text="Select", font=("Times", 10),
                                    command=lambda: FormHelper(self.window).calendar(self.return_entry))
        self.return_button.grid(row=0, column=5, padx=5)

        search_button = Button(date_frame, text="Search", font=("Times", 10), command=self.create_table,width=30,height=2)
        search_button.grid(row=9, column=1, columnspan=3, sticky="NEWS", padx=100, pady=10)

        self.result_frame=Frame(self.frame_name)
        self.result_frame.grid(row=10,column=1)

        self.result_label=StringVar()
        result_lable = Label(self.result_frame, textvariable=self.result_label,width=80, font=("Times", 12), fg="red")
        result_lable.grid(row=0, column=0,columnspan=3,sticky="EW", padx=5)

    def create_register_form(self):

        # print(FormHelper().list_attribute(self.model))


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

        self.exclusive_frame.grid(row=9, column=0, columnspan=40, sticky="NWES",pady=5)
        model_label = Label(self.exclusive_frame, text='Model')
        self.model_entry = Entry(self.exclusive_frame)

        model_label.grid(row=1, column=0, padx=2)
        self.model_entry.grid(row=1, column=1)

        cargo_label = Label(self.exclusive_frame, text='Allowed Cargo')
        cargo_label.grid(row=1, column=2, padx=2)

        self.cargo_entry = Entry(self.exclusive_frame)
        self.cargo_entry.grid(row=1, column=3)

        class_label = Label(self.exclusive_frame, text="Cabin Class")
        class_label.grid(row=1, column=4, padx=20)

        class_option = OptionMenu(self.exclusive_frame, self.cabin_class, *self.cabin_classes)
        class_option.grid(row=1, column=5)

        self.vehicle_button = Button(self.exclusive_frame, text="Submit", font=("Times", 10),command=self.register_submit)
        self.vehicle_button.grid(row=8, column=1, columnspan=3, sticky="E", padx=100, pady=20)






