from tkinter import *
from datetime import date

window=Tk()
window.title("getting started with widgets")
window.geometry("400x300")

lbl=Label(window, text="Hello World",fg="darkblue",bg="lightyellow",height=1,width=300)

name_lbl=Label(window, text="Enter your name:",bg="gold")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message
    message="Welcome to the application !\nToday  date is : "
    greet="hello"+name+ "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="Begin",command=display,heigth=1,bg="pink",fg="red")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()