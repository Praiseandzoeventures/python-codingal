from tkinter import *

window = Tk()
window.title('event handler')
window.geometry('100x100')

def handler__keypress(event):
    print(event.char)
window.bind('<Key>', handler__keypress)
def handler__click(event):
    print("\n button clicked")
button=Button(text="click me")
button.pack()
button.bind('<Button-1>', handler__click)
window.mainloop()