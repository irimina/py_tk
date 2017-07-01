# line drawing

from tkinter import *
tiki=Tk()
canvas = Canvas(tiki,width= 500, height= 500)
canvas.pack() # this changes the size as specified before

# now let's draw inside the canvas
canvas.create_line(0,0,500,500) # line in diagonal across the canvas
canvas.create_line(0,250,500,250) # line across the the canvas horizonatally 
