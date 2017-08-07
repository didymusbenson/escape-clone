from tkinter import *
import random


# Define window dimensions
canvas_width = 800
canvas_height = 640

master = Tk()
master.title( "ESCAPE: Race to the Airlock!" )
# Constructor
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
# Tells the window to fill the entire container
w.pack(expand = YES, fill = BOTH)
# w.bind( "<B1-Motion>", paint ) # BIND AN EVENT TO A METHOD
# Confugre lets you mess with settings, change stuff
w.configure(background='#0076c6')

dicepool = Canvas( w )
dicepool.config(width = 780, height = 100)
dicepool.pack(side= BOTTOM, fill=X, padx=10, pady=10)


labels = []
textVars = []
class dice_bag(object):
    faces = ["Roll me!","Yellow","Red","Green","Green","Blue","Black"]
    face_colors = ["#ffffff","#ffff7f","#ff0000","#00ff00","#00ff00","#0000ff","#000000"]

    def get_face(self, num):
        try:
            return self.faces[num]
        except:
            print('Error getting die face.')

    dlocks = [False,False,False,False,False]

    drolls = [0,0,0,0,0]

    def get_locks(self):
        return self.dlocks

    def set_locks(self, dnum, tf_bool):
        self.dlocks[dnum] = tf_bool


    def get_rolls(self):
        return self.drolls

    def get_d_roll(self, dnum):
        return self.drolls[dnum]


    def set_d_roll(self, dnum, roll):
        # original version of this had error handling, this does not.
        self.drolls[dnum] = roll

dbag = dice_bag()


for i in range(5):
    textVars.append(StringVar())
    labels.append(Label(dicepool,textvariable=textVars[i],relief='solid'))
    labels[i].pack(padx=2,pady=2)
    labels[i].configure(background='#FFFFFF')
    textVars[i].set('ROLL ME!')
    dicepool.create_window(50 + i * 90 , 50, window = labels[i] , width = 78, height = 78)

def roll_die():
    return random.randint(1,6)

def roll_dice():
    results = []
    locklist = dbag.get_locks()
    num_to_unlock = 0

    for die in range(len(dbag.get_locks())):
        if locklist[die] == False:
            results.append(roll_die())
        else:
            results.append(dbag.get_d_roll(die))

    for i in range(5):
        textVars[i].set(str(dbag.get_face(results[i])))
        dbag.set_d_roll(i,results[i])
        labels[i].configure(background=dbag.face_colors[results[i]], fg='#000000')


    for i in range(5):
        if results[i] ==  6:
            dbag.set_locks(i, True)
            labels[i].configure(fg='#FFFFFF')
        elif results[i] == 1 :
            num_to_unlock += 2



pool_frame = Frame(dicepool, height=100, width = 120)
pool_frame.pack_propagate(0)
pool_frame.pack(side=RIGHT)

b3 = Button(pool_frame, text="ROLL DICE", command = roll_dice)
b3.pack(fill=X, padx = 10, pady=5)


mainloop()
