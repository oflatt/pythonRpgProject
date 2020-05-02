from pygame import gfxdraw, Rect


import variables
from DestructiveFrozenClass import DestructiveFrozenClass
from .Garden import Garden

from .shopplants import make_shopplant_list
from .constants import potsperrow
from .Plant import Plant

class Game(DestructiveFrozenClass):

    def __init__(self):

        self.state = 'play'
        self.basescale = int(variables.height / 20 / 6)
        self.zoom = 1

        self.shopplants = make_shopplant_list()
        self.gardens = [Garden(), Garden()]

        # add all shop plants cheat
        for p in self.shopplants:
            self.gardens[0].addplant(Plant(p.headnode))
            self.gardens[1].addplant(Plant(p.headnode))
        

        # position of cursor on items
        self.cursorx = 0
        self.cursory = 0

        # how many items to scroll to keep things on screen
        self.lastcursoroffset = 0
        self.yscrolloffset = 0

            
        self._freeze()


    def shopgetplantbyname(self, name):
        for p in self.shopplants:
            if p.name == name:
                return p
        raise Exception("No shopplant with name " + str(name))


    def scale(self):
        return self.basescale * (1/(1+self.zoom))

    def getgardenypositions(self, time, settings, screen):
        currenty = 0
        ylist = [0]
        for gardeni in range(len(self.gardens)):
            garden = self.gardens[gardeni]
            cursorpos, currenty = garden.draw(time, settings, screen, self.scale(), currenty = currenty, nodraw = True)
            ylist.append(currenty)
            
        return ylist
    
    def draw(self, time, settings, screen):

        selectedgarden = self.gardens[self.cursory]

        newcursoroffset = self.lastcursoroffset
        while selectedgarden.get_xpos_end_of_cursor_plant(self.cursorx, self.scale(), newcursoroffset, screen) == None:
            newcursoroffset -= 1
        while selectedgarden.get_xpos_end_of_cursor_plant(self.cursorx, self.scale(), newcursoroffset, screen)[0] > variables.width:
            newcursoroffset += 1

        # now to get how much it will scroll, calculate based upon a version without scrolling
        if newcursoroffset > 0:
            currentxscroll = selectedgarden.get_xpos_end_of_cursor_plant(newcursoroffset-1, self.scale(), 0, screen)[0]
        else:
            currentxscroll = 0

        endscroll = selectedgarden.get_xpos_end_of_cursor_plant(len(selectedgarden.plants)-1, self.scale(), 0, screen)[0]

        gardenypositions = self.getgardenypositions(time, settings, screen)
        if gardenypositions[self.cursory]+self.yscrolloffset < 0:
            self = self.destructiveset("yscrolloffset", -gardenypositions[self.cursory])
        if gardenypositions[self.cursory+1]+self.yscrolloffset > screen.get_height():
            self = self.destructiveset("yscrolloffset", -(gardenypositions[self.cursory+1]-screen.get_height() + 10*self.scale()))

        currenty = self.yscrolloffset
        
        for gardeni in range(len(self.gardens)):
            garden = self.gardens[gardeni]
            drawcursorindex =-1
            if gardeni == self.cursory:
                drawcursorindex = self.cursorx
            
            cursorpos, currenty = garden.draw(time, settings, screen, self.scale(), currentxscroll = currentxscroll, cursoroffset = newcursoroffset, endscroll=endscroll, drawcursorindex = drawcursorindex, currenty = currenty)

        self = self.destructiveset("lastcursoroffset", newcursoroffset)

        return self

    def current_row_length(self):
        return len(self.gardens[self.cursory].plants)

    def onkeydown(self, key, settings):
        if settings.iskey("right", key):
            self = self.destructiveset("cursorx", (self.cursorx+1) % self.current_row_length())
        elif settings.iskey("left", key):
            self = self.destructiveset("cursorx", (self.cursorx-1)%self.current_row_length())
        elif settings.iskey("up", key):
            self = self.destructiveset("cursory", (self.cursory-1)%len(self.gardens))
        elif settings.iskey("down", key):
            self = self.destructiveset("cursory", (self.cursory+1)%len(self.gardens))
        elif settings.iskey("zoom", key):
            self =self.destructiveset("zoom", (self.zoom + 1)% 4)
            # also reset the offset for recalculation
            self = self.destructiveset("lastcursoroffset", 0)
        return self
