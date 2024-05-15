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
        self.heading = Label(master, text = "Update The Database", font = ('ariel 48 bold'), fg = 'darkorchid3')
        self.heading.place(x=400, y=0)

        self.id_top = Label(master, text= "Enter ID: ", font = ('ariel 20 bold'))
        self.id_top.place(x=0, y=100)
        #Labels
        self.name1 = Label(master, text = "Product Name -", font = ('ariel 20 bold'))
        self.name1.place(x=0, y=170)

        self.stock1 = Label(master, text = "Stock -", font = ('ariel 20 bold'))
        self.stock1.place(x=0, y=240)

        self.cp1 = Label(master, text="Cost Price -", font=('ariel 20 bold'))
        self.cp1.place(x=0, y=310)

        self.sp1 = Label(master, text="Selling Price -", font=('ariel 20 bold'))
        self.sp1.place(x=0, y=380)

        self.total_cp1 = Label(master, text="Total Cost Price -", font=('ariel 20 bold'))
        self.total_cp1.place(x=0, y=450)

        self.total_sp1 = Label(master, text="Total Selling Price -", font=('ariel 20 bold'))
        self.total_sp1.place(x=0, y=520)

        self.vendor1 = Label(master, text="Name of Vendor -", font=('ariel 20 bold'))
        self.vendor1.place(x=0, y=590)

        self.vendor_phone1 = Label(master, text="Vendor PhoneNo. -", font=('ariel 20 bold'))
        self.vendor_phone1.place(x=0, y=660)

        self.total_profit1 = Label(master, text="Total Profit -", font=('ariel 18 bold'))
        self.total_profit1.place(x=850, y=550)

        self.profit_per_item1 = Label(master, text="Profit Per Item -", font=('ariel 18 bold'))
        self.profit_per_item1.place(x=850, y=600)

        self.profit_margin1 = Label(master, text="Profit Margin -", font=('ariel 18 bold'))
        self.profit_margin1.place(x=850, y=650)

        #Enteries
        self.id_top = Entry(master, width=5, font=('ariel 20 bold'))
        self.id_top.place(x=380, y=100)
        self.id_top.focus()

        self.name2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.name2.place(x=380,y=170)

        self.stock2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.stock2.place(x=380, y=240)

        self.cp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.cp2.place(x=380, y=310)

        self.sp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.sp2.place(x=380, y=380)

        self.total_cp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.total_cp2.place(x=380, y=450)

        self.total_sp2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.total_sp2.place(x=380, y=520)

        self.vendor2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.vendor2.place(x=380, y=590)

        self.vendor_phone2 = Entry(master, width=25, font=('ariel 20 bold'))
        self.vendor_phone2.place(x=380, y=660)

        self.total_profit2 = Entry(master, width=15, font=('ariel 18 bold'))
        self.total_profit2.place(x=1050, y=550)

        self.profit_per_item2 = Entry(master, width=15, font=('ariel 18 bold'))
        self.profit_per_item2.place(x=1050, y=600)

        self.profit_margin2 = Entry(master, width=15, font=('ariel 18 bold'))
        self.profit_margin2.place(x=1050, y=650)

        #Button
        self.btn = Button(master, text="Update Database", width=25, height=2, bg = 'darkorchid3', fg = 'white', font=('ariel 15 bold'), command=self.update)
        self.btn.place(x=420, y=720)

        self.btn_search = Button(master, text="Search", width=8, height=1, bg='chocolate2', fg='white',font=('ariel 15 bold'), command=self.search)
        self.btn_search.place(x=500, y=100)

        #Textbox
        self.tBox = Text(master, width=50, height=24)
        self.tBox.place(x=850, y=150)
        self.tBox.insert(END, "ID has reached upto: " + str(id))

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM Inventory WHERE id=?"
        result = c.execute(sql, (self.id_top.get(), ))
        for r in result:
            self.n1 = r[1]#name
            self.n2 = r[2]#stock
            self.n3 = r[3]#cp
            self.n4 = r[4]#sp
            self.n5 = r[5]#totalcp
            self.n6 = r[6]#totalsp
            self.n7 = r[7]#total_profit
            self.n8 = r[8]#profit_per_item
            self.n9 = r[9]#profit_margin_percentage
            self.n10 = r[10]#vendor
            self.n11 = r[11]#vendor_phone
        conn.commit()

        self.name2.delete(0, END)
        self.name2.insert(0, str(self.n1))

        self.stock2.delete(0, END)
        self.stock2.insert(0, str(self.n2))

        self.cp2.delete(0, END)
        self.cp2.insert(0, str(self.n3))

        self.sp2.delete(0, END)
        self.sp2.insert(0, str(self.n4))

        self.total_cp2.delete(0, END)
        self.total_cp2.insert(0, str(self.n5))

        self.total_sp2.delete(0, END)
        self.total_sp2.insert(0, str(self.n6))

        self.vendor2.delete(0, END)
        self.vendor2.insert(0, str(self.n10))

        self.vendor_phone2.delete(0, END)
        self.vendor_phone2.insert(0, str(self.n11))

        self.total_profit2.delete(0, END)
        self.total_profit2.insert(0, str(self.n7))

        self.profit_per_item2.delete(0, END)
        self.profit_per_item2.insert(0, str(self.n8))

        self.profit_margin2.delete(0, END)
        self.profit_margin2.insert(0, str(self.n9))

    def update(self, *args, **kwargs):
        self.u1 = self.name2.get()
        self.u2 = self.stock2.get()
        self.u3 = self.cp2.get()
        self.u4 = self.sp2.get()
        self.u5 = self.total_cp2.get()
        self.u6 = self.total_sp2.get()
        self.u7 = self.vendor2.get()
        self.u8 = self.vendor_phone2.get()
        self.u9 = self.total_profit2.get()
        self.u10 = self.profit_per_item2.get()
        self.u11 = self.profit_margin2.get()

        qurey = "UPDATE Inventory SET name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,total_profit=?,profit_per_item=?,profit_margin_percentage=?,vendor=?,vendor_phone=? WHERE id=?"
        c.execute(qurey, (self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u9,self.u10,self.u11,self.u7,self.u8, self.id_top.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Values updated in Database")

root = Tk()
b = Database(root)

root.geometry("1366x786+0+0")
root.title("Update The Database")
root.mainloop()