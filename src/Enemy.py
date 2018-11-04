#!/usr/bin/python
#Oliver Flatt works on Classes
from FrozenClass import FrozenClass
import graphics, variables, enemies, copy, stathandeling
from FrozenClass import FrozenClass

class Enemy(FrozenClass):

    def __init__(self, animationnum, rarity, name, beatmaprules, volumeenvelope = None):
        self.lv = 0
        self.animationnum = animationnum
        self.rarity = rarity
        self.name = name
        self.beatmapspecs = copy.deepcopy(variables.generic_specs)
        self.beatmapspecs["rules"].extend(beatmaprules)
        if volumeenvelope != None:
            self.beatmapspecs["volumeenvelope"] = volumeenvelope
        self.health = None
        self.storyeventsonwin = None
        self.storyeventsonlose = None
        self.storyeventsonflee = None
        self.specialscale = None
        # reset needs to be called before enemy is used
        self.animation = None
        
        self._freeze()

    def reset(self):
        self.animation = enemies.animations[self.animationnum]
        self.animation.reset()

    def sethealth(self):
        self.health = stathandeling.max_health(self.lv)

    def enterbattle(self):
        if self.name == "bogo":
            graphics.randombogoface()
