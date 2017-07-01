'''
making an object react to user's keys pressed
using if and elif
'''

# this function takes a single parameter with tkinter
# uses to send info to the function about the event
from tkinter import*
tk=Tk() # tk is my object I create from the class Tk()
canvas= Canvas(tk,width=600, height=600)# specify the size of canvas
canvas.pack() # the variable canvas will be modified by pack() to fit in the
# dimensions specified above
canvas.create_polygon(0,0,0,60,50,35, fill='yellow', outline='blue')

'''
canvas.move(identifier for the shape, value for x, value for y)
'''
def movetriangle(event):
     if event.keysym=='Up':
          canvas.move(1,0,-40)
     elif event.keysym =='Down':
          canvas.move(1,0,10)
     elif event.keysym=='Left':
          canvas.move(1,-3,0)
     elif event.keysym=='Right':
          canvas.move(1,3,0)
     
     
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Up>', movetriangle)

'''
What are other events you can use with this?
mouse, letters, numbers.
It works with 1,2 etc and a,b,c,d etc 

'''
