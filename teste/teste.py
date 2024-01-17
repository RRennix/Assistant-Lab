# import modules
from tkinter import *
import winapps
 
# function to attach output 
def app():
 
    for item in winapps.search_installed(e.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        install_location.set(item.install_location)
 
 
# object of tkinter
# and background set for grey
master = Tk()
master.configure(bg='black')
 
# Variable Classes in tkinter
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
install_location = StringVar()
 
 
# Creating label for each information
# name using widget Label
Label(master, text="Enter App name : ",
      bg="black",fg='white').grid(row=0, sticky=W)
Label(master, text="Name : ",
      bg="black",fg='white').grid(row=2, sticky=W)
Label(master, text="Version :",
      bg="black",fg='white').grid(row=3, sticky=W)
Label(master, text="Install date :",
      bg="black",fg='white').grid(row=4, sticky=W)
Label(master, text="publisher :",
      bg="black",fg='white').grid(row=5, sticky=W)
Label(master, text="Path :",
      bg="black",fg='white').grid(row=6, sticky=W)
 
 
# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=name,
      bg="black",fg='white').grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=version,
      bg="black",fg='white').grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=Install_date,
      bg="black",fg='white').grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=publisher,
      bg="black",fg='white').grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=install_location,
      bg="black",fg='white').grid(row=6, column=1, sticky=W)
 
 
e = Entry(master, width=30)
e.grid(row=0, column=1)
 
# creating a button using the widget
b = Button(master, text="Show", command=app, bg="lime green",fg='black')
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
 
mainloop()