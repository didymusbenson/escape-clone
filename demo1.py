from tkinter import *

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
dice = [1,2,3,4,5]
i = 0
for die in dice:
    lb = Label(dicepool, text = "DIE", borderwidth=2 , relief="solid")
    lb.pack()
    lb.configure(background='#FFFF7F')
    dicepool.create_window(50 + i * 90 , 50, window = lb, width = 78, height = 78)
    i += 1

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

# MAKE THE MAGIC HAPPEN!
mainloop()
