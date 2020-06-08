from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root = Tk()
root.geometry("455x233")
root.title("List Box")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of List Box")


Button(root,text="Add item",command=add).pack()

root.mainloop()
