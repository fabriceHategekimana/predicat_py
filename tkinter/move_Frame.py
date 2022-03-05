from tkinter import *
import tkinter.ttk as ttk

ACTIVELABEL = 0

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    #top left coordinate
    x = widget.winfo_x() -widget.startX + event.x
    y = widget.winfo_y() -widget.startY + event.y
    #replace the widget
    widget.place(x=x,y=y)

root = Tk()

frame = Frame(root, bd=10, bg="black")
frame.bind("<Button-1>", drag_start)
frame.bind("<B1-Motion>", drag_motion)
frame.place(x=0, y=0)

label = Label(frame, bg="red", width=10,height=5)
label.pack()

label2 = Label(frame, bg="blue", width=10,height=5)
label2.pack()

label3 = Label(frame, bg="green", width=10,height=5)
label3.pack()

label3 = Label(frame, bg="yellow", width=10,height=5)
label3.pack()

root.mainloop()
