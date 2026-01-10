from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('100x100')
def msg():
    messagebox.showinfo("Alert","stop ! Vius found")
    
button=Button(text="scan for virus",command=msg)
button.place(x=40,y=40)
window.mainloop()