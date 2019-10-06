from Game import Game
from .Game import Game


def initgame(settings, screen):
    if settings.getgamedata("growgame") == None:
        settings.setgamedata("growgame", Game())

    
def onkeydown(outsidetime, settings, key):
    game = settings.getgamedata("growgame")
    settings.setgamedata("growgame", game.onkeydown(key, settings))

def onkeyup(outsidetime, settings, key):
    pass

    
def ontick(outsidetime, settings):
    pass
        

def ondraw(outsidetime, settings, screen):
    screen.fill((0,0,0))
    data = settings.getgamedata("growgame").draw(outsidetime, settings, screen)
    settings.setgamedata("growgame", data)

def onpause(time):
    pass
    
def onunpause(time):
    pass

def creategame():
    return Game("growgame", initgame, onkeydown, onkeyup, ontick, ondraw, onpause, onunpause)
