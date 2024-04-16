from tkinter import *
from tkinter import messagebox
root=Tk()
#messagebox.showinfo("Information","This is information")
#messagebox.showwarning("Warning","This is warning")
#messagebox.showerror("Error","This is error")
#messagebox.askquestion("Confirm","Are you sure?")
#messagebox.askokcancel("Ask ok cancel","aare u sure?")
messagebox.askretrycancel("Ask retry","try again?")
root.mainloop()