'''
making an object react to something
'''

# this function takes a single parameter with tkinter
# uses to send info to the function about the event
from tkinter import*
tk=Tk() # tk is my object I create from the class Tk()
canvas= Canvas(tk,width=600, height=600)# specify the size of canvas
canvas.pack() # the variable canvas will be modified by pack() to fit in the
# dimensions specified above
canvas.create_polygon(10,10,10,60,50,35)

def movetriangle(event):
     canvas.move(1,5,0)

canvas.bind_all('<KeyPress-Return>', movetriangle)
