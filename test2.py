from tkinter import *
from test1 import *

class gem_pool(object):
    gems = 0
    def __init__(self, gems):
        self.gems = gems
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

make_view()
mainloop()
