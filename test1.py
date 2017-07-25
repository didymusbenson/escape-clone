from tkinter import *

def make_view():
    master = Tk()
    master.title( "Example" )
    w = Canvas(master, width=200, height=200)
    w.pack(expand = YES, fill = BOTH)
    w.configure(background='#0076c6')


    gViewTV = StringVar()
    gemView = Label( w, textvariable = gViewTV )
    gemView.pack()
    w.create_window(100, 40, window = gemView, width = 100, height = 40)
    gViewTV.set(20)

    b1 = Button(w, text="-1", command=remove_gem)
    b1.pack()
    w.create_window(100, 120, window = b1, width = 100, height = 100)

