from tkinter import *

def cal(b):
    n=t1.get()
    if b == "=":
        operator=None
        for op in ['+','-','*','/']:
            if op in n:
                operator=op
                break

        if operator is not None:
            num1,num2=n.split(operator)
            if operator=='+':
                result=float(num1)+float(num2)
            elif operator=='-':
                result=float(num1)-float(num2)
            elif operator=='*':
                result=float(num1)*float(num2)
            elif operator=='/':
                if float(num2)!=0:
                    result=float(num1)/float(num2)
                else:
                    t1.delete(0, END)
                    t1.insert(END, "Error")
                    return
        else:
            t1.delete(0, END)
            t1.insert(END, "Error")
            return

        t1.delete(0, END)
        t1.insert(END, str(result))
    
    elif b == "Clear":
        t1.delete(0, END)
    
    else:
        t1.insert(END, b)

root = Tk()
root.title("Simple Calculator")
root.config(bg="orange")
t1 = Entry(root, font=("Arial", 20), justify='left')
t1.grid(row=0, column=0, columnspan=4, pady=8)

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "0", "Clear", "=", "/",
    "."
]

r = 1
c = 0
for b in buttons:
    b1 = Button(root,text=b,font=("Arial", 10), padx=20, pady=20, command=lambda text=b: cal(text))
    b1.grid(row=r,column=c,padx=5,pady=5)
    
    c=c + 1
    if c>3:
        c=0
        r=r+1

root.mainloop()
