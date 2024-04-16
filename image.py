from tkinter import *
from PIL import ImageTk
root=Tk()
root.geometry("600x500")
img=ImageTk.PhotoImage(file="img1.jpg")
l1=Label(root,image=img)
l1.pack()
root.mainloop()