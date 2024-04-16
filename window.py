from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("tkwindow")
root.configure(bg="blue")
root.resizable(True,False)
l1=Label(root,text="Enter the name:")
l1.pack()
t1=Entry(root)
t1.pack()
""" def fun():
    name=t1.get()
    l2=Label(root,text="Hello"+" " +name)
    l2.pack() """
def fun():
    name=t1.get()
    x.set(name)
b1=Button(root,text="Submit",command=fun)
b1.pack()
x=StringVar()
t2=Entry(root,textvariable=x)
t2.pack()
root.mainloop()