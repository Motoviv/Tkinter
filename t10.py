from tkinter  import  * #menu
import  tkinter.messagebox as tmsg
root =Tk()
root.geometry("700x344")
root.title("pycharm")
def myfunc():
    print("welcome to pycharm")
def help():
    print("i will help you")
    a=tmsg.showinfo("Help","srija will help you")
    print(a)
def rate():
    print("Rate Yourself")
    value= tmsg.askquestion("How Would you like to rate yourself")
    if value == "yes":
        msg="Great!!! Rate us on play store"
    else:
        msg="Tell us why you went wrng.Contact you soon!!"

    tmsg.showinfo("Experienxce",msg)
def anu():
    ans=tmsg.askretrycancel("want to use edit button","i dont want to use edit button")
    if ans:
        print("after retrying nothing will happen")
    else:
        print("Thnx for canceling")

#use this to create a non drop down menu
#mymenu=Menu(root)
#mymenu.add_command(label ="File",command=myfunc)
#mymenu.add_command(label ="Exit",command=quit)
#root.config(menu=mymenu)
#menu1
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="NewProject",command=myfunc)
m1.add_command(label="Open",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_separator()
m1.add_command(label="Print",command=myfunc)
m1.add_command(label="Exit",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

#menu2
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Find",command=myfunc)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Delete",command=myfunc)
m2.add_command(label="Select All",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

#menu3
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Getting Started",command=help)
m3.add_command(label="Tip of The Day",command=myfunc)
m3.add_separator()
m3.add_command(label="Contact support",command=myfunc)
m3.add_command(label="About",command=myfunc)
m3.add_command(label="Find Action",command=myfunc)
m3.add_command(label="RateUs",command=rate)
m3.add_command(label="Use edit button ",command=anu)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)

root.mainloop()