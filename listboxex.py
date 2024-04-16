from tkinter import*
root=Tk()
root.geometry("500x400")
l=Listbox(root)
l = Listbox(root)
for i in range(0,100):
    l.insert(i,i)
l.pack()
root.mainloop()
