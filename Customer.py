import random
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("D:\Projects\Shop Management System\Database\store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()

#temporary list
products_list =[]
product_price =[]
product_quantity = []
product_id =[]

#List for Labels
labels_list =[]

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        #Frames
        self.left = Frame(master, width=700, height=786, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=786, bg='lightblue')
        self.right.pack(side=RIGHT)

        #Components
        self.heading = Label(self.left, text = "311 Stores Pvt Ltd.", font=('ariel 48 bold italic underline'), bg='white')
        self.heading.place(x=0, y=0)

        self.date1 = Label(self.right, text="Today's Date : "+str(date), font=('ariel 18 bold'), bg='lightblue', fg='white')
        self.date1.place(x=0, y=0)

        #table invoice
        self.tProduct = Label(self.right, text="Products", font=('ariel 20 bold italic underline'), bg='lightblue', fg='white')
        self.tProduct.place(x=0, y=100)

        self.tquantity = Label(self.right, text="Quantity", font=('ariel 20 bold italic underline'), bg='lightblue', fg='white')
        self.tquantity.place(x=325, y=100)

        self.tamount = Label(self.right, text="Amount", font=('ariel 20 bold italic underline'), bg='lightblue', fg='white')
        self.tamount.place(x=525, y=100)

        #Entering Data
        self.enterid1 = Label(self.left, text="Enter Product ID", font=('ariel 18 bold'), bg='white')
        self.enterid1.place(x=0, y=125)

        self.enterid2 = Entry(self.left, width=8,font=('ariel 18 bold'), bg='gray94')
        self.enterid2.place(x=250, y=125)
        self.enterid2.focus()

        #Button
        self.search_btn = Button(self.left, text="Search", font=('ariel 18 bold'), fg='white', bg='gray80', command=self.ajax)
        self.search_btn.place(x=400, y=115)

        #Fill later with ajax
        self.productname = Label(self.left, text="", bg='white', fg='SpringGreen3', font=('ariel 25 bold'))
        self.productname.place(x=0, y=200)

        self.pprice = Label(self.left, text="", bg='white', fg='SpringGreen3', font=('ariel 25 bold'))
        self.pprice.place(x=0, y=250)

        self.pstock = Label(self.left, text="", bg='white', fg='SpringGreen3', font=('ariel 25 bold'))
        self.pstock.place(x=0, y=300)

        #Total Label
        self.total1 = Label(self.right, text="", font=('ariel 40 bold'), bg='lightblue', fg='white')
        self.total1.place(x=0, y=650)

        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bill)

    def ajax(self, *args, **kwargs):
        self.getid = self.enterid2.get()
        #Get Product Info
        query = "SELECT * from Inventory WHERE id=?"
        result = c.execute(query, (self.getid, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="Product's name: "+str(self.get_name))
        self.pprice.configure(text="Price: Rs " + str(self.get_price))
        self.pstock.configure(text="Pieces Left: " + str(self.get_stock))

        # Quantity
        self.quantity_1 = Label(self.left, text="Enter Quantity", font=('ariel 20 bold'), bg='white')
        self.quantity_1.place(x=0, y=400)
        self.quantity_2 = Entry(self.left, width=10, font=('ariel 20 bold'), bg='gray80')
        self.quantity_2.place(x=220, y=400)
        self.quantity_2.focus()

        # Discount
        self.discount_1 = Label(self.left, text="Enter Discount", font=('ariel 20 bold'), bg='white')
        self.discount_1.place(x=0, y=450)
        self.discount_2 = Entry(self.left, width=10, font=('ariel 20 bold'), bg='gray80')
        self.discount_2.place(x=220, y=450)
        self.discount_2.insert(END, 0)

        #Add to Cart Button
        self.add_to_cart_btn = Button(self.left, text="Add To Cart", font=('ariel 18 bold'), fg='white', bg='gray', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=150, y=500)

        #Generate Bill and Change
        self.change_1 = Label(self.left, text="Given Amount", font=('ariel 20 bold'), bg='white')
        self.change_1.place(x=0, y=600)
        self.change_2 = Entry(self.left,width=10, font=('ariel 20 bold'), bg='gray80')
        self.change_2.place(x=200, y=600)

        #change Button
        self.change_btn = Button(self.left, text="Calculate Change", width=20, height=1, font=('ariel 18 bold'), fg='white', bg='gray', command=self.change_func)
        self.change_btn.place(x=380, y=590)

        #Generate Bill Button
        self.bill_btn = Button(self.left, text="Generate Bill", width=46, height=1, font=('ariel 18 bold'), fg='white', bg='orange', command=self.generate_bill)
        self.bill_btn.place(x=0, y=733)

    def add_to_cart(self, *args, **kwargs):
        #Get values and form the database
        self.quantity_value = int(self.quantity_2.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error!", "Don't have enough stock.")
        else:
            #Price
            self.final_price = (float((self.quantity_value) * (self.get_price))) - float(self.discount_2.get())
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append((self.get_id))

            self.x_index = 0
            self.y_index = 160
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]),font=('ariel 18 bold'), bg='lightblue', fg='white')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqu = Label(self.right, text=str(product_quantity[self.counter]), font=('ariel 18 bold'), bg='lightblue', fg='white')
                self.tempqu.place(x=325, y=self.y_index)
                labels_list.append(self.tempqu)

                self.tempamt = Label(self.right, text=str(product_price[self.counter]), font=('ariel 18 bold'), bg='lightblue', fg='white')
                self.tempamt.place(x=525, y=self.y_index)
                labels_list.append(self.tempamt)

                self.y_index += 40
                self.counter += 1

                #total configure
                self.total1.configure(text="Total: Rs. "+str(sum(product_price)))

                # Delete
                self.quantity_1.place_forget()
                self.quantity_2.place_forget()
                self.discount_1.place_forget()
                self.discount_2.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.pstock.configure(text="")
                self.add_to_cart_btn.destroy()

                #Autofocus on ID
                self.enterid2.focus()
                self.enterid2.delete(0, END)

    def change_func(self, *args, **kwargs):
        #Get amount given by customer
        self.amount_given = float(self.change_2.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        #Label Change
        self.change_amount = Label(self.left, text="Change: Rs. "+str(self.to_give), font=('ariel 22 bold'), fg='red', bg='white')
        self.change_amount.place(x=200, y=670)

    def generate_bill(self, *args, **kwargs):
        #Create the Bill before updating the Database
        directory = "D:/Projects/Shop Management System/Invoice/"+str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        #Templates for the Bill
        company = "\t\t\t\t    311 Stores Pvt. Ltd.\n"
        address = "\t\t\t\t  Just Beyond a Heartbeat\n"
        phone = "\t\t\t\t\t   273105311\n"
        sample = "\t\t\t\t\t    Invoice\n"
        dt = "\t\t\t\t\t  "+str(date)

        table_header = "\n\n\t-------------------------------------------------------------\n\t\tSN.\tProducts\t\t\t\tQty\t\tAmount\n\t-------------------------------------------------------------"
        final = company + address + phone + sample + dt + "\n" + table_header

        #Open file to Write into
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, 'w')
        f.write(final)
        #Fill Dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t"+str(r)+"\t"+str(products_list[i]+"...........")[:12]+"\t\t\t"+str(product_quantity[i])+"\t\t"+str(product_price[i]))

            i += 1
            r += 1

        f.write("\n\n\n\t\t\tTotal: \t\t\t\t\t  Rs. "+str(sum(product_price)))
        f.write("\n\n\t\t\t\t   Thanks For Visiting!")
        #os.startfile(file_name, "print")
        f.close()

        #decrease the stock
        self.x = 0

        initial = "SELECT * FROM Inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x], ))

        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.get_stock) - int(product_quantity[self.x])

            #Updating Stock
            sql = "UPDATE Inventory SET stock=? where id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()

            #Insert Into Transaction
            sql2 = "INSERT INTO Transactions (product_name,quantity,amount,date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x],date))
            conn.commit()

            self.x += 1

        for a in labels_list:
            a.destroy()

        del(products_list[:])
        del(product_id[:])
        del(product_quantity[:])
        del(product_price[:])

        self.total1.configure(text="")
        self.change_amount.configure(text="")
        self.change_2.delete(0, END)
        self.enterid2.focus()

        tkinter.messagebox.showinfo("Success", "Thanks for Visiting...")

root = Tk()
b = Application(root)

root.geometry("1366x786+0+0")
root.mainloop()