from tkinter import *
from functools import *

root=Tk()




def sign():
        top=Toplevel(root)
        top.geometry('400x200')



        Name = StringVar()
        email = StringVar()
        password = StringVar()
        age = StringVar()

        name = Label(top, text="Name").place(x=30, y=50)

        e1 = Entry(top).place(x=80, y=50)

        age = Label(top, text="age").place(x=30, y=90)

        e2 = Entry(top).place(x=80, y=90)

        email = Label(top, text="Email").place(x=30, y=130)

        e2 = Entry(top).place(x=80, y=130)

        password = Label(top, text="Password").place(x=30, y=170)

        e3 = Entry(top).place(x=95, y=170)

        sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=210)
 #       reg()
#def reg():


def login():
        def validateLogin(username, password):
                print("username entered :", username.get())
                print("password entered :", password.get())
                return
        log1=Toplevel(root)
        log1.geometry('400x200')


        username=StringVar()
        password=StringVar()

        usrname=Label(log1,text="username").place(relx=0.0,rely=0.1)
        usrname1=Entry(log1,textvariable=username).place(relx=0.2,rely=0.1)

        pasword = Label(log1, text="password").place(relx=0.0, rely=0.3)
        pasword1 = Entry(log1,textvariable=password,show="*").place(relx=0.2, rely=0.3)

        validateLogin = partial(validateLogin, username, password)


        confrm=Button(log1,text='cofirm',command=validateLogin).place(relx=0.2,rely=0.5)








root.config(bg='skyblue')
root.geometry("200x200")
signup=Button(root,text='sign up', command=sign)
signup.place(relx=0.3,rely=0.3)
signin=Button(root,text='sign in', command=login)
signin.place(relx=0.3,rely=0.5)








root.mainloop()