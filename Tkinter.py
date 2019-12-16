def hello():
    print('Zach is awsome not')


from tkinter import *
tk = Tk()
btn = Button(tk,text='click me', command=hello)
btn.pack()

