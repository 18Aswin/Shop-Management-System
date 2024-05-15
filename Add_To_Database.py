from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("D:\Projects\Shop Management System\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from Inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text = "Add To Database", font = ('ariel 48 bold'), fg = 'darkorchid3')
        self.heading.place(x=400, y=0)

        #Labels
        self.name1 = Label(master, text = "Enter Product Name -", font = ('ariel 20 bold'))
        self.name1.place(x=0, y=150)

        self.stock1 = Label(master, text = "Enter Stock -", font = ('ariel 20 bold'))
        self.stock1.place(x=0, y=220)

        self.cp1 = Label(master, text="Enter the Cost Price -", font=('ariel 20 bold'))
        self.cp1.place(x=0, y=290)

        self.sp1 = Label(master, text="Enter the Selling Price -", font=('ariel 20 bold'))
        self.sp1.place(x=0, y=360)

        self.vendor1 = Label(master, text="Enter Name of Vendor -", font=('ariel 20 bold'))
        self.vendor1.place(x=0, y=430)

        self.vendor_phone1 = Label(master, text="Enter Vendor PhoneNo. -", font=('ariel 20 bold'))
        self.vendor_phone1.place(x=0, y=500)

        self.id1 = Label(master, text="Enter Product ID -", font=('ariel 20 bold'))
        self.id1.place(x=0, y=570)

        #Enteries
        self.name2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.name2.place(x=380,y=150)

        self.stock2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.stock2.place(x=380, y=220)

        self.cp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.cp2.place(x=380, y=290)

        self.sp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.sp2.place(x=380, y=360)

        self.vendor2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.vendor2.place(x=380, y=430)

        self.vendor_phone2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.vendor_phone2.place(x=380, y=500)

        self.id2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.id2.place(x=380, y=570)

        #Button
        self.btn = Button(master, text="Add To Database", width=25, height=2, bg = 'darkorchid3', fg = 'white', font=('ariel 15 bold'), command=self.get_items)
        self.btn.place(x=200, y=650)

        self.btn_clear = Button(master, text="Clear All Fields", width=25, height=2, bg='indianred1', fg='white', font=('ariel 15 bold'), command=self.clear_all)
        self.btn_clear.place(x=600, y=650)

        #Textbox
        self.tBox = Text(master, width=50, height=24)
        self.tBox.place(x=850, y=150)
        self.tBox.insert(END, "ID has reached upto: " + str(id))

        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
        self.name = self.name2.get()
        self.stock = self.stock2.get()
        self.cp = self.cp2.get()
        self.sp = self.sp2.get()
        self.vedor = self.vendor2.get()
        self.vendor_phone = self.vendor_phone2.get()

        #Dynamic Entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.profit_per_item = float(self.sp) - float(self.cp)
        self.total_profit = float(self.profit_per_item) * float(self.stock)
        self.net_profit_margin = format(((float(self.sp) - float(self.cp))/(float(self.sp)))*100, ".2f")

        if self.name =='' or self.stock =='' or self.cp =='' or self.sp =='':
            tkinter.messagebox.showinfo("Error", "Please Fill All The Entries")
        else:
            sql = "INSERT INTO Inventory(name,stock,cp,sp,totalcp,totalsp,total_profit,profit_per_item,profit_margin_percentage,vendor,vendor_phone ) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.total_profit, self.profit_per_item, self.net_profit_margin, self.vedor, self.vendor_phone))
            conn.commit()

            #Textbox Insert
            self.tBox.insert(END, "\n\nInserted "+str(self.name)+ " into the database with code "+ str(self.id2.get()))

            tkinter.messagebox.showinfo("Success", "Data Added Successfully")

    def clear_all(self, *args, **kwargs):
        self.name2.delete(0, END)
        self.stock2.delete(0, END)
        self.cp2.delete(0, END)
        self.sp2.delete(0, END)
        self.vendor2.delete(0, END)
        self.vendor_phone2.delete(0, END)
        self.id2.delete(0, END)

root = Tk()
b = Database(root)

root.geometry("1366x786+0+0")
root.title("Add To Database")
root.mainloop()