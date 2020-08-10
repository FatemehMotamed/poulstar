from datetime import datetime
from tkinter import *

from form_helper import FormHelper
from models import *
from settings import session


class PersonForm():
    def __init__(self, frame_name=None, window=None,ticket=None):
        self.frame_name=frame_name
        self.window=window
        self.ticket=ticket
        # self.model = Person()

    def submit_ticket(self):
        x=0
        n=datetime.now()
        reg_date=str(n.year)+"-"+str(n.month)+"-"+str(n.day)
        reg_time=str(n.hour)+":"+str(n.minute)+":"+str(n.second)
        for i in self.list_item:
            person=Person(i[0].get(),i[1].get(),i[2].get(),i[3].get())
            # person=Person("aa","ba","ca","da")
            # ticket = session.query(Ticket).filter(Ticket.id == self.ticket_id).one()
            reg=Register(self.price_list[x],reg_time,reg_date,self.ticket,person)
            session.add(reg)
            session.commit()
            x=x+1

    def create_person_info_form(self,number):
        self.list_item=[]
        f=FormHelper()
        data=f.read_json()
        header=[]
        self.price_list=[]
        for d in data:
            if d["number"]>0:
                for j in range(d["number"]):
                    header.append(d["age"])
                    self.price_list.append(d["finish_price"])
        x=0
        for i in range(10,int(number)+10):
            list_entry = []

            old_label = Label(self.window, text=header[x])
            old_label.grid(row=i, column=0)

            if x<len(header):
                x=x+1
            else:
                x=0

            name_label = Label(self.window, text="Firs Name")
            name_label.grid(row=i, column=1)

            list_entry.append(Entry(self.window))
            list_entry[0].grid(row=i, column=2)

            family_label = Label(self.window, text="Last Name")
            family_label.grid(row=i, column=3)

            list_entry.append(Entry(self.window))
            list_entry[1].grid(row=i, column=4)

            phone_label = Label(self.window, text="Phone")
            phone_label.grid(row=i, column=5)

            list_entry.append(Entry(self.window))
            list_entry[2].grid(row=i, column=6)

            code_label = Label(self.window, text="Code")
            code_label.grid(row=i, column=7)

            list_entry.append(Entry(self.window))
            list_entry[3].grid(row=i, column=8)
            list_entry=tuple(list_entry)
            self.list_item.append(list_entry)

        btn=Button(self.window,text="Register",command=self.submit_ticket)
        btn.grid(row=50,column=3,columnspan=2)

