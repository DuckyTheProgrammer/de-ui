from tkinter import *
import customtkinter
import os

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

# Beginning of the app
app = customtkinter.CTk()
app.geometry('350x450')
app.title('Signing in...')

# Functions
def de():
    warningText = customtkinter.CTkLabel(app, text="Something went wrong,\nplease check your password and username...", text_color="#ed4337", font=('', 12))
    checkUserName = username.get()
    checkPwd = pwd.get()
    
    if checkUserName == "admin" and checkPwd == "pwd":
        button.configure(state="disabled")
        main = customtkinter.CTk()
        main.title('PDE')
        main.geometry('750x750')


        title = customtkinter.CTkLabel(main, text="PDE", corner_radius=2.5, font=('Impact', 25),width=260, height=30)
        title.place(rely=0.05, relx=0.5 ,anchor=customtkinter.CENTER)

        barCode = customtkinter.CTkEntry(main, width=320, height=30, placeholder_text="Barcode of the product")
        barCode.place(rely=0.2, relx=0.05)

        barCodeEntry = customtkinter.CTkButton(master=main, text="Enter", font=('Garamond', 15))
        barCodeEntry.place(relx=0.58, rely=0.22, anchor=customtkinter.CENTER)

        dataListOut = customtkinter.CTkButton(master=main, text="List Out", font=('Garamond', 15))
        dataListOut.place(relx=0.77, rely=0.22, anchor=customtkinter.CENTER)

        

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

