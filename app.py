from tkinter import *
import customtkinter
import os
import sqlite3

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

# Beginning of the app
app = customtkinter.CTk()
app.geometry('350x450')
app.title('Signing in...')

conn = sqlite3.connect('barcode.db')
c = conn.cursor()

table_name = 'stock'

# Check if the table exists
c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
table_exists = c.fetchone()

if table_exists:
    print(f"The table '{table_name}' exists.")
else:
    print(f"The table '{table_name}' does not exist.")
    print(f"Creating table: '{table_name}'...")
    
    c.execute(f"""CREATE TABLE '{table_name}'
            (
            productName text,
            barcode text, 
            quantity int
            )"""
            )

conn.commit()
# Functions


def de():

    warningText = customtkinter.CTkLabel(app, text="Something went wrong,\nplease check your password and username...", text_color="#ed4337", font=('', 12))
    checkUserName = username.get()
    checkPwd = pwd.get()
 
    def submit():

        conn = sqlite3.connect('barcode.db')
        c = conn.cursor()

        p_name = productName.get()
        p_code = productBarCode.get()
        p_qty =  productQuantity.get()

        warningLabel = customtkinter.CTkLabel(main, text="Noticed empty fields", text_color="#ed4337")

        if warningLabel.winfo_exists() == 1:
            warningLabel.destroy()
        else:
            pass

        if not p_name:
            print('no value for product name')
            warningLabel = customtkinter.CTkLabel(main, text="Noticed empty fields", text_color="#ed4337")
            warningLabel.place(relx=0.2, rely=0.47)
        elif not p_code:
            print('no value for product code')
            warningLabel = customtkinter.CTkLabel(main, text="Noticed empty fields", text_color="#ed4337")
            warningLabel.place(relx=0.2, rely=0.47)
        elif not p_qty:
            print('no value for product quantity')
            warningLabel = customtkinter.CTkLabel(main, text="Noticed empty fields", text_color="#ed4337")
            warningLabel.place(relx=0.2, rely=0.47)
        else:
            c.execute('INSERT INTO stock VALUES (:p_name, :p_code, :p_qty)',{
                'p_name': productName.get(),
                'p_code': productBarCode.get(),
                'p_qty': productQuantity.get()
            })


        conn.commit()
        
    if checkUserName == "admin" and checkPwd == "pwd":
        button.configure(state="disabled")
        main = customtkinter.CTk()
        main.title('PDE')
        main.geometry('750x750')

        def clearFrame():
            frameChildren = frameForOutput.winfo_children()
            print(frameChildren)

            for child in frameChildren:
                child.destroy()
            # frameChildren.destroy()


        def query():

            conn = sqlite3.connect('barcode.db')
            c = conn.cursor()

            c.execute("SELECT *, oid FROM stock")
            data = c.fetchall()
            print(data)

            print_data = ''
            for i in data:
                print_data += str(i[3]) + ' |' + ' ' + str(i[0]) + ' - ' + str(i[1]) + ' - ' + str(i[2]) + '\n'

            query_label = customtkinter.CTkLabel(frameForOutput, text=print_data, font=("Impact", 16))
            query_label.pack()
            query_label.configure(state='disabled')

        

        clearBtn = customtkinter.CTkButton(master=main, text="Clear", command=clearFrame, font=('Garamond', 15))
        clearBtn.place(relx=0.36, rely=0.47, anchor=customtkinter.CENTER)

        title = customtkinter.CTkLabel(main, text="PDE", corner_radius=2.5, font=('Impact', 25),width=260, height=30)
        title.place(rely=0.05, relx=0.5 ,anchor=customtkinter.CENTER)
        

        productName = customtkinter.CTkEntry(main, width=320, height=30, placeholder_text="Product name")
        productName.place(rely=0.2, relx=0.05)

        productBarCode = customtkinter.CTkEntry(main, width=320, height=30, placeholder_text="Product Code")
        productBarCode.place(rely=0.27, relx=0.05)

        productQuantity = customtkinter.CTkEntry(main, width=320, height=30, placeholder_text="Product Quantity")
        productQuantity.place(rely=0.34, relx=0.05)

        dataEntryBtn = customtkinter.CTkButton(master=main, text="Enter", font=('Garamond', 15), command=submit)
        dataEntryBtn.place(relx=0.16, rely=0.42, anchor=customtkinter.CENTER)

        dataListOut = customtkinter.CTkButton(master=main, text="List Out", command=query, font=('Garamond', 15))
        dataListOut.place(relx=0.36, rely=0.42, anchor=customtkinter.CENTER)

        frameForOutput = customtkinter.CTkScrollableFrame(main, width=300, height=500)
        frameForOutput.place(relx=0.5, rely=0.2)

        

        main.resizable(False,False)
        main.mainloop()

    else:
        warningText.place(rely=0.7, relx=0.5 ,anchor=customtkinter.CENTER)
        
    

# UI
title = customtkinter.CTkLabel(app, text="Authorization", corner_radius=5, font=('Garamond', 25),width=160, height=30)
title.place(rely=0.3, relx=0.5 ,anchor=customtkinter.CENTER)

username = customtkinter.CTkEntry(app, width=220, height=25, placeholder_text="Username")
username.place(rely=0.42, relx=0.5, anchor=customtkinter.CENTER)

pwd = customtkinter.CTkEntry(app, width=220, height=25, placeholder_text="Password", show="*")
pwd.place(rely=0.5, relx=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="SIGN IN", font=('Garamond', 15), command=de)
button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


app.resizable(False,False)
app.mainloop()

