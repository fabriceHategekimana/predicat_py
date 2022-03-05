from tkinter import *
import tkinter.ttk as ttk

# s = ttk.Style()
# themes: ('clam', 'alt', 'default', 'classic')
# s.theme_use("classic")

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

window = Tk()

label = Label(window,bg="red", width=10,height=5)
label.place(x=0,y=0)
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2 = Label(window,bg="blue", width=10,height=5)
label2.place(x=100,y=100)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

label3 = Label(window,bg="green", width=10,height=5)
label3.place(x=200,y=200)
label3.bind("<Button-1>", drag_start)
label3.bind("<B1-Motion>", drag_motion)

label3 = Label(window,bg="yellow", width=10,height=5)
label3.place(x=300,y=300)
label3.bind("<Button-1>", drag_start)
label3.bind("<B1-Motion>", drag_motion)

window.mainloop()
