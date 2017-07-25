from tkinter import *
import random
from app_view import *


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

def remove_gem():
    if gPool.get_gems() > 0:
        gPool.set_gems(gPool.get_gems() - 1)
        gViewTV.set(str(gPool.get_gems()))
    else:
        print("no gems to remove")


def add_gem():
    gPool.set_gems(gPool.get_gems() + 1)
    gViewTV.set(str(gPool.get_gems()))


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


def roll_die():
    return random.randint(1,6)

def roll_dice():
    results = []
    for die in dbag.get_locks():
        if die == False:
            results.append(roll_die())
        else:
            results.append(6)


    if any(results[0] in n for n in [1,2,3,4,5]):
        d1tv.set(str(dbag.get_face(results[0])))
        die1.configure(background=dbag.face_colors[results[0]])
    else:
        d1tv.set(str(dbag.get_face(results[0])))
        die1.configure(background=dbag.face_colors[results[0]])
        dbag.set_locks(1, True)

    if results[1] !=  6:
        d2tv.set(str(dbag.get_face(results[1])))
        die2.configure(background=dbag.face_colors[results[1]])
    else:
        d2tv.set(str(dbag.get_face(results[0])))
        die2.configure(background=dbag.face_colors[results[0]])
        dbag.set_locks(2, True)

    if results[2] !=  6:
        d3tv.set(str(dbag.get_face(results[2])))
        die3.configure(background=dbag.face_colors[results[2]])
    else:
        d3tv.set(str(dbag.get_face(results[0])))
        die3.configure(background=dbag.face_colors[results[0]])
        dbag.set_locks(3, True)

    if results[3] !=  6:
        d4tv.set(str(dbag.get_face(results[3])))
        die4.configure(background=dbag.face_colors[results[3]])
    else:
        d4tv.set(str(dbag.get_face(results[0])))
        die4.configure(background=dbag.face_colors[results[0]])
        dbag.set_locks(4, True)

    if results[4] !=  6:
        d5tv.set(str(dbag.get_face(results[4])))
        die5.configure(background=dbag.face_colors[results[4]])
    else:
        d5tv.set(str(dbag.get_face(results[0])))
        die5.configure(background=dbag.face_colors[results[0]])
        dbag.set_locks(5, True)

    print(dbag.get_locks())
    print(results)

mainloop()
