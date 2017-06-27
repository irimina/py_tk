from tkinter import *
import time
tk =Tk()
canvas= Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)              
canvas.create_text(100,100, text='This is a lovely text', fill='red')
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
     canvas.move(1,5,0)
     canvas.move(2,3,0)
     canvas.move(3,5,5)
     tk.update()
     time.sleep(0.05)

for x in range(0,60):
     canvas.move(1,-5,0)
     canvas.move(2,-3,0)
     canvas.move(3,-5,-5)
     tk.update()
     time.sleep(0.01)

'''    
for x in range(0,60):
     canvas.move(2,3,0)
     tk.update()
     time.sleep(0.05)

     
for x in range(0,60):
     canvas.move(3,5,5)
     tk.update()
     
 '''    
