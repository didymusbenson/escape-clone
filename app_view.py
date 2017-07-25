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


# Create the text variable for the view
gViewTV = StringVar()
# Create the label
gemView = Label( w, textvariable = gViewTV )
gemView.pack()
w.create_window(270, 60, window = gemView, width = 100, height = 100)

# Set the label to the current amount of gems
gViewTV.set(str(gPool.get_gems()))


# Create the button, pack it, and make the window for it in the Canvas
b1 = Button(w, text="REMOVE BATTERY", command=remove_gem)
b1.pack()
w.create_window(270, 130, window = b1, width = 100, height = 20)

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

# declare die textvariables
d1tv = StringVar()
d2tv = StringVar()
d3tv = StringVar()
d4tv = StringVar()
d5tv = StringVar()
# dice labels
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

dicepool.create_window(50 + 0 * 90 , 50, window = die1 , width = 78, height = 78)
dicepool.create_window(50 + 1 * 90 , 50, window = die2 , width = 78, height = 78)
dicepool.create_window(50 + 2 * 90 , 50, window = die3 , width = 78, height = 78)
dicepool.create_window(50 + 3 * 90 , 50, window = die4 , width = 78, height = 78)
dicepool.create_window(50 + 4 * 90 , 50, window = die5 , width = 78, height = 78)

b3 = Button(dicepool, text="ROLL DICE", command = roll_dice)
b3.pack()
dicepool.create_window(710, 20, window = b3, width = 100, height = 20)
