import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk

from airplane import Airplane
from buss import Buss
from train import Train


class Form():
    def __init__(self,frame_name,window,vehicle,user):
        self.frame_name=frame_name
        self.window=window
        self.vehicle=vehicle
        self.user=user
        self.traveller_dic = {
            1: {
                'age': 'Adults (12+ years)',
                'number': 1,
            },
    
            2: {
                'age': 'Children (2-12 years)',
                'number': 0,
            },
    
            3: {
                'age': 'Baby (-2 years)',
                'number': 0,
            }
    
        }
    def submit_form(self):
        name=self.name_entry.get()
        company=self.company_entry.get()
        capacity=self.capacity_entry.get()
        if self.vehicle=="airplane":
            model=self.model_entry.get()
            allowed_cargo=self.cargo_entry.get()
            a=Airplane(name,capacity,company,allowed_cargo,model)
            a.register()

        elif self.vehicle=="train" or self.vehicle=="buss":
            hall_type=self.type.get()
            class_cabin=self.cabin_class.get()

            if self.vehicle=="train":
                cupe_capacity=self.cupe_capacity.get()
                speed=self.speed.get()
                t=Train(name,capacity,company,hall_type,cupe_capacity,speed,class_cabin)
                t.register()

            elif self.vehicle=="buss":
                model = self.model_entry.get()
                b=Buss(name,capacity,company,hall_type,class_cabin,model)
                b.register()
    def ticket_submit(self):
        class_travel=self.cabin_class.get()
        inventory=self. inventory_entry.get()
        origin=self.origin_city.get()
        destination=self.destination_city.get()
        time=self.time_entry.get()
        depart_date=self.depart_entry.get()
        return_date=self.return_entry.get()
        basic_price=self.basic_price_entry.get()
        id_vehicle=self.vehicle_box.get()


    def create_logo(self):
        pass

    def set_default(self):
        date_now=datetime.datetime.now()
        return_date = date_now + datetime.timedelta(days=7)
        date_now_str = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
        date_return_str = "{}-{}-{}".format(return_date.year, return_date.month, return_date.day)
        self.depart_entry.insert(0, date_now_str)
        self.number_passenger_entry.insert(0, "1 people")
        if self.vehicle!="buss":
            self.return_entry.insert(0, date_return_str)

    def select_ticket_type_frame(self):
        t = self.ticket_type.get()
        if t == "one_way":
            self.return_button.config(state="disabled")
            self.return_entry.config(state="disabled")
            self.return_lable.config(state="disabled")
        elif t == "return":
            self.return_button.config(state="normal")
            self.return_entry.config(state="normal")
            self.return_lable.config(state="normal")

    def calendar(self,entry_name):
        date_now=datetime.datetime.now()

        def print_sel():
            if entry_name == "depart":
                date = cal.selection_get()
                self.depart_entry.delete(0, END)
                self.depart_entry.insert(0, date)
                top.destroy()
            else:
                date = cal.selection_get()
                self.return_entry.delete(0, END)
                self.return_entry.insert(0, date)
                top.destroy()

        top = Toplevel(self.window)

        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=date_now.year, month=date_now.month, day=date_now.day)

        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def travellers(self,btn):
        global traveller_win
        sum_traveller = 0
        if btn == "show":
            traveller_win = Toplevel(self.window)
            traveller_win.geometry("250x220")

            for i in range(1, 4):
                self.traveller_dic[i]['age_label'] = Label(traveller_win, text=self.traveller_dic[i]['age'], font=("Times", 12),
                                                      fg="blue", pady=20)
                self.traveller_dic[i]['age_label'].grid(row=i, column=0)

                arg = "m" + str(i)
                self.traveller_dic[i]['dec_button'] = Button(traveller_win, text="-",
                                                        command=lambda name=arg: self.travellers(name))
                self.traveller_dic[i]['dec_button'].grid(row=i, column=1)

                self.traveller_dic[i]['number_label'] = Label(traveller_win, text=self.traveller_dic[i]['number'])
                self.traveller_dic[i]['number_label'].grid(row=i, column=2, padx=10)

                arg = "p" + str(i)
                self.traveller_dic[i]['inc_button'] = Button(traveller_win, text="+",
                                                        command=lambda name=arg: self.travellers(name))
                self.traveller_dic[i]['inc_button'].grid(row=i, column=3)

            ok_button = Button(traveller_win, text="Ok", command=lambda: self.travellers("ok"))
            ok_button.place(x=100, y=180)

        elif btn[0] == "p":
            index = int(btn[1])
            if self.traveller_dic[index]['number'] < 20:
                self.traveller_dic[index]['number'] += 1
            self.traveller_dic[index]['number_label'].config(text=self.traveller_dic[index]['number'])

        elif btn[0] == "m":
            index = int(btn[1])
            if self.traveller_dic[index]['number'] > 0:
                self.traveller_dic[index]['number'] -= 1
            self.traveller_dic[index]['number_label'].config(text=self.traveller_dic[index]['number'])
        if btn == "ok":
            for key, value in self.traveller_dic.items():
                sum_traveller += value['number']
            num = str(sum_traveller) + " people"
            self.number_passenger_entry.delete(0, END)
            self.number_passenger_entry.insert(0, num)
            traveller_win.destroy()

    def create_search_form(self):

        citys = ['tehran', 'rasht', 'shiraz']
        self.origin_city = StringVar()
        self.origin_city.set("tehran")
        self.destination_city = StringVar()
        self.destination_city.set("tehran")
        self.ticket_type = StringVar()
        self.ticket_type.set("return")
        cabin_classes=[]
        cabin_class=""

        form_fram = Frame(self.frame_name, pady=10)
        form_fram.grid(row=8, column=0, columnspan=40, sticky="NWES", pady=10)

        origin_lable = Label(form_fram, text="Origin", font=("Times", 12), fg="blue")
        origin_lable.grid(row=0, column=0, padx=10)

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
                                         command=lambda: self.travellers("show"))
        number_passenger_button.grid(row=0, column=6, padx=3)

        type_frame = Frame(form_fram)
        type_frame.grid(row=1, column=0, columnspan=40, sticky="NWES", pady=20)

        if self.vehicle =="airplane" or self.vehicle=="train":
            radio_txt1="Return"
            radio_value1 = "return"
            radio_txt2 = "One Way"
            radio_value2 = "one_way"
        else:
            radio_txt1 = "Normal"
            radio_value1 = "normal"
            radio_txt2 = "VIP"
            radio_value2 = "vip"


        self.return_radio = Radiobutton(type_frame, text=radio_txt1, variable=self.ticket_type, value=radio_value1, font=("Times", 12),
                                   command=self.select_ticket_type_frame)
        self.return_radio.grid(row=0, column=0)

        self.one_way_radio = Radiobutton(type_frame, text=radio_txt2, variable=self.ticket_type, value=radio_value2,
                                    font=("Times", 12), command=self.select_ticket_type_frame)
        self.one_way_radio.grid(row=0, column=1)

        if self.vehicle =="airplane":
            cabin_classes = ["Economy", "Business", "First Class"]
            cabin_class = StringVar()
            cabin_class.set("Economy")

        elif self.vehicle =="buss":
            cabin_classes = ["‌Bed Buss","Half-Bed Buss"]
            cabin_class = StringVar()
            cabin_class.set("‌Bed Buss")


        if self.vehicle=="airplane" or self.vehicle=="buss":
            class_label = Label(type_frame, text="Cabin Class", font=("Times", 12), fg="blue")
            class_label.grid(row=0, column=2, padx=20)

            class_option = OptionMenu(type_frame, cabin_class, *cabin_classes)
            class_option.grid(row=0, column=3)

        if self.vehicle == "buss":

            depart_lable = Label(type_frame, text="Depart Date ", font=("Times", 12), fg="blue")
            depart_lable.grid(row=0, column=4, padx=5)

            self.depart_entry = Entry(type_frame)
            self.depart_entry.grid(row=0, column=5)

            depart_button = Button(type_frame, text="Select", font=("Times", 10),
                                   command=lambda: self.calendar("depart"))
            depart_button.grid(row=0, column=6, padx=5)
        else:

            date_frame = Frame(form_fram)
            date_frame.grid(row=2, column=0, columnspan=40, sticky="NWES")

            depart_lable = Label(date_frame, text="Depart Date ", font=("Times", 12), fg="blue")
            depart_lable.grid(row=0, column=0, padx=5)

            self.depart_entry = Entry(date_frame)
            self.depart_entry.grid(row=0, column=1)

            depart_button = Button(date_frame, text="Select", font=("Times", 10), command=lambda: self.calendar("depart"))
            depart_button.grid(row=0, column=2, padx=5)

            self.return_lable = Label(date_frame, text="Return Date ", font=("Times", 12), fg="blue")
            self.return_lable.grid(row=0, column=3, padx=5)

            self.return_entry = Entry(date_frame)
            self.return_entry.grid(row=0, column=4)

            self.return_button = Button(date_frame, text="Select", font=("Times", 10), command=lambda: self.calendar("return"))
            self.return_button.grid(row=0, column=5, padx=5)


        if self.user=="operator":
            operator_frame = Frame(form_fram)
            operator_frame.grid(row=3, column=0, columnspan=40, sticky="NWES",pady=20)

            basic_price_lable = Label(operator_frame, text="Price", font=("Times", 12), fg="blue")
            basic_price_lable.grid(row=0, column=0, padx=5)

            self.basic_price_entry = Entry(operator_frame)
            self.basic_price_entry.grid(row=0, column=1)

            inventory_label = Label(operator_frame, text="Number of ticket", font=("Times", 12), fg="blue")
            inventory_label.grid(row=0, column=2, padx=10)

            self.inventory_entry = Entry(operator_frame)
            self.inventory_entry.grid(row=0, column=3)

            time_label = Label(operator_frame, text="Time", font=("Times", 12), fg="blue")
            time_label.grid(row=1, column=0, padx=5,pady=20)

            self.time_entry = Entry(operator_frame)
            self.time_entry.grid(row=1, column=1)

            times=['AM', 'PM']
            time=StringVar()
            time.set('AM')
            time_option = OptionMenu(operator_frame,time,*times )
            time_option.grid(row=1, column=2)

            vehicle_lable=Label(operator_frame,text="Vehicle id",font=("Times", 12), fg="blue")
            vehicle_lable.grid(row=1, column=3,sticky="WE")

            self.vehicle_box = Entry(operator_frame)
            self.vehicle_box.grid(row=1, column=4,sticky="W")

            vehicle_select = Button(operator_frame, text="Select", font=("Times", 10))
            vehicle_select.grid(row=1, column=5, padx=5,sticky="W")

            vehicle_button = Button(operator_frame, text="Submit", font=("Times", 10), command=self.submit_form)
            vehicle_button.grid(row=2, column=1, columnspan=3, sticky="E", padx=100, pady=20)

    def create_register_vehicle_form(self):
        types = ['Coupe Train', 'Hall Train']
        self.type = StringVar()
        self.type.set("Coupe Train")

        vehicle_frame = Frame(self.frame_name, pady=10)
        vehicle_frame.grid(row=8, column=0, columnspan=40, sticky="NWES", pady=10)

        name_label=Label(vehicle_frame,text='Name')
        name_label.grid(row=0,column=0)

        self.name_entry = Entry(vehicle_frame)
        self.name_entry.grid(row=0, column=1)

        capacity_label = Label(vehicle_frame, text='Capacity')
        capacity_label.grid(row=0, column=2,padx=2)

        self.capacity_entry = Entry(vehicle_frame)
        self.capacity_entry.grid(row=0, column=3)

        company_label = Label(vehicle_frame, text='Company')
        company_label.grid(row=0, column=4, padx=2)

        self.company_entry = Entry(vehicle_frame)
        self.company_entry.grid(row=0, column=5)

        model_label = Label(vehicle_frame, text='Model')
        self.model_entry = Entry(vehicle_frame)

        if self.vehicle=='airplane':

            model_label.grid(row=1, column=0, padx=2)
            self.model_entry.grid(row=1, column=1)

            cargo_label = Label(vehicle_frame, text='Allowed Cargo')
            cargo_label.grid(row=1, column=2, padx=2)

            self.cargo_entry = Entry(vehicle_frame)
            self.cargo_entry.grid(row=1, column=3,pady=20)



        elif self.vehicle=="train":
            cupe_capacitys = ['4 people','6 people','8 people']
            self.cupe_capacity = StringVar()
            self.cupe_capacity.set('4 people')

            speeds = ['High Speed', 'Normal']
            self.speed = StringVar()
            self.speed.set('Normal')

            class_trains = ['5 star', '4 star','3 star','Economy']
            self.cabin_class = StringVar()
            self.cabin_class.set('Economy')

            type_lable = Label(vehicle_frame, text="Type")
            type_box = OptionMenu(vehicle_frame, self.type, *types)
            type_lable.grid(row=1, column=0, padx=2,pady=20)
            type_box.grid(row=1, column=1)

            cupe_capacity_label= Label(vehicle_frame, text="Cupe Capacity")
            cupe_capacity_label.grid(row=1, column=2,padx=10,sticky="WE")

            cupe_capacity_box = OptionMenu(vehicle_frame, self.cupe_capacity, *cupe_capacitys)
            cupe_capacity_box.grid(row=1, column=3,sticky="WE")

            speed_lable = Label(vehicle_frame, text="Speed")
            speed_lable.grid(row=1, column=4,sticky="WE")

            speed_box = OptionMenu(vehicle_frame, self.speed, *speeds)
            speed_box.grid(row=1, column=5,sticky="WE")

            class_lable = Label(vehicle_frame, text="Class")
            class_lable.grid(row=2, column=0,sticky="WE")

            class_box = OptionMenu(vehicle_frame, self.cabin_class, *class_trains)
            class_box.grid(row=2, column=1,sticky="WE")

        elif self.vehicle=="buss":
            types = ['Normal', 'VIP']
            self.type = StringVar()
            self.type.set("Normal")

            class_busses = ['Bed buss ', 'Half-bed Buss','Normal']
            self.cabin_class = StringVar()
            self.cabin_class.set("Normal")

            model_label.grid(row=1, column=0, padx=2)
            self.model_entry.grid(row=1, column=1)

            type_lable = Label(vehicle_frame, text="Type")
            type_box = OptionMenu(vehicle_frame, self.type, *types)
            type_lable.grid(row=1, column=2, padx=2, pady=20,sticky="WE")
            type_box.grid(row=1, column=3,sticky="WE")

            class_lable = Label(vehicle_frame, text="Class")
            class_lable.grid(row=1, column=4, sticky="WE")
            class_box = OptionMenu(vehicle_frame, self.cabin_class, *class_busses)
            class_box.grid(row=1, column=5, sticky="WE")



        vehicle_button = Button(vehicle_frame, text="Submit", font=("Times", 10), command=self.submit_form)
        vehicle_button.grid(row=3, column=1,columnspan=3,sticky="E",padx=100,pady=20)




        # origin_lable = Label(vehicle_frame, text="Origin", font=("Times", 12), fg="blue")
        # origin_lable.grid(row=0, column=0, padx=10)
        #
        # origin_box = OptionMenu(vehicle_frame, city, *citys)
        # origin_box.grid(row=0, column=1)
    def create_ticket_form(self):
        pass

