from tkinter import *
root = Tk()
def getvals():
 print("It Works")

root.geometry("660x360")

#heading for form
Label(root,text="welcome to srija travels",font="aerial 13 bold",relief= SUNKEN,bg="red").grid(row=0,column=1)
#entry for text
name =Label(root,text ="NAME",relief=SUNKEN,bg="pink",font=30)
gender =Label(root,text ="GENDER",relief=SUNKEN,bg="pink",font=30)
contact =Label(root,text ="CONTACT",relief=SUNKEN,bg="pink",font=30)
paymentmode =Label(root,text ="PAYMENTMODE",relief=SUNKEN,bg="pink",font=30)
city =Label(root,text ="CITY",relief= SUNKEN,bg="pink",font=30)

#pack the text for a form
name.grid(row=1,column=2)
gender.grid(row=2,column=2)
contact.grid(row=3,column=2)
paymentmode.grid(row=4,column=2)
city.grid(row=5,column=2)

#variable for storeing entries
namevalue = StringVar()
gendervalue = StringVar()
contactvalue = StringVar()
paymentmodevalue = StringVar()
cityvalue = StringVar()
FoodServicevalue = IntVar() #checkbox

#entry for a form
nameentry =Entry(root,textvariable=namevalue,)
genderentry =Entry(root,textvariable=gendervalue)
contactentry =Entry(root,textvariable=contactvalue)
paymentmodeentry =Entry(root,textvariable=paymentmodevalue)
cityentry =Entry(root,textvariable=cityvalue)
FoodService =Entry(root,textvariable = FoodServicevalue)

#pack
nameentry.grid(row=1,column=3)
genderentry.grid(row=2, column=3)
contactentry.grid(row=3, column=3)
paymentmodeentry.grid(row=4, column=3)
cityentry.grid(row=5, column=3)

#Foodservice checkbox and packeing it
FoodService =Checkbutton(text="want to pre book your meal",bg= "grey",fg="yellow",font= 20,variable=FoodServicevalue)
FoodService.grid(row=6, column=3)

#button make and pack it
Button(text ="submit to srija travels",font=30,fg="red",command=getvals).grid(row=7,column=3)


root.mainloop()