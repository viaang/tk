from tkinter import *

window = Tk()

window.title("Hello world")
window.geometry("400x400")

text = Label(text = "hi", bg = "green",fg = "blue" )
text.pack()
name = Entry()
name.pack()
def display( ) :
    namer = name.get()
    big_text.insert(END,"hello")

big_text = Text(height = "6")
big_text.pack()







button = Button(text = "press me", fg = 'orange', height = '2', width = "4", command = display)
button.pack()


window.mainloop()

