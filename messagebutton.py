from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x400")
def f1():
    messagebox.showinfo("Information","Red clicked")
b1=Button(root,text="Red",font="Arial 30 bold ",fg="white",bg="red",width=10,command=f1)
b1.pack()
def f2():
    messagebox.showinfo("Information","Green clicked")
b2=Button(root,text="Green",font="Arial 30 bold ",fg="white",bg="green",width=10,command=f2)
b2.pack()
def f3():
    messagebox.showinfo("Information","Blue clicked")
b3=Button(root,text="Blue",font="Arial 30 bold ",fg="white",bg="blue",width=10,command=f3)
b3.pack()
def f4():
    messagebox.showinfo("Information","Pink clicked")
b4=Button(root,text="Pink",font="Arial 30 bold ",fg="white",bg="pink",width=10,command=f4)
b4.pack()
root.mainloop()