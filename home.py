from tkinter import*
from tkinter import messagebox
import mysql.connector
root=Tk()
root.geometry("350x400")
root.title("Welcome")

def fun():
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='tkinter1'
    )
    mycursor=mydb.cursor()

def login():
    global root2
    root2=Toplevel(root)
    root2.title("Login")
    root2.geometry("500x400")
    global username1,password1
    username1=StringVar()
    password1=StringVar()
    l=Label(root2,text="Login Here",font="bold")
    l.place(x=200,y=8)
    l1=Label(root2,text="Username")
    l1.place(x=50,y=50)
    t1=Entry(root2,textvariable=username1)
    t1.place(x=180,y=50)
    l1=Label(root2,text="Password")
    l1.place(x=50,y=100)
    t1=Entry(root2,textvariable=password1)
    t1.place(x=180,y=100)
    b3=Button(root2,text="Login",width=15,command=log)
    b3.place(x=100,y=150)
b1=Button(root,text="Login",width=10,command=login)
b1.place(x=145,y=100)

def register():
    global root1
    root1=Toplevel(root)
    root1.title("Registration")
    root1.geometry("500x400")
    global username,password,firstname,lastname
    username=StringVar()
    password=StringVar()
    firstname=StringVar()
    lastname=StringVar()
    l=Label(root1,text="Register Here",font="bold")
    l.place(x=200,y=10)
    l1=Label(root1,text="username")
    l1.place(x=50,y=50)
    t1=Entry(root1,textvariable=username)
    t1.place(x=180,y=50)
    l1=Label(root1,text="password")
    l1.place(x=50,y=100)
    t1=Entry(root1,textvariable=password)
    t1.place(x=180,y=100)
    l1=Label(root1,text="firstname")
    l1.place(x=50,y=150)
    t1=Entry(root1,textvariable=firstname)
    t1.place(x=180,y=150)
    l1=Label(root1,text="lastname")
    l1.place(x=50,y=200)
    t1=Entry(root1,textvariable=lastname)
    t1.place(x=180,y=200)
    b3=Button(root1,text="Register",command=reg)
    b3.place(x=180,y=250)
b2=Button(root,text="Register",width=10,command=register)
b2.place(x=145,y=150)
def reg():
    fun()

    user_name=username.get()
    pswd=password.get()
    first_name=firstname.get()
    last_name=lastname.get()

    if user_name=="" or pswd=="" or first_name=="" or last_name=="":
       l1=Label(root1,text="Please complete the form",fg="red") 
       l1.place(x=200,y=300)
    else:
        sql='SELECT * FROM registration WHERE username=%s'
        value=(user_name,)
        mycursor.execute(sql,value)

        if mycursor.fetchone() is not None:
            l1=Label(root1,text="Username already exist!!",fg="red")
            l1.place(x=200,y=300)
        else:
            sql="INSERT INTO registration VALUES(%s,%s,%s,%s)"
            value=(user_name,pswd,first_name,last_name)
            mycursor.execute(sql,value)
            mydb.commit()
            messagebox.showinfo("Registration successfull","Registration successfully completed")

def log():
    fun()

    global user_name1
    user_name1=username1.get()
    pswd1=password1.get()
    if user_name1=="" or password1=="":
        l1=Label(root2,text="Please enter both username and password",fg='red')
        l1.place(x=50,y=200)
    else:
        sql='SELECT * FROM registration  WHERE username=%s AND password=%s'
        value=(user_name1,pswd1)
        mycursor.execute(sql,value)

        if mycursor.fetchone() is not None:
            logpage(user_name1)
        else:
            messagebox.showwarning("Access denied","Access denied")

def logpage(user_name1):
    global root3,uname
    root3=Toplevel(root)
    root3.title('welcome')
    root3.geometry('500x300')
    uname=user_name1
    l1=Label(root3,text='WELCOME'+' '+uname)
    l1.pack()
    b1=Button(root3,text='Change Password',width=15,command=lambda:update(uname))
    b1.place(x=180,y=70)
    b1=Button(root3,text='Delete Account',width=15,command=lambda:delete(uname))
    b1.place(x=180,y=130)
    
def update(uname):
    global root4
    root4=Toplevel(root3)
    root4.geometry('500x300')
    root4.title('Change Password')
    global newpswd,uname1
    uname1=uname
    newpswd=StringVar()
    l1=Label(root4,text="Enter new password")
    l1.place(x=50,y=80)
    t1=Entry(root4,textvariable=newpswd)
    t1.place(x=170,y=80)
    b1=Button(root4,text="Update Password",command=lambda:update1(uname1))
    b1.place(x=50,y=120)

def update1(uname1):
    fun()
    global newpswd1
    newpswd1=newpswd.get()
    uname2=uname1
    if newpswd1=="":
        l1=Label(root4,text="Please enter new password",fg='red')
        l1.place(x=80,y=200)
    else:
        sql='UPDATE registration SET password=%s WHERE username=%s'
        value=(newpswd1,uname2,)
        mycursor.execute(sql,value)
        mydb.commit() 
        messagebox.showinfo('Updated','Updated Successfully')

def delete(uname):
    fun()

    sql="DELETE FROM registration WHERE username=%s"
    value=(uname,)
    mycursor.execute(sql,value)
    mydb.commit()
    messagebox.showinfo("Delete","Deleted successfully")
    
root.mainloop()