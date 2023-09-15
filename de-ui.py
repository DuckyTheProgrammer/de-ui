from tkinter import *
import customtkinter


main = customtkinter.CTk()
main.title('PDE')
main.geometry('750x750')


title = customtkinter.CTkLabel(main, text="PDE", corner_radius=2.5, font=('Impact', 25),width=260, height=30)
title.place(rely=0.05, relx=0.5 ,anchor=customtkinter.CENTER)

barCode = customtkinter.CTkEntry(main, width=320, height=30, placeholder_text="Barcode of the product")
barCode.place(rely=0.2, relx=0.05)

button = customtkinter.CTkButton(master=main, text="Enter", font=('Garamond', 15))
button.place(relx=0.58, rely=0.22, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(master=main, text="List Out", font=('Garamond', 15))
button2.place(relx=0.77, rely=0.22, anchor=customtkinter.CENTER)

main.mainloop()