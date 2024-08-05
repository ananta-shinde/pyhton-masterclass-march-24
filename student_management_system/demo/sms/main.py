import tkinter
from tkinter import *


myapp = tkinter.Tk(className="Login")
welcome_message = Label(myapp,text="Welcome to Student Management System")
username_label = Label(myapp,text ="Username :")
password_label = Label(myapp,text="Password :")
login_button = Button(myapp,text="Login",width=50)
username_entry = Entry(myapp)
password_entry = Entry(myapp)
terms_and_condition_checkbutton = Checkbutton(myapp,text="I accept terms and condition")




welcome_message.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
terms_and_condition_checkbutton.pack()
login_button.pack()



myapp.mainloop()


