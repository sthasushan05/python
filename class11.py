from tkinter import *

def display(a, b):
    top = Toplevel(root)
    HEIGHT1=200
    WIDTH1=300

    can=Canvas(top,height=HEIGHT1,width=WIDTH1)
    can.pack()
    Label(top, text="name :" + a, font=("", 20),bg="red").place(relx=0,rely=0)
    Label(top, text="age :" + b, font=("", 20)).place(relx=0,rely=0.2)
    Button(top, text="confirm", command=lambda: top.destroy()).place(relx=0.1,rely=0.4,relheight=0.2,relwidth=0.3)
    print(a, b)


HEIGHT = 600
WIDTH = 700
root = Tk()
root.config(bg="grey")
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg='skyblue')
frame.place(relx=0.5, rely=0.15, relheight=0.30, relwidth=0.60, anchor='n')

name = StringVar()
agge = StringVar()
gender=StringVar()
s = Label(frame, text='username', bg="light green", fg='orange')
s.place(relx=0.1, rely=0.0, relheight=0.15, relwidth=0.15)
username = Entry(frame, textvariable=name, bg='purple', fg='violet')
username.place(relx=0.25, rely=0.0, relheight=0.15, relwidth=0.50)

s1 = Label(frame, text='age', bg="light green", fg='orange')
s1.place(relx=0.1, rely=0.2, relheight=0.15, relwidth=0.15)
age = Entry(frame, textvariable=agge, bg='purple', fg='violet')
age.place(relx=0.25, rely=0.2, relheight=0.15, relwidth=0.50)

button = Button(frame, text='submit', bg='maroon', fg='white', command=lambda: display(name.get(), agge.get()))
button.place(relx=0.4, rely=0.5, relheight=0.15, relwidth=0.15)

root.mainloop()
