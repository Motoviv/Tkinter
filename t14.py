from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scroll Bar")
#for connecting scroll bar to widget
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
lbx=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(344):
  lbx.insert(END,f"Item {i} ")
lbx.pack(fill="both",padx=20)
text=Text(root,yscrollcommand = scrollbar.set) #for text
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
scrollbar.config(command=lbx.yview)



root.mainloop()
