from tkinter import *

master = Tk()
master.title( "EXAMPLE" )
w = Canvas(master,
           width=800,
           height=120)
w.pack(expand = YES, fill = BOTH)
w.configure(background='#0076c6')

# CREATE A DICE POOL LABEL AND ADD TO CANVAS
dicepool = Canvas( w )
dicepool.pack()
w.create_window(400, 60, window = dicepool, width = 780, height = 100)

# DICE DICTIONARY (currently unused)
dice_d = {}

# DICE ARRAY (will ultimately be an array of DIE objects)
dice = [1,2,3,4,5]
i = 0
for die in dice:
    dice_d["die_tv{0}".format(die)] = "DIE"

    lb = Label(dicepool, text = "DIE", borderwidth=2 , relief="solid")
    lb.pack()
    lb.configure(background='#FFFF7F')
    dicepool.create_window(50 + i * 90 , 50, window = lb, width = 78, height = 78)
    i += 1

# RUN
mainloop()
