import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk

from airplane import Airplane
from buss import Buss
from train import Train


class FormHelper():
    def __init__(self,window):
        self.window=window
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

    def set_date(self,entry_name):
        date_now=datetime.datetime.now()
        return_date = date_now + datetime.timedelta(days=7)
        date_now_str = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
        date_return_str = "{}-{}-{}".format(return_date.year, return_date.month, return_date.day)
        return date_now_str,date_return_str

        # self.depart_entry.insert(0, date_now_str)
        # self.number_passenger_entry.insert(0, "1 people")
        # if self.vehicle!="buss":
        #     self.return_entry.insert(0, date_return_str)

    def calendar(self,entry_name):
        date_now=datetime.datetime.now()
        print(entry_name)

        def print_sel():
            date = cal.selection_get()
            entry_name.delete(0, END)
            entry_name.insert(0, date)
            top.destroy()

        top = Toplevel(self.window)

        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=date_now.year, month=date_now.month, day=date_now.day)

        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def travellers(self,btn,entry_name):
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
                                                        command=lambda name=arg: self.travellers(name,entry_name))
                self.traveller_dic[i]['dec_button'].grid(row=i, column=1)

                self.traveller_dic[i]['number_label'] = Label(traveller_win, text=self.traveller_dic[i]['number'])
                self.traveller_dic[i]['number_label'].grid(row=i, column=2, padx=10)

                arg = "p" + str(i)
                self.traveller_dic[i]['inc_button'] = Button(traveller_win, text="+",
                                                        command=lambda name=arg: self.travellers(name,entry_name))
                self.traveller_dic[i]['inc_button'].grid(row=i, column=3)

            ok_button = Button(traveller_win, text="Ok", command=lambda: self.travellers("ok",entry_name))
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
            entry_name.delete(0, END)
            entry_name.insert(0, num)
            traveller_win.destroy()