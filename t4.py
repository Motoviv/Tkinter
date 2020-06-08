from tkinter import *
def getvals():
    print(uservalue.get())
    print(passvalue.get())

root = Tk()
root.geometry("660x360")
user =Label(root,text="usermae")
user.grid()
password = Label(root,text="passwoord")
password.grid(row=1)
#calsses in tkniter
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable =uservalue)
passentry = Entry(root,textvariable =passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text ="submit",command=getvals).grid()
root.mainloop()
