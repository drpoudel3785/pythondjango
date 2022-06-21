from tkinter import *
from  tkinter import  ttk
import datetime
#importing connection
import sqlite3

# create connection to database
cnt = sqlite3.connect('sql.db')
cursor = cnt.cursor()

#defining register function
def register():
    #getting form data
    id1 = int(id.get())
    username1=username.get()
    password1=password.get()
    email1=email.get()
    phone1=phone.get()
    usertype1=int(usertype.get())
    status1=status.get()
    createddate = datetime.date.today()
    updateddate = datetime.date.today()
    #applying empty validation
    if id1=='' or username1==''or password1=='' or email1==''or phone1==''or usertype1=='' or status1=='' :
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = cnt.cursor()


       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = ("INSERT INTO users(id , username , password , email , phone , usertype , status , createddate , updateddate) VALUES (?,?,?,?,?,?,?,?,?)"
       )
       if usertype1==1:
            data = (id1, username1 , password1 , email1 , phone1 , "admin" , status1 , createddate , updateddate)
       else:
           data = (id1 , username1 , password1 , email1 , phone1 , "user" , status1 , createddate , updateddate)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           cnt.commit()
       except:
           cnt.rollback()
       message.set("Data INseted")

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global  message;
    global id
    global username
    global password
    global email
    global phone
    global usertype
    global status
    global createddate
    global updateddate
    id = IntVar()
    username = StringVar()
    password=StringVar()
    email=StringVar()
    phone=StringVar()
    usertype=IntVar()
    status=StringVar()
    createddate=StringVar()
    updateddate=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    # id Label
    Label(reg_screen, text="ID * ").place(x=20, y=40)
    # name textbox
    Entry(reg_screen, textvariable=id).place(x=90, y=42)

    #name Label
    Label(reg_screen, text="UserName * ").place(x=20,y=80)
    #name textbox
    Entry(reg_screen, textvariable=username).place(x=90,y=82)

    # Password Label
    Label(reg_screen, text="Password * ").place(x=20, y=120)
    # name textbox
    Entry(reg_screen, textvariable=password).place(x=90, y=122)


    # email Label
    Label(reg_screen, text="Email * ").place(x=20, y=160)
    # email textbox
    Entry(reg_screen, textvariable=email).place(x=90, y=162)

    # Phone Label
    Label(reg_screen, text="Phone * ").place(x=20, y=200)
    # contact textbox
    Entry(reg_screen, textvariable=phone).place(x=90, y=202)

    # User Label
    Label(reg_screen, text="Usertype * ").place(x=20, y=240)
    # usertype radiobutton
    Radiobutton(reg_screen,text="Admin",variable=usertype,value=1).place(x=90,y=240)
    Radiobutton(reg_screen, text="User", variable=usertype, value=2).place(x=150, y=242)

    # status Label
    Label(reg_screen, text="Status * ").place(x=20, y=280)
    # city combobox
    statuschoosen = ttk.Combobox(reg_screen, width=27, textvariable=status)
    statuschoosen['values'] = (' Active',
                              ' Decative',
                            )
    statuschoosen.current()
    statuschoosen.place(x=90,y=282)

    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=304)
    #Login button
    Button(reg_screen, text="Register", width=10, height=1, bg="orange",command=register).place(x=105,y=330)
    reg_screen.mainloop()

#calling function Registrationform
Registrationform()
