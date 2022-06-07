from tkinter import *

#tk widget toolkit
#tkinter pythong interface
root = Tk()
#GUI logic

root.title("LABA Python Training")
root.iconbitmap("favicon.ico")
root.minsize(300, 100)
root.maxsize(1200,900)
lbl = Label(root, text="Hello")
lbl.grid(column=1, row=3)
lbl1 = Label(root, text="World", font=("Arial Bold", 50))
lbl1.grid(column=3, row=3)
lbl.pack()
#GUI window
root.mainloop()
