#calculator
from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text") #take out text from button we use cget

    if text == "=":
         if scvalue.get().isdigit():
             value = int(scvalue.get())
         else:
              try:
                    value=eval(screen.get())
              except Exception as e:
                  print(e)
                  value="ERROR"
                  screen.update()

         scvalue.set(value)
         screen.update()

    elif text == "C":
         scvalue.set("")
         screen.update()
    else:
         scvalue.set(scvalue.get()+text)
         screen.update()


root=Tk()
root.geometry("640x700")
root.title("CALCULATOR")
root.wm_iconbitmap("1.ico")
root.configure(background="grey") #to change in gui use configure

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="luvida 25 bold")
screen.pack(fill=X,ipadx=8,pady=15,padx=15)

f=Frame(root,bg="red")
b=Button(f,text="9",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="8",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="7",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")
b=Button(f,text="6",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="5",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="4",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")
b=Button(f,text="3",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="2",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="1",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")
b=Button(f,text="0",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="C",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="+",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")
b=Button(f,text="/",font="lucida 35 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="%",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="=",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="red")
b=Button(f,text="-",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text="00",font="lucida 35 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

b=Button(f,text=".",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()