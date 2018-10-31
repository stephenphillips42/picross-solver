# Look up : https://docs.python.org/3/library/tk.html

import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter.messagebox

######## Example 1
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

######## Example 2
top = tkinter.Tk()

C = tkinter.Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()
top.mainloop()

######## Example 2
top = tkinter.Tk()
top.geometry("100x100")
def helloCallBack():
  msg = tkinter.messagebox.showinfo( "Hello Python", "Hello World" )

B = tkinter.Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
