from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("Tittle of  my GUI")
#to change icon of title
root.wm_iconbitmap("1.ico")
root.configure(background="pink") #to change in gui use configure

width=root.winfo_screenmmwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close",command= root.destroy).pack()
root.mainloop()