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


# THIS BUTTON IS FOR TESTING PURPOSES ONLY.
#b2 = Button(w, text="ADD BATTERY", command=add_gem)
#b2.pack()
#w.create_window(270, 160, window = b2, width = 100, height = 20)

##########################################
# CREATE A MESSAGE LABEL AND ADD TO CANVAS
message = Label( w, text = "MESSAGE" )
message.pack()
w.create_window(560, 60, window = message, width = 460, height = 100)

# CREATE A DICE POOL LABEL AND ADD TO CANVAS
dicepool = Canvas( w )
dicepool.pack()
w.create_window(400, 580, window = dicepool, width = 780, height = 100)


def swap_lock(n):
    locklist = dbag.get_locks()
    rolls = dbag.get_rolls()
    if (locklist[n] == True and rolls[n] != 6):
        locklist[n] = False
    elif (locklist[n] == False and rolls[n] != 6):
        locklist[n] = True
    dbag.set_locks(n + 1, locklist[n])

# declare die textvariables
d1tv = StringVar()
d2tv = StringVar()
d3tv = StringVar()
d4tv = StringVar()
d5tv = StringVar()
# dice labels
die1 = Button(dicepool, textvariable = d1tv, relief="solid", command= lambda: swap_lock(0))
die1.pack(padx=2,pady=2)
die1.configure(background='#FFFFFF')
die2 = Button(dicepool, textvariable = d2tv, relief="solid", command= lambda: swap_lock(1))
die2.pack(padx=2,pady=2)
die2.configure(background='#FFFFFF')
die3 = Button(dicepool, textvariable = d3tv, relief="solid", command= lambda: swap_lock(2))
die3.pack(padx=2,pady=2)
die3.configure(background='#FFFFFF')
die4 = Button(dicepool, textvariable = d4tv, relief="solid", command= lambda: swap_lock(3))
die4.pack(padx=2,pady=2)
die4.configure(background='#FFFFFF')
die5 = Button(dicepool, textvariable = d5tv, relief="solid", command= lambda: swap_lock(4))
die5.pack(padx=2,pady=2)
die5.configure(background='#FFFFFF')
# ffff7f = yellow
d1tv.set("Roll me!")
d2tv.set("Roll me!")
d3tv.set("Roll me!")
d4tv.set("Roll me!")
d5tv.set("Roll me!")

dicepool.create_window(50 + 0 * 90 , 50, window = die1 , width = 78, height = 78)
dicepool.create_window(50 + 1 * 90 , 50, window = die2 , width = 78, height = 78)
dicepool.create_window(50 + 2 * 90 , 50, window = die3 , width = 78, height = 78)
dicepool.create_window(50 + 3 * 90 , 50, window = die4 , width = 78, height = 78)
dicepool.create_window(50 + 4 * 90 , 50, window = die5 , width = 78, height = 78)

############################################################################
# DYNAMICALLY CREATE "DIE" ELEMENTS THIS IS NOT WHAT WILL NEED TO BE DONE
# IN THE FINAL VERSION OF THE GAME, BUT IT'S A STEP IN THE RIGHT DIRECTION
# REGARDING THE LOGIC.

# This will be an array of "Die" objects, which is why I'm not doing
# "For i in range(5)

class dice_bag(object):
    faces = ["Roll me!","Yellow","Red","Green","Green","Blue","Black"]
    face_colors = ["#ffffff","#ffff7f","#ff0000","#00ff00","#00ff00","#0000ff","#000000"]

    def get_face(self, num):
        try:
            return self.faces[num]
        except:
            print('Error getting die face.')

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

    def set_locks(self, dnum, tf_bool):
        if dnum == 1:
            self.d1lock = tf_bool
        elif dnum == 2:
            self.d2lock = tf_bool
        elif dnum == 3:
            self.d3lock = tf_bool
        elif dnum == 4:
            self.d4lock = tf_bool
        elif dnum == 5:
            self.d5lock = tf_bool
        else:
            print("Error setting die locks!")

    def get_rolls(self):
        return [self.d1roll, self.d2roll, self.d3roll, self.d4roll, self.d5roll]

    def get_d_roll(self, dnum):
        if dnum == 0:
            return self.d1roll
        elif dnum == 1:
            return self.d2roll
        elif dnum == 2:
            return self.d3roll
        elif dnum == 3:
            return self.d4roll
        elif dnum == 4:
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

def unlock_sixes(n):
    locklist = dbag.get_locks()
    rolls = dbag.get_rolls()
    unlocked = 0
    for i in range(len(locklist)):
        if (locklist[i] == True and rolls[i] == 6 and unlocked < n):
            rolls[i] = 0
            locklist[i] = False
            unlocked += 1

    if locklist[0] == False:
        dbag.set_locks(1, False)
        die1.config(highlightbackground="#000000")
    if locklist[1] == False:
        dbag.set_locks(2, False)
        die2.config(highlightbackground="#000000")
    if locklist[2] == False:
        dbag.set_locks(3, False)
        die3.config(highlightbackground="#000000")
    if locklist[3] == False:
        dbag.set_locks(4, False)
        die4.config(highlightbackground="#000000")
    if locklist[4] == False:
        dbag.set_locks(5, False)
        die5.config(highlightbackground="#000000")


def roll_die():
    return random.randint(1,6)

def roll_dice():
    results = []
    for die in range(len(dbag.get_locks())):
        locklist = dbag.get_locks()
        if locklist[die] == False:
            results.append(roll_die())
        else:
            results.append(dbag.get_d_roll(die))

    d1tv.set(str(dbag.get_face(results[0])))
    dbag.set_d_roll(1, results[0])
    die1.configure(background=dbag.face_colors[results[0]], fg="#000000")
    d2tv.set(str(dbag.get_face(results[1])))
    dbag.set_d_roll(2, results[1])
    die2.configure(background=dbag.face_colors[results[1]], fg="#000000")
    d3tv.set(str(dbag.get_face(results[2])))
    dbag.set_d_roll(3, results[2])
    die3.configure(background=dbag.face_colors[results[2]], fg="#000000")
    d4tv.set(str(dbag.get_face(results[3])))
    dbag.set_d_roll(4, results[3])
    die4.configure(background=dbag.face_colors[results[3]], fg="#000000")
    d5tv.set(str(dbag.get_face(results[4])))
    dbag.set_d_roll(5, results[4])
    die5.configure(background=dbag.face_colors[results[4]], fg="#000000")

    num_to_unlock = 0

    if results[0] ==  6:
        dbag.set_locks(1, True)
        die1.configure(fg="#FFFFFF")
    elif results[0] == 1:
        num_to_unlock += 2

    if results[1] ==  6:
        dbag.set_locks(2, True)
        die2.configure(fg="#FFFFFF")
    elif results[1] == 1:
        num_to_unlock += 2

    if results[2] ==  6:
        dbag.set_locks(3, True)
        die3.configure(fg="#FFFFFF")
    elif results[2] == 1:
        num_to_unlock += 2

    if results[3] ==  6:
        dbag.set_locks(4, True)
        die4.configure(fg="#FFFFFF")
    elif results[3] == 1:
        num_to_unlock += 2

    if results[4] ==  6:
        dbag.set_locks(5, True)
        die5.configure(fg="#FFFFFF")
    elif results[4] == 1:
        num_to_unlock += 2

    unlock_sixes(num_to_unlock)

    #print(dbag.get_locks())
    #print(results)

def reset_sixes():
    if dbag.get_d_roll(0) == 6:
        d1tv.set(str(dbag.get_face(0)))
        dbag.set_d_roll(1, 0)
        die1.configure(background=dbag.face_colors[0], fg="#000000")
    if dbag.get_d_roll(1) == 6:
        d2tv.set(str(dbag.get_face(0)))
        dbag.set_d_roll(2, 0)
        die2.configure(background=dbag.face_colors[0], fg="#000000")
    if dbag.get_d_roll(2) == 6:
        d3tv.set(str(dbag.get_face(0)))
        dbag.set_d_roll(3, 0)
        die3.configure(background=dbag.face_colors[0], fg="#000000")
    if dbag.get_d_roll(3) == 6:
        d4tv.set(str(dbag.get_face(0)))
        dbag.set_d_roll(4, 0)
        die4.configure(background=dbag.face_colors[0], fg="#000000")
    if dbag.get_d_roll(4) == 6:
        d5tv.set(str(dbag.get_face(0)))
        dbag.set_d_roll(5, 0)
        die5.configure(background=dbag.face_colors[0], fg="#000000")

def reset_dice():
    for i in range(5):
        dbag.set_locks(i + 1, False))
    d1tv.set(str(dbag.get_face(0)))
    dbag.set_d_roll(1, 0)
    die1.configure(background=dbag.face_colors[0], fg="#000000")
    d2tv.set(str(dbag.get_face(0)))
    dbag.set_d_roll(2, 0)
    die2.configure(background=dbag.face_colors[0], fg="#000000")
    d3tv.set(str(dbag.get_face(0)))
    dbag.set_d_roll(3, 0)
    die3.configure(background=dbag.face_colors[0], fg="#000000")
    d4tv.set(str(dbag.get_face(0)))
    dbag.set_d_roll(4, 0)
    die4.configure(background=dbag.face_colors[0], fg="#000000")
    d5tv.set(str(dbag.get_face(0)))
    dbag.set_d_roll(5, 0)
    die5.configure(background=dbag.face_colors[0], fg="#000000")

def turn_of_fate():
    add_gem()
    unlock_sixes(10)
    reset_sixes()

######################################################################
# DIE POOL BUTTONS!
b3 = Button(dicepool, text="ROLL DICE", command = roll_dice)
b3.pack()
dicepool.create_window(710, 20, window = b3, width = 100, height = 20)

b4 = Button(dicepool, text="TURN OF FATE", command = turn_of_fate)
b4.pack()
dicepool.create_window(710, 50, window = b4, width = 100, height = 20)

# DEBUGGER BUTTON TO RESET DICE
b5 = Button(dicepool, text="RESET DICE", command = reset_dice)
b5.pack()
dicepool.create_window(710, 80, window = b5, width = 100, height = 20)


# MAKE THE MAGIC HAPPEN!
mainloop()
