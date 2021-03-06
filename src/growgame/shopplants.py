import math, random, copy


from variables import brighten, devprint
from rdraw.pointlist import listarc, linelist_to_shapelist, scalepointlist, flippointlist
from rdraw.Texture import Texture

from .ShopPlant import ShopPlant
from .PlantNode import PlantNode
from .PlantShape import PlantShape
from .crossplants import crossplants





bigstem_list = [(0.0,0.0)]
for x in range(20):
    bigstem_list.append((float(x), -0.25))
    if x == 20-1:
        bigstem_list.append((float(x), 0.0))
        
bigstem_plantshape = PlantShape(bigstem_list, (0, 200, 0), (0, 120, 0))


def sunflower():
    #make a sunflower
    flower_stem_list = [(0.0,0.0)]
    for x in range(60):
        flower_stem_list.append((x, 1.0))
    stem_plant_shape = PlantShape(flower_stem_list, (0, 200, 0), (0, 120, 0))
    
    petal_shape_list = [(0.0, 0.0)]
    petal_num_points = 15
    for x in range(petal_num_points):
        petal_shape_list.append((x, 2*math.sin(x/petal_num_points * math.pi)))
    petal_shape = PlantShape(petal_shape_list, (250, 227, 77), (250, 210, 77))
    petal_node = PlantNode([petal_shape], 17, math.pi/4)

    center_outline = (125, 90, 9)
    center_fill = (99, 72, 9)
    center_radius = 6
    
    center_shape_list = listarc(-center_radius, 0, center_radius*2, center_radius, 10)
    #adding texture to the center of the sunflower
    center_texture_1 = Texture((43, 30, 2), 0.1, 0.05, 0.05, stopcolors = [center_outline], acceptedcolors = [center_fill])
    center_texture_2 = Texture((74, 53, 4), 0.3, 0.05, 0.05, stopcolors = [center_outline], acceptedcolors = [center_fill])
    center_texture_3 = Texture((102, 73, 6), 0.4, 0.05, 0.15, stopcolors = [center_outline], acceptedcolors = [center_fill])
    center_texture_4 = Texture((125, 90, 16), 0.5, 0.3, 0.05, stopcolors = [center_outline], acceptedcolors = [center_fill])
    
    center_shape = PlantShape(center_shape_list, center_fill, center_outline)
    center_shape = center_shape.destructiveset("textures", [center_texture_1, center_texture_2, center_texture_3, center_texture_4])
    
    center_node = PlantNode([center_shape], 1, math.pi/20)

    #adding two leaves, and limiting the range of placement for each
    leaf_shape_list_1 = [(0.0, 0.0)]
    leaf_outline = (0, 84, 0)
    leaf_fill = (0, 120, 0)
    for x in range(1, 10):
        leaf_shape_list_1.append((x, 25*math.exp(-.5*x)*math.sin((1/5)*x)))
    for x in range(9, -1, -1):
        leaf_shape_list_1.append((x, 0))
    leaf_shape_1 = PlantShape(leaf_shape_list_1, leaf_fill, leaf_outline, completelistp = True)
    leaf_node_1 = PlantNode([leaf_shape_1], 1, math.pi)
    leaf_node_1 = leaf_node_1.destructiveset("shiftchance", 0.01)
    leaf_node_1 = leaf_node_1.destructiveset("branchoffset", 0.5)

    leaf_shape_list_2 = [(0.0, 0.0)]
    for x in range(1, 10):
        leaf_shape_list_2.append((x, 25*math.exp(-.5*x)*math.sin((1/5)*x)))
    for x in range(9, -1, -1):
        leaf_shape_list_2.append((x, 0))
    leaf_shape_2 = PlantShape(leaf_shape_list_2, leaf_fill, leaf_outline, completelistp = True)
    leaf_node_2 = PlantNode([leaf_shape_2], 1, math.pi)
    leaf_node_2 = leaf_node_2.destructiveset("shiftchance", 0.01)
    leaf_node_2 = leaf_node_2.destructiveset("branchoffset", 0.7)
    
    stem_node = PlantNode([stem_plant_shape], 1, math.pi/5, children=[center_node, petal_node, leaf_node_1, leaf_node_2])
    return ShopPlant("Sunflower", stem_node, 80)
            
    
def makestarter():
    # make the starter flower
    petal_list = [(0.0, 0.0)]
    petal_numofpoints = 13
    for x in range(petal_numofpoints):
        petal_list.append((x, 4*math.sin(x/petal_numofpoints * math.pi)))


    middlecolor = (241, 252, 63)
    middletexture = Texture(brighten(middlecolor, -50), 0.2, 0.05, 0.05, acceptedcolors = [middlecolor])

    middleradius = 2.5
    middlelist = listarc(-middleradius, 0, middleradius*2, middleradius, 8)
    middleshape = PlantShape(middlelist, middlecolor, brighten(middlecolor, -30))
    
    # set the texture of the middle of the flower to fill in some dark pixels
    middleshape = middleshape.destructiveset("textures", [middletexture])
    
    middlenode = PlantNode([middleshape], 1, math.pi/20)

    petal_shape = PlantShape(petal_list, (0, 0, 200), (0, 0, 120))
    petalnode = PlantNode([petal_shape], 5, math.pi*2 / 5)
    
    starter_flower = PlantNode([bigstem_plantshape], 1, math.pi/10, children = [middlenode, petalnode])
    

    
    return ShopPlant("blue flower", starter_flower, 0)


def makerose():
    petal_list = [(0, 0)]
    petal_numofpoints = 13
    
    for x in range(petal_numofpoints):
        petal_list.append((x*0.75, -(2*math.sin((1-(x**1.5/petal_numofpoints**1.5)) * math.pi))))

    petal_shape = PlantShape(petal_list, (120, 0, 0), (180, 0, 0))
    petalnode = PlantNode([petal_shape], 4, math.pi/8)
    petalnode = petalnode.destructiveset("anglevariance", 0.1)
    petalnode = petalnode.destructiveset("heightvariance", 0.2)
    petalnode = petalnode.destructiveset("widthvariance", 1)
    petalnode = petalnode.destructiveset("brancharea", 0)

    
    innerpetal_list = [(0, 0)]
    innerpetal_numofpoints = 13
    
    for x in range(innerpetal_numofpoints):
        innerpetal_list.append((x*0.75, -(1.5*math.sin((1-(x**1.5/innerpetal_numofpoints**1.5)) * math.pi))))
    

    innerpetal_shape = PlantShape(innerpetal_list, (100, 0, 0), (120, 0, 0))
    innerpetalnode = PlantNode([innerpetal_shape], 4, 0)
    innerpetalnode = innerpetalnode.destructiveset("anglevariance", 0)
    innerpetalnode = innerpetalnode.destructiveset("heightvariance", 0.4)
    innerpetalnode = innerpetalnode.destructiveset("brancharea", 0)

    spikes_list = [(0, 0.5), (2, 0)]
    spikes_shape = PlantShape(spikes_list, (70, 10, 40), (100, 0, 40))
    spikes_node = PlantNode([spikes_shape], 1, math.pi)
    spikes_node = spikes_node.destructiveset("repeatnumseparate", 3)
    spikes_node = spikes_node.destructiveset("brancharea", 0.6)
    spikes_node = spikes_node.destructiveset("branchoffset", 0.2)
    spikes_node = spikes_node.destructiveset("heightvariance", 1)
    
    rose = PlantNode([bigstem_plantshape], 1, math.pi/10, children = [petalnode, innerpetalnode, spikes_node])

    return (ShopPlant("rose", rose, 20))


def makecactus():
    spike_list = [(0, 0), (1.5, 0)]
    spikecolor = (80, 80, 80)
    spikes_shape = PlantShape(spike_list, spikecolor, spikecolor)
    spike_node = PlantNode([spikes_shape], 1, math.pi/4)
    spike_node = spike_node.destructiveset("repeatnumseparate", 10)
    spike_node = spike_node.destructiveset("brancharea", 1)
    spike_node = spike_node.destructiveset("shiftchance", 0.05)
    
    body_list = [(0,0)]
    body_numofpoints = 20
    roundedness = 3.5
    for x in range(body_numofpoints):
        body_list.append((x, -(5*math.sin(x**roundedness/body_numofpoints**roundedness * math.pi/2 + math.pi/2))))


    cactuscolor = (29, 183, 55)
    cactuslinecolor = brighten(cactuscolor, -20)
    spiketexture = Texture(spikecolor, 0.1, 0.2, 0.05)
    spiketexture.acceptedcolorsspawn = [cactuscolor, cactuslinecolor]

    
    bodylineshapes = []
    number_of_lines = 2
    for i in range(number_of_lines):
        bodylinelist = scalepointlist(body_list, 1-((i+1)/(number_of_lines+1)), 1)
        rightlinelist = flippointlist(bodylinelist)
        bodylinelist = linelist_to_shapelist(bodylinelist)
        rightlinelist = linelist_to_shapelist(rightlinelist)
        bodylineshapes.append(PlantShape(bodylinelist, brighten(cactuscolor, -40), cactuslinecolor,completelistp = True, textures = [spiketexture]))
        bodylineshapes.append(PlantShape(rightlinelist,brighten(cactuscolor, -40), cactuslinecolor, completelistp = True, textures = [spiketexture]))

    body_shape = PlantShape(body_list, cactuscolor, brighten(cactuslinecolor, -20))
    body_shape = body_shape.destructiveset("textures", [spiketexture])
    body_node = PlantNode([body_shape] + bodylineshapes, 1, math.pi/5, children = [spike_node])
    body_node = body_node.destructiveset("shiftchance", 0.0)
    body_node = body_node.destructiveset("widthvariance", 0.4)
    body_node = body_node.destructiveset("heightvariance", 0.4)
    

        
    return ShopPlant("cactus", body_node, 40)


def testcactus():
    spikecolor = (80, 80, 80)
    
    body_list = [(0,0)]
    body_numofpoints = 20
    roundedness = 3.5
    for x in range(body_numofpoints):
        body_list.append((x, -(5*math.sin(x**roundedness/body_numofpoints**roundedness * math.pi/2 + math.pi/2))))


    cactuscolor = (29, 183, 55)
    cactuslinecolor = brighten(cactuscolor, -20)
    spiketexture = Texture(spikecolor, 0.1, 0.2, 0.05)
    spiketexture.acceptedcolorsspawn = [cactuscolor, cactuslinecolor]

    
    bodylineshapes = []
    number_of_lines = 2
    for i in range(number_of_lines):
        bodylinelist = scalepointlist(body_list, 1-((i+1)/(number_of_lines+1)), 1)
        rightlinelist = flippointlist(bodylinelist)
        bodylinelist = linelist_to_shapelist(bodylinelist)
        rightlinelist = linelist_to_shapelist(rightlinelist)
        bodylineshapes.append(PlantShape(bodylinelist, brighten(cactuscolor, -40), cactuslinecolor,completelistp = True, textures = [spiketexture]))
        bodylineshapes.append(PlantShape(rightlinelist,brighten(cactuscolor, -40), cactuslinecolor, completelistp = True, textures = [spiketexture]))

    body_shape = PlantShape(body_list, cactuscolor, brighten(cactuslinecolor, -20))
    body_shape = body_shape.destructiveset("textures", [spiketexture])
    body_node = PlantNode([body_shape] + bodylineshapes, 1, math.pi/5, children =[])
    body_node = body_node.destructiveset("shiftchance", 0.0)
    body_node = body_node.destructiveset("widthvariance", 0.4)
    body_node = body_node.destructiveset("heightvariance", 0.4)
    

    body_node3 = copy.deepcopy(body_node)
    body_node2 = copy.deepcopy(body_node)
    body_node2 = body_node2.destructiveset("repeatnumseparate", 5)
    body_node2 = body_node2.destructiveset("brancharea", 1)
    body_node2 = body_node2.destructiveset("children", [body_node3])
    

    body_node = body_node.destructiveset("children", [body_node2])
        
    return ShopPlant("testcactus", body_node, 40)




def makecross(plant1, plant2):
    return ShopPlant( "cross", crossplants(plant1, plant2).headnode, 80)


def maketestplant():
    lineup = []
    for y in range(30):
        lineup.append((y, 0))
    lineup = linelist_to_shapelist(lineup)
    
    shape1 = PlantShape(lineup, (200, 0, 0), (100, 0, 0), completelistp = True)
    shape2 = PlantShape(lineup, (0, 255, 0), (0, 100, 0), completelistp = True)
    shape3 = PlantShape(lineup, (0, 0, 255), (0, 0, 100), completelistp = True)
    node1 = PlantNode([shape1], 1, 0)
    node1 = node1.destructivesetfields({"anglevariance" : 0, "brancharea" : 0, "shiftchance" : 0, "angleoffset" : math.pi/2})
    node2 = PlantNode([shape2], 1, 0/5, children = [node1])
    node2 = node2.destructivesetfields({"anglevariance" : 0, "brancharea" : 0, "shiftchance" : 0, "angleoffset" : 0})
    node3 = PlantNode([shape3], 1, 0/5, children = [node2])
    node3 = node3.destructivesetfields({"anglevariance" : 0, "brancharea" : 0, "shiftchance" : 0})
    return ShopPlant("test", node3, 0)
    

def make_shopplant_list():
    shopplantlist = []
    def addnormalshopplants():    
        shopplantlist.append(makestarter())
        shopplantlist.append(makerose())
        shopplantlist.append(makecactus())
        shopplantlist.append(sunflower())
    addnormalshopplants()

    numberofshopplants = len(shopplantlist)


    #shopplantlist.append(testcactus())
    #shopplantlist.append(maketestplant())

    def addcombinationscheat():
        for i in range(10):
            plant1index = random.randint(0, numberofshopplants-1)
            plant2index = random.randint(0, numberofshopplants-1)
            plant1 = shopplantlist[plant1index]
            plant2 = shopplantlist[plant2index]
            devprint("###### making cross between " + plant1.name + " and " + plant2.name)
            shopplantlist.append(makecross(plant1, plant2))
    addcombinationscheat()
    return shopplantlist

