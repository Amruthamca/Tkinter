from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("Count Vowels")
root.configure(bg="pink")
root.resizable(False, False)
l1=Label(root, text="Enter the string:")
l1.pack()
t1=Entry(root)
t1.pack()
def f1():
    string=t1.get()
    vowel_count=0
    for i in string:
        if i.lower() in 'aeiou':
            vowel_count=vowel_count+1
    a.set(format(vowel_count))
b1=Button(root, text="Count Vowels", command=f1)
b1.pack()
a=StringVar()
t2=Entry(root, textvariable=a)
t2.pack()
root.mainloop()
