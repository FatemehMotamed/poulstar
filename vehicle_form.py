from tkinter import *

from form_helper import FormHelper


class VehicleForm():
    def __init__(self, frame_name,window):
        self.window=window
        self.frame_name = frame_name
        self.exclusive_frame = Frame(self.frame_name)
        self.exclusive_frame.grid(row=1, column=0, columnspan=40, sticky="NWES", pady=20)


    def create_form(self):
        self.vehicle_radio = StringVar()
        self.vehicle_radio.set("airplane")

        citys = ['tehran', 'rasht', 'shiraz']
        self.origin_city = StringVar()
        self.origin_city.set("tehran")
        self.destination_city = StringVar()
        self.destination_city.set("tehran")


        form_fram = Frame(self.frame_name, pady=10)
        form_fram.grid(row=0, column=0, columnspan=40, sticky="NWES", pady=10)

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
                                         command=lambda: FormHelper(self.window).travellers("show",self.number_passenger_entry))
        number_passenger_button.grid(row=0, column=6, padx=3)



