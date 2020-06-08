# handeling events in tkinter
from tkinter import *
def b1(event):
    print("you click on the button")
root=Tk()
root.title("handleing event")
root.geometry("544x334")
widget= Button(root,text="Click me plz")
widget.pack()
widget.bind('<Button-1>',b1)
widget.bind('<Double-1>',quit)

root.mainloop()