from tkinter import *
from  PIL import  Image, ImageTk

def every_100(text):
    final_text =""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return  final_text
root= Tk()
root.title("Newsspaper")
root.geometry("900x900")
texts=[]
photos=[]

for i in range(0,3):
    with open(f"{i+1}.txt") as f:
      text = f.read()
      texts.append(every_100(text))

image= Image.open(f"{i+1}.jpg")
photo = ImageTk.PhotoImage(image)
#resize this images
image=image.resize((250,200),Image.ANTIALIAS)

photos.append(ImageTk.PhotoImage(image))
p=Frame(root,width=800,height=70)
Label(p,text="Todays News",font ="lucida 20 bold",bg="pink").pack()
Label(p,text="24 MAY,2020",font ="lucida 13 bold",bg="grey").pack()
p.pack(anchor="nw")

f1=Frame(root,width=900,height=200)
Label(f1,text=texts[0],padx=15,pady=15).pack(side="left")
Label(f1,image=photos[0]).pack(side="left")
f1.pack()

f2=Frame(root,width=600,height=200,pady=13)
Label(f2,text=texts[1],padx=15,pady=15).pack(side="right")
Label(f2,image=photos[0],anchor="e").pack(side="left")
f2.pack()

f3=Frame(root,width=300,height=400,pady=13)
Label(f3,text=texts[2],padx=15,pady=15).pack(side="left")
Label(f3,image=photos[0],anchor="e").pack(side="left")
f3.pack()

root.mainloop()