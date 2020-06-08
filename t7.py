from tkinter import *
root =Tk()
canvas_width =800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("canvas")
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
#line goes from the point x1 ,y1 to x2 ,y2
can_widget.create_line(0,0,800,400,fill="pink")
can_widget.create_line(0,400,800,0,fill="green")
#top left and bottom right cordinates in rectactangle
can_widget.create_rectangle(6,6,266,266,fill="grey")
#create text cprdinate-
can_widget.create_text(400,200,text="HAPPY BIRTHDAY",fill="red")
can_widget.create_oval(6,6,266,266,fill="red")
can_widget.canvasy(500,200)

root.mainloop()