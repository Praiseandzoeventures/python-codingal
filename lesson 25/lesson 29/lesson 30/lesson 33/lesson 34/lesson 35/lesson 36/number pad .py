from tkinter import *
window=Tk()
window.title("Number Pad")
window.geometry("250x300")
nums=[[9,8,7],[6,5,4],[3,2,1],['4',0,'*']]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)

window.rowconfigure(i,weight=1,minsize=50)

for j in range(0,3):

Frame = Frame(master=window,relief = SUNKEN,borderwidth=1)

Frame.grid(row=i,column=j)

label=Label(master=Frame,text=nums[i][j],bg="yellow")

label.pack(padx=3,pady=3)

window.mainloop()
textbox=Text(bg="lightblue",height=2,width=20)