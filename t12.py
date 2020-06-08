from tkinter import *
from tkinter  import  * #menu
import  tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x354")
root.title("Radio button")
def order():
    tmsg.showinfo("Order recieved",f"we have recieved your order for {var.get()}.Thnx for ordering")

var=IntVar()
var =StringVar()
var.set("Radio")
Label(root,text="What would you like to have sir?",justify=LEFT,bg= "red",padx=15,font="bold 17" ).pack()
radio = Radiobutton(root,text="Dosa",padx=13,variable = var,value="Dosa",font=22).pack(anchor="nw")
radio = Radiobutton(root,text="Idli",padx=13,variable =var,value="Idli",font=22).pack(anchor="nw")
radio = Radiobutton(root,text="Samosa",padx=13,variable =var,value="Samosa",font=22).pack(anchor="nw")
radio = Radiobutton(root,text="Sandwich",padx=13,variable =var,value="Sandwich",font=22).pack(anchor="nw")
radio = Radiobutton(root,text="Piza",padx=13,variable =var,value="Piza",font=22).pack(anchor="nw")
Button(text="order now",command=order).pack()
root.mainloop()