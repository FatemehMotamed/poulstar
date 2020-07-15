from vehicle_form import VehicleForm
from tkinter import *
from form_helper import FormHelper

class BussForm(VehicleForm):
    def __init__(self, frame_name,window):
        super().__init__(frame_name,window)


    def select_ticket_exclusive_frame(self):
        pass



    def create_form(self):
        cabin_classes = ["‌Bed Buss", "Half-Bed Buss"]
        cabin_class = StringVar()
        cabin_class.set("‌Bed Buss")

        self.ticket_type = StringVar()
        self.ticket_type.set("normal")

        self.normal_radio = Radiobutton(self.exclusive_frame, text="Normal", variable=self.ticket_type, value="normal",
                                        font=("Times", 12),
                                        command=self.select_ticket_exclusive_frame)
        self.normal_radio.grid(row=0, column=0)

        self.vip_radio = Radiobutton(self.exclusive_frame, text="VIP", variable=self.ticket_type, value="vip",
                                         font=("Times", 12), command=self.select_ticket_exclusive_frame)
        self.vip_radio.grid(row=0, column=1)


        class_label = Label(self.exclusive_frame, text="Cabin Class", font=("Times", 12), fg="blue")
        class_label.grid(row=0, column=2, padx=20)

        class_option = OptionMenu(self.exclusive_frame, cabin_class, *cabin_classes)
        class_option.grid(row=0, column=3)

        depart_lable = Label(self.exclusive_frame, text="Depart Date ", font=("Times", 12), fg="blue")
        depart_lable.grid(row=0, column=4, padx=5)

        self.depart_entry = Entry(self.exclusive_frame)
        self.depart_entry.grid(row=0, column=5)

        depart_button = Button(self.exclusive_frame, text="Select", font=("Times", 10),
                               command=lambda: FormHelper(self.window).calendar(self.depart_entry))
        depart_button.grid(row=0, column=6, padx=5)