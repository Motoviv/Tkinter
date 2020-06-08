from  tkinter import *
from  PIL import  Image, ImageTk
imagenary_tech_root = Tk() #create a basic gui
 #gui logic
 #width x height - gemetory
imagenary_tech_root.geometry("700x334")

#imagenary_tech_root.minsize(300,100) #minimize- width,height

#imagenary_tech_root.maxsize(566,300) #maxsize-width,height

a = Label(text="HAPPY BIRTHDAY")
a.pack()
#for jpg images

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

a1_label =Label(image=photo)
a1_label.pack()
imagenary_tech_root.mainloop()

