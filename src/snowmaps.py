import variables, graphics, enemies
from random import randint
from Map import Map
from graphics import snowland
from Exit import Exit
from Rock import Rock


# snowentrance###########################################################################
snowentrance = Map(snowland(650, 500, True), [])
snowentrance.populate_with("snowpinetree", randint(4, 10))

snowentrance.exitareas = [Exit("right", False, "jeremyhome", "left", "same"),
                          Exit("left", False, "snowarea1", "right", "same")]
snowentrance.enemies = enemies.snowenemies
snowentrance.lvrange = [6]

# snowarea1##############################################################################
snowarea1 = Map(snowland(700, 500), [])
snowarea1.populate_with("snowpinetree", randint(10, 15))

snowarea1.lvrange = [6, 7]
snowarea1.enemies = enemies.snowenemies

snowarea1.exitareas = [Exit("right", False, "snowentrance", "left", "same"),
                       Exit("left", False, "hoppingtreearea", "right", "same")]

# hoppingtreearea#######################################################################
hoppingrock = Rock("chicking0", 350, 250, variables.TREECOLLIDESECTION)
hoppingtreearea = Map(snowland(800, 500), [hoppingrock])

hoppingtreearea.lvrange = [6, 8]
hoppingtreearea.enemies = enemies.snowenemies

hoppingtreearea.exitareas = [Exit("right", False, "snowarea1", "left", "same")]

