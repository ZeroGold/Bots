import time
from tkinter import *



class var:
    def __init__(self, y = 0):
        self.y = y
    def setVar(self, x):
        self.y = x
    def getVar(self):
        return self.y




var = var()
interface = Tk()
interface.geometry('480x320')
frame = Frame(interface)
text = Label(text="Placeholder")
frame.pack()
button = Button(interface,text="Press This",command = lambda:doThis(1))
button.pack()
text.configure(text="Hello!", font=40)
interface.update()
text.place(x=100,y=100)
button.place(x=150,y=150)

def window():
    interface.deiconify()
    interface.mainloop()
    


    
def doThis(x):
    var.setVar(x)
    interface.quit()

while True:
    window()
    if var.getVar() == 1:
        time.sleep(2)
        text.configure(text="Bad Idea! >:(",font=40)
        interface.update()
        time.sleep(5)
        text.configure(text="!!!Now hacking you!!!",font=40)
        interface.update()
        text.place(x=100,y=100)
        time.sleep(5)
        text.configure(text="Just kidding! :)")
        interface.update()
        quit()
