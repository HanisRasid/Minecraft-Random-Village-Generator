from Foundation import Foundation, Nature, Well
from roads import Roads, Lamp_Post, zNeg, zPos
from Tree import Tree
from farm import Farm
from mcpi.minecraft import Minecraft
from random import randint
from villagechurch import VillageChurch
from forge import Forge

# houses
from hanishouse import HanisHouse
from Henrys_House import HenryHouse
from laskaris_house import LaskarisHouse
from patricks_house import PatrickHouse

# Assignment 1 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

def genHouse(house_num, x, y, z):
    hanis_house = 1
    henry_house = 2
    laskaris_house = 3
    patrick_house = 4

    house = None

    if house_num == hanis_house:
        house = HanisHouse(x, y, z)
    elif house_num == henry_house:
        house = HenryHouse(x, y, z)
    elif house_num == laskaris_house:
        house = LaskarisHouse(x, y, z)
    elif house_num == patrick_house:
        house = PatrickHouse(x, y, z)
    
    house.generateHouse()

    return house

mc = Minecraft.create()
# mc.postToChat("Hello world")
x, y, z = mc.player.getTilePos()


Foundation(x - 45, y, z - 45).flatten()
Foundation(x - 45, y, z - 45).hill()

Nature(x - 45, y, z - 45).set_grass()
Nature(x - 45, y, z - 45).set_flowers()

road = Roads(x, y, z)
road.create_roads()

pos_x = 1
neg_x = 2
pos_z = 3
neg_z = 4

x_randomizer = randint(0, 5)
z_randomizer = randint(0, 4)


house1 = genHouse(1, x + 30 - x_randomizer, y + 0, z - 25 + z_randomizer)
road.connectToHouse(house1, neg_x)

house2 = genHouse(3, x - 30 + x_randomizer, y + 0, z - 25 + z_randomizer)
road.connectToHouse(house2, pos_z)

house3 = genHouse(4, x - 25  + x_randomizer, y + 0, z + 30 - z_randomizer)
road.connectToHouse(house3, neg_z)

house4 = genHouse(2, x + 30 - x_randomizer, y + 0, z + 25 - z_randomizer)
road.connectToHouse(house4, neg_z)


Farm(x + 25, y, z).placeFarm()
Farm(x - 37, y, z).placeFarm()

VillageChurch(x, y, z - 30).generateChurch()
zPos(x,y-1,z -20).straight(road.church_road())
Forge(x, y, z + 30).generate_forge()
zNeg(x-2,y-1,z+26).straight(road.forge_road())


Well(x, y, z).centre_well()

Lamp_Post(x, y, z).set_lamps()

Tree(x, y - 2, z).Forest()

