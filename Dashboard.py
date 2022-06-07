from tkinter import *
from tkinter import Menu
from tkinter import messagebox
window = Tk()

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()

def save():
        messagebox.showinfo("Save this file")

window.title("Welcome to Dashboard")
menu = Menu(window)
new_item = Menu(menu)
#you may notice a dashed line at the beginning, well, if you click that line, it will show the menu items in a small separate window.
#You can disable this feature by disabling the tearoff feature like this:
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='New' , command=openNewWindow)
new_item.add_separator()
new_item.add_command(label='Save', command=save)
new_item.add_command(label='Save AS')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()