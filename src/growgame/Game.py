from pygame import gfxdraw, Rect


import variables
from DestructiveFrozenClass import DestructiveFrozenClass
from ChoiceButtons import ChoiceButtons
from .Garden import Garden
from pygame import Rect

from .shopplants import make_shopplant_list
from .constants import potsperrow
from .Plant import Plant

class Game(DestructiveFrozenClass):

    def __init__(self):

        self.state = 'play'
        self.basescale = int(variables.height / 20 / 6)
        self.zoom = 1
        self.gardenlimit = 12

        self.shopplants = make_shopplant_list()
        self.gardens = [Garden()]

        # add all shop plants cheat
        #for p in self.shopplants:
         #   self.gardens[0].addplant(Plant(p.headnode))
          #  self.gardens[1].addplant(Plant(p.headnode))
        

        # position of cursor on items
        self.cursorx = 0
        self.cursory = 0

        # how many items to scroll to keep things on screen
        self.lastcursoroffset = 0
        self.yscrolloffset = 0


        self.sun = 0
        buttonnames = ["breed (-10 Sun)", "sell (+5 Sun)"]
        self.specialbuttonslen = len(buttonnames)
        for p in self.shopplants:
            labelname = p.name + " (-" + str(p.cost) + " Sun)"
            buttonnames.append(labelname)
            

        self.shop = ChoiceButtons(buttonnames, 1/25)
        
        self._freeze()


    def buttonpressed(self, index):
        flowerindex = index-self.specialbuttonslen
        self.addflower(self.shopplants[flowerindex])

    def addflower(self, shopplant):
        for garden in self.gardens:
            if len(garden.plants) < self.gardenlimit:
                garden.addplant(Plant(shopplant.headnode))
                return
        # otherwise all full
        self.gardens.append(Garden())
        self.gardens[-1].addplant(Plant(shopplant.headnode))
        
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

    def gardenindex(self):
        return max(self.cursory-1, 0)
    
    def draw(self, time, settings, screen):

        
        gardensareay = (self.shop.buttons[0].y*2) * screen.get_height() + self.shop.buttons[0].height()
        
        selectedgarden = self.gardens[self.gardenindex()]

        newcursoroffset = self.lastcursoroffset
        currentxscroll = 0
        if self.cursory != 0:
        
            while selectedgarden.get_xpos_end_of_cursor_plant(self.cursorx, self.scale(), newcursoroffset, screen) == None:
                newcursoroffset -= 1
            while selectedgarden.get_xpos_end_of_cursor_plant(self.cursorx, self.scale(), newcursoroffset, screen)[0] > variables.width:
                newcursoroffset += 1

            # now to get how much it will scroll, calculate based upon a version without scrolling
            if newcursoroffset > 0:
                currentxscroll = selectedgarden.get_xpos_end_of_cursor_plant(newcursoroffset-1, self.scale(), 0, screen)[0]
                

        endscroll = 0
        if len(selectedgarden.plants) > 0:
            endscroll = selectedgarden.get_xpos_end_of_cursor_plant(len(selectedgarden.plants)-1, self.scale(), 0, screen)[0]

        gardenypositions = self.getgardenypositions(time, settings, screen)
        if gardenypositions[self.gardenindex()]+self.yscrolloffset < 0:
            self = self.destructiveset("yscrolloffset", -gardenypositions[self.gardenindex()])
        if gardenypositions[self.gardenindex()+1]+self.yscrolloffset > screen.get_height()-gardensareay:
            self = self.destructiveset("yscrolloffset", -(gardenypositions[self.gardenindex()+1]-screen.get_height() + gardensareay + 10*self.scale()))

        currenty = self.yscrolloffset + gardensareay
        
        for gardeni in range(len(self.gardens)):
            garden = self.gardens[gardeni]
            drawcursorindex =-1
            if gardeni == self.gardenindex() and self.cursory != 0:
                drawcursorindex = self.cursorx
            
            cursorpos, currenty = garden.draw(time, settings, screen, self.scale(), currentxscroll = currentxscroll, cursoroffset = newcursoroffset, endscroll=endscroll, drawcursorindex = drawcursorindex, currenty = currenty)

        self = self.destructiveset("lastcursoroffset", newcursoroffset)

        screen.fill(variables.GREY, Rect(0, 0, screen.get_width(), gardensareay))
        
        self.shop.isselected = self.cursory == 0
        if self.cursory == 0:
            self.shop.currentoption = self.cursorx
        else:
            self.shop.currentoption = 0
        self.shop.draw()
        
        return self

    def current_row_length(self):
        if(self.cursory == 0):
            return len(self.shop.buttons)
        else:
            return len(self.gardens[self.gardenindex()].plants)

    def onkeydown(self, key, settings):
        if settings.iskey("right", key):
            self = self.destructiveset("cursorx", (self.cursorx+1) % self.current_row_length())
        elif settings.iskey("left", key):
            self = self.destructiveset("cursorx", (self.cursorx-1)%self.current_row_length())
        elif settings.iskey("up", key):
            self = self.destructiveset("cursory", (self.cursory-1)%(len(self.gardens)+1))
            self = self.destructiveset("cursorx", self.cursorx % self.current_row_length())
        elif settings.iskey("down", key):
            self = self.destructiveset("cursory", (self.cursory+1)%(len(self.gardens)+1))
            self = self.destructiveset("cursorx", self.cursorx % self.current_row_length())
        elif settings.iskey("action", key):
            if self.cursory == 0:
                self.buttonpressed(self.cursorx)
        elif settings.iskey("zoom", key):
            self =self.destructiveset("zoom", (self.zoom + 1)% 4)
            # also reset the offset for recalculation
            self = self.destructiveset("lastcursoroffset", 0)
        return self
