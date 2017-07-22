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

# CREATE A CLOCK LABEL AND ADD TO CANVAS
clock = Label( w, text = "CLOCK" )
clock.pack()
w.create_window(110,60, window = clock, width = 200, height = 100)



# CREATE A GEM POOL CLASS THAT CONTAINS THE GEM TOTAL
# SERVES AS PRACTICE CREATING PY OBJECTS
class gem_pool(object):
    gems = 0
    def __init__(self, gems):
        self.gems = gems

    def get_gems(self):
        return self.gems

    def set_gems(self, gems):
        self.gems = gems

def make_gem_pool(gems):
    g = gem_pool(20)
    return g

gPool = make_gem_pool(20)

###########################################
# CREATE A GEM POOL LABEL AND ADD TO CANVAS

# Create the text variable for the view
gViewTV = StringVar()
# Create the label
gemView = Label( w, textvariable = gViewTV )
gemView.pack()
w.create_window(270, 60, window = gemView, width = 100, height = 100)

# Set the label to the current amount of gems
gViewTV.set(str(gPool.get_gems()))



##############################################################
# CREATE A TEST BUTTON THAT WILL REMOVE GEMS FROM THE GEM POOL
# AND ANOTHER BUTTON THAT WILL ADD GEMS

# define the method to remove gems
def remove_gem():
    if gPool.get_gems() > 0:
        gPool.set_gems(gPool.get_gems() - 1)
        gViewTV.set(str(gPool.get_gems()))
    else:
        print("no gems to remove")

# Create the button, pack it, and make the window for it in the Canvas
b1 = Button(w, text="REMOVE BATTERY", command=remove_gem)
b1.pack()
w.create_window(270, 130, window = b1, width = 100, height = 20)

# define the method to add gems
def add_gem():
    gPool.set_gems(gPool.get_gems() + 1)
    gViewTV.set(str(gPool.get_gems()))


# Create the button, pack it, and make the window for it in the Canvas
b2 = Button(w, text="ADD BATTERY", command=add_gem)
b2.pack()
w.create_window(270, 160, window = b2, width = 100, height = 20)

##########################################
# CREATE A MESSAGE LABEL AND ADD TO CANVAS
message = Label( w, text = "MESSAGE" )
message.pack()
w.create_window(560, 60, window = message, width = 460, height = 100)

# CREATE A DICE POOL LABEL AND ADD TO CANVAS
dicepool = Canvas( w )
dicepool.pack()
w.create_window(400, 580, window = dicepool, width = 780, height = 100)

############################################################################
# DYNAMICALLY CREATE "DIE" ELEMENTS THIS IS NOT WHAT WILL NEED TO BE DONE
# IN THE FINAL VERSION OF THE GAME, BUT IT'S A STEP IN THE RIGHT DIRECTION
# REGARDING THE LOGIC.

# This will be an array of "Die" objects, which is why I'm not doing
# "For i in range(5)

class dice_bag(object):
    faces = ["Roll me!","Yellow","Red","Green","Green","Blue","Black"]

    def get_face(self, num):
        try:
            return self.faces[num]
        except:
            print('Error getting die face.')

    d1tv = StringVar()
    d2tv = StringVar()
    d3tv = StringVar()
    d4tv = StringVar()
    d5tv = StringVar()

    die1 = Label(dicepool, textvariable = d1tv, borderwidth=2 , relief="solid")
    die1.pack()
    die1.configure(background='#FFFFFF')

    die2 = Label(dicepool, textvariable = d2tv, borderwidth=2 , relief="solid")
    die2.pack()
    die2.configure(background='#FFFFFF')

    die3 = Label(dicepool, textvariable = d3tv, borderwidth=2 , relief="solid")
    die3.pack()
    die3.configure(background='#FFFFFF')

    die4 = Label(dicepool, textvariable = d4tv, borderwidth=2 , relief="solid")
    die4.pack()
    die4.configure(background='#FFFFFF')

    die5 = Label(dicepool, textvariable = d5tv, borderwidth=2 , relief="solid")
    die5.pack()
    die5.configure(background='#FFFFFF')

    # ffff7f = yellow
    d1tv.set("Roll me!")
    d2tv.set("Roll me!")
    d3tv.set("Roll me!")
    d4tv.set("Roll me!")
    d5tv.set("Roll me!")

    d1lock = False
    d2lock = False
    d3lock = False
    d4lock = False
    d5lock = False

    d1roll = 0
    d2roll = 0
    d3roll = 0
    d4roll = 0
    d5roll = 0

    def get_locks(self):
        return [self.d1lock, self.d2lock, self.d3lock, self.d4lock, self.d5lock]



    def get_d_roll(self, dnum):
        if dnum == 1:
            return self.d1roll
        elif dnum == 2:
            return self.d2roll
        elif dnum == 3:
            return self.d3roll
        elif dnum == 4:
            return self.d4roll
        elif dnum == 5:
            return self.d5roll
        else:
            print("Error getting die roll!")

    def set_d_roll(self, dnum, roll):
        if dnum == 1:
            self.d1roll = roll
        elif dnum == 2:
            self.d2roll = roll
        elif dnum == 3:
            self.d3roll = roll
        elif dnum == 4:
            self.d4roll = roll
        elif dnum == 5:
            self.d5roll = roll
        else:
            print("Error setting die roll!")

dbag = dice_bag()

dicepool.create_window(50 + 0 * 90 , 50, window = dbag.die1 , width = 78, height = 78)
dicepool.create_window(50 + 1 * 90 , 50, window = dbag.die2 , width = 78, height = 78)
dicepool.create_window(50 + 2 * 90 , 50, window = dbag.die3 , width = 78, height = 78)
dicepool.create_window(50 + 3 * 90 , 50, window = dbag.die4 , width = 78, height = 78)
dicepool.create_window(50 + 4 * 90 , 50, window = dbag.die5 , width = 78, height = 78)

# ADD A METHOD THAT SETS THE DICE TEXT VARIABLES
#def set_dice_views():
#    dbag.d1tv.set(str(dbag.get_face(0)))
#    dbag.d2tv.set(str(dbag.get_face(1)))
#    dbag.d3tv.set(str(dbag.get_face(2)))
#    dbag.d4tv.set(str(dbag.get_face(3)))
#    dbag.d5tv.set(str(dbag.get_face(4)))
#
#set_dice_views()

def roll_die():
    return random.randint(1,6)

def roll_dice(array):
    results = []
    for die in array:
        if die == False:
            results.append(roll_die())
        else:
            results.append("locked")

    if results[0] != 'locked':
        dbag.d1tv.set(str(dbag.get_face(results[0])))

    if results[1] != 'locked':
        dbag.d2tv.set(str(dbag.get_face(results[1])))

    if results[2] != 'locked':
        dbag.d3tv.set(str(dbag.get_face(results[2])))

    if results[3] != 'locked':
        dbag.d4tv.set(str(dbag.get_face(results[3])))

    if results[4] != 'locked':
        dbag.d5tv.set(str(dbag.get_face(results[4])))

    print(results)


b3 = Button(dicepool, text="ROLL DICE", command = lambda: roll_dice(dbag.get_locks()))
b3.pack()
dicepool.create_window(710, 20, window = b3, width = 100, height = 20)

#roll_dice(dbag.get_locks())


# MAKE THE MAGIC HAPPEN!
mainloop()
