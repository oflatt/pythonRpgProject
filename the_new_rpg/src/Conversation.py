#!/usr/bin/python
#Oliver Flatt works on Classes
import variables, pygame, graphics

class Conversation():
    line = 0
    area = [0, 0, 0, 0] #x, y, width, height in a list (a Rect)
    isbutton = True #true if you have to hit a button to enter
    textsize = 0.5

    def __init__(self, dialogue):
        #dialogue is a list of strings, one per line. Writer has to make sure they fit
        self.dialogue = dialogue

    def draw(self):
        h = variables.height
        w = variables.height
        b = h*13/16
        pygame.draw.rect(variables.screen, variables.BLACK, [0, b, w, h])
        line1 = graphics.sscale_customfactor(variables.font.render(self.dialogue[self.line], 0, variables.WHITE), self.textsize)
        line2 = graphics.sscale_customfactor(variables.font.render(self.dialogue[self.line+1], 0, variables.WHITE), self.textsize)
        line3 = graphics.sscale_customfactor(variables.font.render(self.dialogue[self.line+2], 0, variables.WHITE), self.textsize)
        variables.screen.blit(line1, [w/2 - line1.get_width()/2, b])
        variables.screen.blit(line2, [w/2 - line2.get_width()/2, b+line1.get_height()])
        variables.screen.blit(line3, [w/2 - line3.get_width()/2, b+line1.get_height()+line2.get_height()])

    def keypress(self, key):
        if self.line < len(self.dialogue) - 3:
            self.line += 1