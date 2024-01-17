import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import windowsapps
root = tk.Tk()
root.geometry('500x100')
root.attributes('-alpha',0.75)
root.attributes('-topmost',True)
root.anchor('center')
root.title('Abrir apps')
root.iconbitmap('X:/Downloads/Lab-1-main/tktest/icon.ico')
def open(aplicativo):
    try:
        windowsapps.open_app(aplicativo)
    except:
        resultado = "Can't find "+str(aplicativo)
        showinfo(
            title='Error',
            message= resultado
            )
app = tk.StringVar()
print(app)
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)
app_label = ttk.Label(frame,background='lime green',text='Insert the app name below')
app_label.pack(fill='x',expand=True)
app_entry = ttk.Entry(frame,textvariable= app).pack(fill='x',expand=True)
ttk.Button(
    frame,
    text='Open',
    command= lambda: open(app.get())
).pack()
root.mainloop()