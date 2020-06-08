from  tkinter import *
import  tkinter.messagebox as tmsg
root= Tk()
root.geometry("450x300")
root.title("Slider Gui")
def getdollar():
    print(f"we have credited{myslider2.get()} dollars to your bank account")
    a=tmsg.showinfo("Amount credited ",f"{myslider2.get()} dollars to your bank account")

#myslider = Scale(root,from_=0,to=100) vertical scaler
#myslider.pack()
Label(root,text ="How many dollars do you want?",font="bold",fg="red",bg="grey").pack()
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
#myslider2.set(30) #initial value
Button(root,text="Get Dollars",padx=10,pady=10,font=30,bg="yellow",command=getdollar).pack()
myslider2.pack()

root.mainloop()