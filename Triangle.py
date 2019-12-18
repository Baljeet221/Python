def movetriangle(event):
    canvas.move(1,5,0)
from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
def movetriangle(event):
    canvas.move(1,5,0)
canvas.bind_all('<KeyPress-Return>', movetriangle)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
def movetriangle(evnet):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
        tk.update()
def down(evnet):
    elif event.keysym == 'Down':
        canvas.move(1,0,3)
tk.update()
def left(evnet):
    elif event.keysym == 'Left':
        canvas.move(1,-3,0)
tk.update()
    else:
        canvas.move(1,3,0)
