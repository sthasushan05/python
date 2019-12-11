from tkinter import *

HEIGHT=700
WIDTH=800
#starting of the gui program
root=Tk()
root.title("calculator")

#canvas helps to create the height and width of a program
canvas=Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
Label(root,text="calculator").place(relx=0.5,rely=0)
#relheight relwidth hepls to increase the length and height were as relx and rely helps to put the object in right palce
frame=Frame(root,bg="grey")
frame.place(relx=0.5,rely=0.2,relheight=0.15,relwidth=0.35,anchor='n')

username=Label(frame,text="username",bg="blue",fg='white',bd=2)
username.place(relx=0,rely=0,relheight=0.20,relwidth=0.35)

entry=Entry(frame,bd=4)
entry.place(relx=0.3,rely=0,relheight=0.20,relwidth=0.65)

password=Label(frame,text="password",bg="blue",fg='white')
password.place(relx=0,rely=0.2,relheight=0.20,relwidth=0.35)
entry1=Entry(frame,bd=4)
entry1.place(relx=0.3,rely=0.2,relheight=0.20,relwidth=0.65)

button=Button(frame,text="confirm",bg="maroon",fg="white")
button.place(relx=0.4,rely=0.5,relheight=0.20,relwidth=0.35)



root.mainloop()
