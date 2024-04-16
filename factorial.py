from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("Factorial")
root.configure(bg="grey")
root.resizable(False,False)
l1=Label(root, text="Enter the number:")
l1.pack()
t1=Entry(root)
t1.pack()
def f1():
    n=int(t1.get())
    fact=1 
    for i in range(1,n+1):
        fact *= i
    x.set(fact)
b1=Button(root,text="factorial",command=f1)
b1.pack()
x=StringVar()
t2=Entry(root,textvariable=x)
t2.pack() 
root.mainloop()