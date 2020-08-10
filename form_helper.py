import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk

from tkinter import ttk
import json

# from vehicle_form import VehicleForm

from ttkwidgets import CheckboxTreeview
class FormHelper():
    def __init__(self,window=None,frame=None):
        self.window=window
        self.frame=frame
        self.traveller_dic  = self.read_json()

        self.item_list = {0: {}, 1: {}, 2: {}, 3: {}}
    def radio_on_off(self,radio,btn,entry,label):

        t = radio.get()
        if t == "one_way":
            btn.config(state="disabled")
            entry.config(state="disabled")
            label.config(state="disabled")
        elif t == "return":
            btn.config(state="normal")
            entry.config(state="normal")
            label.config(state="normal")

    def set_date(self,entry_name):
        date_now=datetime.datetime.now()
        return_date = date_now + datetime.timedelta(days=7)
        date_now_str = "{}-{}-{}".format(date_now.year, date_now.month, date_now.day)
        date_return_str = "{}-{}-{}".format(return_date.year, return_date.month, return_date.day)
        return date_now_str,date_return_str


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

    def read_json(self):
        with open('traveller.json') as json_file:
            data  = json.load(json_file)
        return data

    def write_json(self,data):
        with open('traveller.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def travellers(self,btn,entry_name):
        global traveller_win
        sum_traveller = 0

        if btn == "show":
            traveller_win = Toplevel(self.window)
            traveller_win.geometry("250x220")

            for i in range(0, 3):
                self.item_list[i]['age_label'] = Label(traveller_win, text=self.traveller_dic[i]['age'], font=("Times", 12),
                                                      fg="blue", pady=20)
                self.item_list[i]['age_label'].grid(row=i, column=0)

                arg = "m" + str(i)
                self.item_list[i]['dec_button'] = Button(traveller_win, text="-",
                                                        command=lambda name=arg: self.travellers(name,entry_name))
                self.item_list[i]['dec_button'].grid(row=i, column=1)

                self.item_list[i]['number_label'] = Label(traveller_win, text=self.traveller_dic[i]['number'])
                self.item_list[i]['number_label'].grid(row=i, column=2, padx=10)

                arg = "p" + str(i)
                self.item_list[i]['inc_button'] = Button(traveller_win, text="+",
                                                        command=lambda name=arg: self.travellers(name,entry_name))
                self.item_list[i]['inc_button'].grid(row=i, column=3)

            ok_button = Button(traveller_win, text="Ok", command=lambda: self.travellers("ok",entry_name))
            ok_button.place(x=100, y=180)

        elif btn[0] == "p":
            index = int(btn[1])
            if self.traveller_dic[index]['number'] < 20:
                self.traveller_dic[index]['number'] += 1
            self.item_list[index]['number_label'].config(text=self.traveller_dic[index]['number'])

        elif btn[0] == "m":
            index = int(btn[1])
            if self.traveller_dic[index]['number'] > 0:
                self.traveller_dic[index]['number'] -= 1
            self.item_list[index]['number_label'].config(text=self.traveller_dic[index]['number'])
        if btn == "ok":
            for item in self.traveller_dic:
                sum_traveller += item['number']
            entry_name.delete(0, END)
            entry_name.insert(0, sum_traveller)
            traveller_win.destroy()
            self.write_json(self.traveller_dic)

    def reset_json(self):

        with open('traveller.json') as json_file:
            data = json.load(json_file)

        for item in data:
            item['number'] = 0
            item['finish_price'] = 0

        with open('traveller.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    def list_attribute(self,model):
        list = model.__dict__
        list_attr=[]

        for i in list:
            if not i[0].startswith('_'):
                list_attr.append(i)
        return list_attr

    def mycallback(self,event):
        global last_focus
        item=self.treev.item(self.treev.selection())
        # self.item=item['values']
        self.item_id=item['values'][0]
        _iid = self.treev.identify_row(event.y)
        if _iid != last_focus:
            if last_focus:
                self.treev.item(last_focus, tags=[])
            self.treev.item(_iid, tags=['focus'])
            last_focus = _iid

    def create_table(self,table_data):
        coulumn_list=[]
        row_list = []
        if table_data=={}:
            return 0
        self.window.resizable(width=1, height=1)


        self.treev = CheckboxTreeview(self.frame, selectmode='browse',height=2)

        self.treev.grid(row=1,column=0)



        verscrlbar = ttk.Scrollbar(self.frame,
                                   orient="vertical",
                                   command=self.treev.yview)

        verscrlbar.grid(row=1,column=1)

        self.treev.configure(xscrollcommand=verscrlbar.set)

        self.treev.tag_configure('focus', background='blue')
        global last_focus
        last_focus = None
        self.treev.bind("<ButtonRelease-1>", self.mycallback)

        # coulumn_list.insert(0,"")
        # table_data=VehicleForm("", "", model).select_data()

        for key, value in table_data[0].items():
            coulumn_list.append(key)

        self.treev["columns"] = coulumn_list

        # Defining heading
        self.treev['show'] = 'headings'

        for i in range(0,len(coulumn_list)):
            self.treev.column(str(i), width=90, anchor='c')
            self.treev.heading(str(i), text=str(coulumn_list[i]))

        for i in range(0,len(table_data)):
            for key, value in table_data[i].items():
                row_list.append(value)
            r=self.treev.insert("", 'end', text=i,
                                      values=tuple(row_list))
            self.treev.change_state(r,"checked")
            row_list=[]



