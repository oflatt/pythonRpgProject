#!/usr/bin/python
import variables, classvar, conversations, enemies
from graphics import GR
from Map import Map
from Rock import Rock
from Exit import Exit
from pygame import Rect

# Coordinates for maps are based on the base of each map respectively
honeyw = GR["honeyside0"]["w"]
honeyh = GR["honeyside0"]["h"]
honeyfeetheight = honeyh * (3 / 29)
extraarea = 50
insidewidth = GR["honeyhouseinside"]["w"]
insideheight = GR["honeyhouseinside"]["h"]
# p is the width of a pixel
p = insidewidth / 176

treecollidesection = [0, 19 / 20, 1, 1 / 20]

# outside3##############################################################################################################
b = GR["rightturn"]["w"] / 10
outsideheight = GR["rightturn"]["h"]
outside3 = Map(GR["rightturn"], [])
outside3.exitareas = [Exit([0, outsideheight, b * 10, extraarea], False, "outside2", "same", 0)]
outside3.enemies = [enemies.spoe]
outside3.lvrange = [1,2]

# outside2##############################################################################################################
b = GR["leftturn"]["w"] / 10
outsideheight = GR["leftturn"]["h"]
outside2 = Map(GR["leftturn"], [Rock(GR["rock"], 5 * b, 4 * b, [0, 0, 1, 1]),
                                Rock(GR["rock"], 6 * b, 2 * b, [0, 0, 1, 1]),
                                Rock(GR["pinetree0"], 4 * b, 5 * b, treecollidesection),
                                Rock(GR["pinetree0"], 6 * b, 1.8 * b, treecollidesection),
                                Rock(GR["pinetree1"], 5.5 * b, 4.5 * b, treecollidesection),
                                Rock(GR["pinetree1"], 2 * b, 4.7 * b, treecollidesection),
                                Rock(GR["pinetree1"], 1.7 * b, 0.3 * b, treecollidesection)])

outside2.exitareas = [
    Exit([-extraarea, 0, extraarea, outsideheight], False, 'outside1', GR["horizontal"]["w"] - honeyw, "same"),
    Exit([0, -extraarea, b * 10, extraarea], False, 'outside3', "same", GR["rightturn"]["h"] - honeyh)]
outside2.enemies = [enemies.sheep, enemies.greenie, enemies.perp]
outside2.lvrange = [1]

# jeremyhome############################################################################################################
b = GR["halfpath"]["w"] / 10
hole = Rock(GR["rabbithole"], b * 5 + GR["rabbithole"]["w"], b * 5 - GR["rabbithole"]["h"], [0, 1 / 2, 1, 1 / 2])
jmyman = Rock(GR["jeremy0"], b * 5 + GR["rabbithole"]["w"], b * 5 - GR["rabbithole"]["h"], [0, 3 / 4, 1, 1 / 4])
jmyman.background_range = hole.background_range.copy()

jeremyhome = Map(GR["horizontal"], [hole, jmyman])
jeremyhome.exitareas = [
    Exit([b * 10, int(GR["house"]["h"]), extraarea, GR["halfpath"]["h"]], False, 'outside1', 0, "same")]
conversations.jeremy.area = [b * 5 + GR["rabbithole"]["w"] - (honeyw / 2), b * 5 - GR["rabbithole"]["h"],
                             GR["rabbithole"]["w"] - (honeyw / 2), GR["rabbithole"]["h"]]
jeremyhome.conversations = [conversations.jeremy]

# outside1##############################################################################################################
b = GR["horizontal"]["w"] / 10

treerock = Rock(GR["pinetree0"], 3.5 * b, 1.5 * b, treecollidesection)
meangreeny = treerock.y + GR["pinetree0"]["h"] - GR["meangreen0"]["h"]
meangreenrock = Rock(GR["meangreen0"].copy(), treerock.x + 0.5 * b, meangreeny, [0, 0.81, 1, 0.19])
meangreenrock.background_range = treerock.background_range.copy()
outside1 = Map(GR["horizontal"], [Rock(GR["house"], 0, 0, None),
                                  meangreenrock,
                                  Rock(GR["rock"], 6.5 * b, 7 * b, [0, 0, 1, 1]),
                                  Rock(GR["rock"], 5.5 * b, 3.5 * b, [0, 0, 1, 1]),
                                  Rock(GR["rock"], 2.5 * b, 6.3 * b, [0, 0, 1, 1]),
                                  treerock])
housewidth = GR["house"]["w"]
househeight = GR["house"]["h"]
outsidewidth = GR["horizontal"]["w"]
outsideheight = GR["horizontal"]["h"]
outside1.startpoint = [b * 8, b * 4]
outside1.exitareas = [Exit([outsidewidth, 0, extraarea, outsideheight], False, 'outside2', 0, "same"),
                      Exit([-extraarea, 0, extraarea, outsideheight], False, 'jeremyhome', GR["halfpath"]["w"] - honeyw,
                           "same"),
                      Exit([housewidth * (1.5 / 5), househeight * (3 / 5), housewidth * (1 / 10),
                            househeight * (1 / 5)],
                           True, 'honeyhome',
                           p * 41, insideheight - honeyh)]
outside1.colliderects = [Rect(0, 0, housewidth, househeight)]
outside1.lvrange = [1, 2]
outside1c = conversations.secondscene
outside1c.area = [treerock.x, 0, outsidewidth, outsideheight]
outside1c.isbutton = False
outside1c.part_of_story = 2
outside1c.special_battle = enemies.greenie
outside1.conversations = [outside1c]

# honeyhome#############################################################################################################
b = insidewidth / 10
honeyhome = Map(GR["honeyhouseinside"],
                [Rock(GR["table"], p * 75, p * 110, [0, 0.5, 1, 0.5]),
                 Rock(GR['stash'], p * 130, p * 60, [0, 0.9, 1, 0.1])])
honeyhome.startpoint = [86 * p, 56 * p]
honeyhome.exitareas = [Exit([35 * p + honeyw / 2, 165 * p, 37 * p - honeyw, extraarea],
                            True, 'outside1',
                            GR["house"]["w"] * (1 / 5), GR["house"]["h"] - honeyh + honeyfeetheight)]

racoonc = conversations.firstscene
racoonc.area = [0, 7 * b + GR["tp"]["h"], insidewidth,
                extraarea]  # extraarea because it does not matter how thick it is down
racoonc.isbutton = False
racoonc.part_of_story = 1  # makes it so you can only have the conversation once
honeyhome.conversations = [racoonc]
honeyhome.colliderects = [Rect(0, 0, p * 31, p * 74),  # bed
                          Rect(0, 0, insidewidth, p * 44),  # wall
                          Rect(44 * p, 0, 26 * p, 56 * p),  # wardrobe
                          Rect(p * 75, p * 110 + p * 11, p * 44, p * 13)]  # table

# teleportation and stuff###############################################################################################
home_map = honeyhome
current_map = home_map
current_map_name = 'honeyhome'
classvar.player.teleport(current_map.startpoint[0] * current_map.map_scale_offset,
                         current_map.startpoint[1] * current_map.map_scale_offset)


def new_scale_offset():
    global current_map
    variables.scaleoffset = current_map.map_scale_offset
    classvar.player.scale_by_offset()


def change_map_nonteleporting(name):
    global current_map_name
    global current_map
    current_map_name = name
    possibles = globals()
    map_picked = possibles.get(name)
    if not map_picked:
        raise NotImplementedError("Map %s not implemented" % name)
    current_map = map_picked


def change_map(name, newx, newy):
    change_map_nonteleporting(name)
    if (isinstance(newx, str)):
        newx = classvar.player.xpos
        if (newx < 0):
            newx = 0
        if (newx > (current_map.base["w"] * current_map.map_scale_offset - (honeyw * current_map.map_scale_offset))):
            newx = current_map.base["w"] * current_map.map_scale_offset - (honeyw * current_map.map_scale_offset)
    else:
        newx *= current_map.map_scale_offset
    if (isinstance(newy, str)):
        newy = classvar.player.ypos
        if (newy < 0):
            newy = 0
        if (newy > (current_map.base["h"] * current_map.map_scale_offset - (honeyh * current_map.map_scale_offset))):
            newy = current_map.base["h"] * current_map.map_scale_offset - (honeyh * current_map.map_scale_offset)
    else:
        newy *= current_map.map_scale_offset
    classvar.player.teleport(newx, newy)
    new_scale_offset()


def engage_conversation(c):
    classvar.player.change_of_state()
    if c.part_of_story == "none":
        variables.settings.state = "conversation"
        conversations.currentconversation = c
    elif c.part_of_story == classvar.player.storyprogress:
        variables.settings.state = "conversation"
        classvar.player.storyprogress += 1
        conversations.currentconversation = c


def on_key(key):
    if key in variables.settings.enterkeys:
        e = current_map.checkexit()
        c = current_map.checkconversation()
        if not e == False:
            change_map(e.name, e.newx, e.newy)
        elif not c == False:
            engage_conversation(c)


def checkexit():
    e = current_map.checkexit()
    if not e == False:
        if e.isbutton == False:
            change_map(e.name, e.newx, e.newy)


def checkconversation():
    c = current_map.checkconversation()
    if not c == False:
        if c.isbutton == False:
            engage_conversation(c)
