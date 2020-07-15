from vehicle_form import VehicleForm
from tkinter import *
from form_helper import FormHelper

class TrainForm(VehicleForm):
    def __init__(self, frame_name,window):
        super().__init__(frame_name,window)

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

    def create_form(self):
        self.ticket_type = StringVar()
        self.ticket_type.set("return")
        cabin_classes = ["Economy", "Business", "First Class"]
        cabin_class = StringVar()
        cabin_class.set("Economy")

        self.return_radio = Radiobutton(self.exclusive_frame, text="Return", variable=self.ticket_type, value="return",
                                        font=("Times", 12),
                                        command=self.select_ticket_exclusive_frame)
        self.return_radio.grid(row=0, column=0)

        self.one_way_radio = Radiobutton(self.exclusive_frame, text="One Way", variable=self.ticket_type, value="one_way",
                                         font=("Times", 12), command=self.select_ticket_exclusive_frame)
        self.one_way_radio.grid(row=0, column=1)

        date_frame = Frame(self.exclusive_frame)
        date_frame.grid(row=2, column=0, columnspan=40, sticky="NWES")

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