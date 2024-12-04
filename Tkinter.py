from tkinter import *
import sqlite3
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox

window=Tk()
window.geometry("500x500")
window.title("welcome")


imge=Image.open("C:/Users/ganny/OneDrive/Pictures/profile/blank.png")
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()

menu=Menu(window)
window.config(menu=menu)

def quitt():
    quit()

def abt():
    tkinter.messagebox.showinfo("welcome",'Demo Form!')

def database():
    n1=fn.get()
    l1=ln.get()
    date=dob.get()
    country=con.get()
    prog=varc2
    gender=r1var.get()
    conn=sqlite3.connect("Form.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Last TEXT,DOB TEXT,Country TEXT,Programming TEXT,Gender TEXT)')
    cursor.execute('INSERT INTO Student (Name,Last,DOB,Country,Programming,Gender) VALUES(?,?,?,?,?,?)',(n1,l1,date,country,prog,gender))
    conn.commit()
subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=quitt)

subm1=Menu(menu)
menu.add_cascade(label="Options",menu=subm1)
subm1.add_command(label="About",command=abt)





fn=StringVar()
ln=StringVar()
dob=StringVar()
con=StringVar()
varc1="Java"
varc2="Python"
r1var=StringVar()

# def start():
#     first=fn.get()
#     last=ln.get()
#     dob1=dob.get()
#     con1=con.get()
#     r1=r1var.get()
#     print(f"Your name is {first}{last}")
#     print(f"Your DOB is {dob1}")
#     print(f"Your country is {con1}")
#     print(f"Your Gender is{r1}")
#     tkinter.messagebox.showinfo("welcome",'You are successfully logged in!')


def sec_win():
    root=Tk()
    root.title("welcome to second window")
    root.geometry('250x200')
    lab1=Label(root,text="Registration completed",relief="solid",font=("ariel",12,"bold"))
    lab1.place(x=30,y=80)
    But=Button(root,text="Demo",width="12",fg="white",bg="red",command=abt)
    But.place(x=70,y=120)
def exit():
    print("Quit")

label1=Label(window,text="Registration form",relief="solid",font=("ariel",16,"bold"))
label1.place(x=150,y=30)

label2=Label(window,text="First Name:",font=("ariel",12))
label2.place(x=100,y=130)

entry1=Entry(window,textvariable=fn)
entry1.place(x=250,y=132)

label3=Label(window,text="Last Name:",font=("ariel",12))
label3.place(x=100,y=180)

entry2=Entry(window,textvariable=ln)
entry2.place(x=250,y=182)

label4=Label(window,text="D  O  B:",font=("ariel",12))
label4.place(x=100,y=230)

entry3=Entry(window,textvariable=dob)
entry3.place(x=250,y=232)

label5=Label(window,text="Country:",font=("ariel",12))
label5.place(x=100,y=280)


list1=['India','USA','Canada','japan']
droplist=OptionMenu(window,con,*list1)
con.set("Select Country")
droplist.config(width=15)
droplist.place(x=250,y=282)

label5=Label(window,text="Prog Language:",font=("ariel",12))
label5.place(x=100,y=330)

c1=Checkbutton(window,text="Java",variable=varc1).place(x=250,y=330)
c1=Checkbutton(window,text="Python",variable=varc2).place(x=310,y=330)

r1=Radiobutton(window,text="Male",variable=r1var,value="Male").place(x=250,y=380)
r1=Radiobutton(window,text="Female",variable=r1var,value="Female").place(x=320,y=380)

label5=Label(window,text="Gender:",font=("ariel",12))
label5.place(x=100,y=380)


B1=Button(window,text="Login",width="12",fg="white",bg="red",command=database).place(x=150,y=425)
window.bind("<Return>",database)
B2=Button(window,text="Quit",width="12",fg="white",bg="red",command=exit)
B2.place(x=270,y=425)
B3=Button(window,text="Signup",width="12",fg="white",bg="red",command=sec_win)
B3.place(x=216,y=470)

window.mainloop()