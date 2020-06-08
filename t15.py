from tkinter import *
def update():
    print("updateing gui")
    root.geometry(f"{width.get()}x{height.get()}")
root=Tk()
root.geometry("344x233")

width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="APPLY",command=update).pack()
root.mainloop()