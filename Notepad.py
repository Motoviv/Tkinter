#gui notepad
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
      global  file
      file=askopenfilename(defaultextension=".txt",filetypes=[("All File","*.*"),("Text Documents","*.txt")])
      if file=="":
          file=None
      else:
          root.title(os.path.basename(file) + " - Notepad")
          TextArea.delete(1.0, END)
          f=open(file,"r")
          TextArea.insert(1.0,f.read)
          f.close()

def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='Notepad.txt',defaultextension=".txt",filetypes=[("All File","*.*"),("Text Documents","*.txt")])
        if file== "":
           file=None
        else:
        #save as a new file
              f=open(file,"w")
              f.write(TextArea.get(1.0,END))
              f.close()
              root.title(os.path.basename(file) + "**NOTEPAD**")
              print("FILE SAVED")
    else:
        #save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "**NOTEPAD**")

def quitApp():
     root.destroy()
def cut():
     TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("NOTEPAD","By SRIJA SINHA")

if __name__ == '__main__':
 root=Tk()
root.title("NOTEPAD")
root.wm_iconbitmap("1.ico")
root.configure(background="pink") #to change in gui use configure
root.geometry("640x500")
#add text
TextArea =Text(root,font="lucida 13")
file=None
TextArea.pack(expand=True,fill=BOTH)

#create menu bar

MenuBar = Menu(root)
#file menu starts
FileMenu =Menu(MenuBar,tearoff=0)

#to open new file
FileMenu.add_command(label="New",command=newFile)

#to open already existing file
FileMenu.add_command(label="Open",command=openFile)

# to save current file
FileMenu.add_command(label="Save",command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File",menu=FileMenu)
#file menu ends

#edit menu starts
EditMenu= Menu(MenuBar,tearoff=0)
#to give a feature of cut,copy,paste

EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=EditMenu)
#edid menu ends

#help menu starts
HelpMenu= Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Naotepad",command=about)
MenuBar.add_cascade(label="Help",menu=HelpMenu)
#help menu ends
root.config(menu=MenuBar)

#adding scroll bar in notepad
scroll=Scrollbar(TextArea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)






root.mainloop()