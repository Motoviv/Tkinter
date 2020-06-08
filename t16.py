#status bar
from tkinter import *
def upload():
    statusvar.set("Bussy")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("READY NOW")

root=Tk()
root.geometry("354x233")
root.title("status bar")

statusvar=StringVar()
statusvar.set("Ready")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()
root.mainloop()