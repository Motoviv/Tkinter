from  tkinter import *
root = Tk()
root.geometry("660x360")
def hello():
    print("Have A Long Life")
f1= Frame(root,bg="blue",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

b1=Button(f1,fg="black",text="print now",command =hello)
b1.pack(padx=12)

f2= Frame(root,bg="yellow",borderwidth=6,relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l= Label(f1,text="may ur all dresms come true")
l.pack(pady=140)

l= Label(f2,text="HAPPY BIRTHDAY")
l.pack()

root.mainloop()