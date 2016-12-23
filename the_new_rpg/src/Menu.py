import graphics, variables, pygame, enemies, pickle, classvar, maps, os
from variables import settings
from classvar import player

#can't pickle pygame masks, and problems pickeling pygame surfaces
def save():
    player.mask = 0
    savelist = [settings, player.xpos, player.ypos, player.lv, player.exp, classvar.battle, maps.current_map_name]
    with open("bdsave0.txt", "wb") as f:
        pickle.dump(savelist, f)

def load():
    if(os.path.isfile(os.path.abspath("bdsave0.txt"))):
        if os.path.getsize(os.path.abspath("bdsave0.txt")) > 0:
            f = open("bdsave0.txt", "rb")
            loadedlist = pickle.load(f)
            variables.settings, player.xpos, player.ypos, player.lv, player.exp, classvar.battle, maps.current_map_name = loadedlist
            maps.change_map_nonteleporting(maps.current_map_name)

    if(not isinstance(classvar.battle, str)):
        classvar.battle.enemy.reset()

class Menu():
    option = 0
    options = ["resume", "save", "controls", "exit"]
    optionpics = []
    textxoffset = 0
    textyspace = 0

    def __init__(self):
        for o in self.options:
            textpic = graphics.sscale_customfactor(variables.font.render(o, 0, variables.WHITE), 1)
            self.optionpics.append(textpic)

        self.textyspace = self.optionpics[0].get_height() * (3 / 2)
        self.textxoffset = self.optionpics[0].get_width() / 6
        self.reset()

    def reset(self):
        self.option = 0
        self.enemyanimation = enemies.random_enemy()

    def draw(self):
        for x in range(len(self.optionpics)):
            variables.screen.blit(self.optionpics[x],
                                  [self.textxoffset, (x + 1) * self.textyspace - self.optionpics[x].get_height() / 2])

        pygame.draw.rect(variables.screen, variables.WHITE,
                         [self.textxoffset / 4, (self.option + 1) * self.textyspace, self.textxoffset * (3 / 4),
                          self.textxoffset * (3 / 4)])

    def onkey(self, key):
        if key in settings.upkeys:
            self.option = (self.option - 1) % len(self.options)
        elif key in settings.downkeys:
            self.option = (self.option + 1) % len(self.options)
        elif key in settings.enterkeys:
            if self.options[self.option] == "resume":
                settings.menuonq = False
                classvar.player.change_of_state()
                classvar.battle.unpause()
            elif self.options[self.option] == "save":
                save()
