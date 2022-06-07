from tkinter import *
from tkinter import messagebox

def clicked():
    lbl.configure(text="Button was clicked !!")
    res = txt.get()
    numone = int(num1.get())
    numtwo=int(num2.get())
    sum = numone+numtwo
    lblsum.configure(text = sum)

    messagebox.showinfo('The Sum is :  ', sum)
    # res = messagebox.askquestion('Message title','Message content')
    # res = messagebox.askyesno('Message title','Message content')
    # res = messagebox.askyesnocancel('Message title','Message content')
    # res = messagebox.askokcancel('Message title','Message content')
    # res = messagebox.askretrycancel('Message title','Message content')


window = Tk()
window.geometry("600x400")
window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl1 = Label(window, text="World", font=("Arial Bold", 50))
lbl1.grid(column=3, row=3)

lblsum = Label(window, font=("Arial Bold", 20))
lblsum.grid(column=0, row=4)

#TextBox
#state='disabled'
txt = Entry(window,width=30)
txt.grid(column=5, row=5)
#Add a placeholder in the entry Widget
txt.insert(0, "Enter your Name")

num1 = Entry(window,width=30)
num1.grid(column=1, row=1)

num2 = Entry(window,width=30)
num2.grid(column=2, row=1)
#Set focus to the entry widget
txt.focus()



#adding button
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)

btn.grid(column=2, row=3)
window.mainloop()