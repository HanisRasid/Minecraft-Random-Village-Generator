from mcpi import minecraft
from mcpi import block
import random

mc = minecraft.Minecraft.create()



class HanisHouse:
    def __init__(self, x, y, z):
        self.x = x - 6
        self.y = y + random.randint(0, 2)
        self.z = z - 5

    """generates house"""
    def small_house(self):

        glass_colour = random.randint(1,15)
        concrete_colour = random.randint(1,15)
        plank_colour = random.randint(1,5)
    
        """Grass Foundation"""
        mc.setBlocks(self.x-1, self.y - 1, self.z-3, self.x + 13, self.y - 1, self.z + 13, block.GRASS)
        mc.setBlocks(self.x - 1 - 1 - random.randint(0, 2), self.y - 2, self.z-3 - 1 - random.randint(0, 2), self.x + 13 + 1 + random.randint(0, 2), self.y - 2, self.z + 13 + 1 + random.randint(0, 2), block.GRASS)

        """House foundation"""
        mc.setBlocks(self.x-1, self.y + 1, self.z-3, self.x+12, self.y+10, self.z+15, 0)
        mc.setBlocks(self.x+1, self.y-1, self.z, self.x+10, self.y-1, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x + 1, self.y-1, self.z + 5, self.x + 5, self.y-1, self.z + 10, 98)
        mc.setBlock(self.x+2,self.y-1,self.z+2,89)
        mc.setBlock(self.x+5,self.y-1,self.z+2,89)
        mc.setBlock(self.x+8,self.y-1,self.z+2,89)
        mc.setBlock(self.x+8,self.y-1,self.z+5,89)
        mc.setBlock(self.x+8,self.y-1,self.z+8,89)

        """Hedges"""
        mc.setBlocks(self.x + 1, self.y-1, self.z+5,self.x+5,self.y-1,self.z+5, 17,1)
        mc.setBlocks(self.x + 1, self.y, self.z+5,self.x+5,self.y,self.z+5, 18)
        mc.setBlocks(self.x+1, self.y-1, self.z-1,self.x+11,self.y-1,self.z-1, 17,1)
        mc.setBlocks(self.x+11, self.y-1, self.z-1,self.x+11,self.y-1,self.z+11, 17,1)
        mc.setBlocks(self.x+11, self.y-1, self.z+11,self.x+1,self.y-1,self.z+11, 17,1)
        mc.setBlocks(self.x+1, self.y, self.z-1,self.x+11,self.y,self.z-1, 18)
        mc.setBlocks(self.x+11, self.y, self.z-1,self.x+11,self.y,self.z+11, 18)
        mc.setBlocks(self.x+11, self.y, self.z+11,self.x+1,self.y,self.z+11, 18)

        """Level 1 walls with window"""
        mc.setBlocks(self.x+1, self.y-1, self.z, self.x+10, self.y + 4, self.z, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y-1, self.z, self.x+10, self.y + 4, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y-1, self.z+10, self.x+6, self.y + 4, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+6, self.y-1, self.z+10, self.x+6, self.y + 4, self.z, 5, plank_colour)
        mc.setBlocks(self.x+6, self.y-1, self.z+4, self.x+1, self.y + 4, self.z+4, 5, plank_colour)
        mc.setBlocks(self.x+1, self.y, self.z+3, self.x+1, self.y + 3, self.z+1, 95, glass_colour)

        """Doors facing a certain direction"""
        mc.setBlocks(self.x+6,self.y,self.z+7,self.x+6,self.y+1,self.z+8,0)

        #Left door facing south
        mc.setBlock(self.x+7,self.y+1,self.z+7,64, 13)
        mc.setBlock(self.x+7,self.y,self.z+7,64, 5)

        #Right door facing east
        mc.setBlock(self.x+7,self.y+1,self.z+8,64, 8)
        mc.setBlock(self.x+7,self.y,self.z+8,64, 0)

        """Chest and furnace"""
        mc.setBlock(self.x+7,self.y,self.z+1,61, 3)
        mc.setBlock(self.x+8,self.y,self.z+1,58, 3)
        mc.setBlock(self.x+9,self.y,self.z+1,54, 3)
        
        """Bedroom"""
        mc.setBlocks(self.x+6,self.y,self.z+1,self.x+6,self.y+2,self.z+3,5,plank_colour)
        mc.setBlock(self.x+6,self.y+1,self.z+2,64, 13)
        mc.setBlock(self.x+6,self.y,self.z+2,64, 5)

        #bed
        mc.setBlock(self.x+3, self.y, self.z + 3, 26, 8)
        mc.setBlock(self.x+3, self.y, self.z+2, 26, 0)

        #bedside table
        mc.setBlock(self.x+2,self.y,self.z+3,85)
        mc.setBlock(self.x+2,self.y+1,self.z+3,72)
        
        """Level 1 roof"""
        mc.setBlocks(self.x, self.y+4, self.z-1, self.x+11, self.y+4, self.z+11, 251, concrete_colour)
        mc.setBlocks(self.x, self.y+4, self.z + 6, self.x + 4, self.y+4, self.z + 11, 0)
        mc.setBlocks(self.x+2,self.y+3,self.z+1,self.x+5,self.y+3,self.z+3, 95,glass_colour)

        """Level 2 walls with pillars and windows"""
        mc.setBlocks(self.x+6, self.y+5, self.z+10, self.x+6, self.y+7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z+10, self.x+10, self.y+7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+7, self.y+5, self.z+10, self.x+9, self.y+7, self.z+10, 95, glass_colour)
        mc.setBlocks(self.x+6, self.y+5, self.z+6, self.x+6, self.y+7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z, self.x+10, self.y+7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z+5, self.x+10, self.y+7, self.z+5, 5, plank_colour)
        mc.setBlock(self.x+9, self.y+6, self.z+5, 50, 2)
        mc.setBlock(self.x+7, self.y+6, self.z+5, 50, 1)
        mc.setBlocks(self.x+8, self.y+3, self.z+9, self.x+8, self.y+4, self.z+9, 0)
        mc.setBlocks(self.x+7, self.y, self.z+9, self.x+9, self.y, self.z+9, 53, 2)
        mc.setBlocks(self.x+7, self.y+1, self.z+9, self.x+9, self.y+2, self.z+9, 65)
        mc.setBlocks(self.x+8, self.y+3, self.z+9, self.x+8, self.y+4, self.z+9, 65)
        mc.setBlock(self.x+8, self.y+5, self.z+9, 96)
        mc.setBlocks(self.x+6, self.y+5, self.z+5, self.x+6, self.y+7, self.z+5, 5, plank_colour)
        mc.setBlocks(self.x+5, self.y+5, self.z-1, self.x+11, self.y+7, self.z-1, 251, concrete_colour)

        """Glass pane railing for balcony"""
        mc.setBlocks(self.x+4, self.y+5, self.z-1, self.x, self.y+5, self.z-2, 102)
        mc.setBlocks(self.x+4, self.y+5, self.z-2, self.x, self.y+5, self.z-2, 0)
        mc.setBlocks(self.x+5, self.y+5, self.z+5, self.x, self.y+5, self.z+6, 102)
        mc.setBlocks(self.x+5, self.y+5, self.z+6, self.x, self.y+5, self.z+6, 0)
        mc.setBlocks(self.x, self.y+5, self.z-1, self.x-1, self.y+5, self.z+5, 102)
        mc.setBlocks(self.x-1, self.y+5, self.z-1, self.x-1, self.y+5, self.z+6, 0)

        """Swimming pool"""
        mc.setBlocks(self.x+2, self.y+4, self.z+1, self.x+5, self.y+4, self.z+3, 0)
        mc.setBlocks(self.x+2, self.y+4, self.z+1, self.x+5, self.y+4, self.z+3, 8)

        """Bench"""
        mc.setBlocks(self.x+7, self.y+5, self.z,self.x+8,self.y+5,self.z, 53,7)

        """Level 2 roof"""
        mc.setBlocks(self.x+5,self.y+8,self.z-2, self.x+11, self.y+8,self.z+11,251, concrete_colour)

    def big_house(self):
        """Randomises the material of the house"""
        glass_colour = random.randint(1,15)
        concrete_colour = random.randint(1,15)
        plank_colour = random.randint(1,5)

        """Grass Foundation"""
        mc.setBlocks(self.x-1, self.y - 1, self.z-3, self.x + 13, self.y - 1, self.z + 13, block.GRASS)
        mc.setBlocks(self.x - 1 - 1 - random.randint(0, 2), self.y - 2, self.z-3 - 1 - random.randint(0, 2), self.x + 13 + 1 + random.randint(0, 2), self.y - 2, self.z + 13 + 1 + random.randint(0, 2), block.GRASS)

        """House foundation"""
        mc.setBlocks(self.x-1, self.y, self.z-3, self.x+12, self.y+10, self.z+13, 0)
        mc.setBlocks(self.x+1, self.y-1, self.z, self.x+10, self.y-1, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x + 1, self.y-1, self.z + 5, self.x + 5, self.y-1, self.z + 10, 98)
        mc.setBlock(self.x+2,self.y-1,self.z+2,89)
        mc.setBlock(self.x+5,self.y-1,self.z+2,89)
        mc.setBlock(self.x+8,self.y-1,self.z+2,89)
        mc.setBlock(self.x+8,self.y-1,self.z+5,89)
        mc.setBlock(self.x+8,self.y-1,self.z+8,89)

        """Hedges"""
        mc.setBlocks(self.x + 1, self.y-1, self.z+5,self.x+5,self.y-1,self.z+5, 17,1)
        mc.setBlocks(self.x + 1, self.y, self.z+5,self.x+5,self.y,self.z+5, 18)
        mc.setBlocks(self.x+1, self.y-1, self.z-1,self.x+11,self.y-1,self.z-1, 17,1)
        mc.setBlocks(self.x+11, self.y-1, self.z-1,self.x+11,self.y-1,self.z+11, 17,1)
        mc.setBlocks(self.x+11, self.y-1, self.z+11,self.x+1,self.y-1,self.z+11, 17,1)
        mc.setBlocks(self.x+1, self.y, self.z-1,self.x+11,self.y,self.z-1, 18)
        mc.setBlocks(self.x+11, self.y, self.z-1,self.x+11,self.y,self.z+11, 18)
        mc.setBlocks(self.x+11, self.y, self.z+11,self.x+1,self.y,self.z+11, 18)
        """Level 1 walls with window"""
        mc.setBlocks(self.x+1, self.y-1, self.z, self.x+10, self.y + 4, self.z, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y-1, self.z, self.x+10, self.y + 4, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y-1, self.z+10, self.x+6, self.y + 4, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+6, self.y-1, self.z+10, self.x+6, self.y + 4, self.z, 5, plank_colour)
        mc.setBlocks(self.x+6, self.y-1, self.z+4, self.x+1, self.y + 4, self.z+4, 5, plank_colour)
        mc.setBlocks(self.x+1, self.y, self.z+3, self.x+1, self.y + 3, self.z+1, 95, glass_colour)

        """Doors facing a certain direction"""
        mc.setBlocks(self.x+6,self.y,self.z+7,self.x+6,self.y+1,self.z+8,0)

        #Left door facing south
        mc.setBlock(self.x+7,self.y+1,self.z+7,64, 13)
        mc.setBlock(self.x+7,self.y,self.z+7,64, 5)

        #Right door facing east
        mc.setBlock(self.x+7,self.y+1,self.z+8,64, 8)
        mc.setBlock(self.x+7,self.y,self.z+8,64, 0)

        """Chest and furnace"""
        mc.setBlock(self.x+7,self.y,self.z+1,61, 3)
        mc.setBlock(self.x+8,self.y,self.z+1,58, 3)
        mc.setBlock(self.x+9,self.y,self.z+1,54, 3)
        
        """Bedroom"""
        mc.setBlocks(self.x+6,self.y,self.z+1,self.x+6,self.y+2,self.z+3,5,plank_colour)
        mc.setBlock(self.x+6,self.y+1,self.z+2,64, 13)
        mc.setBlock(self.x+6,self.y,self.z+2,64, 5)

        #bed
        mc.setBlock(self.x+3, self.y, self.z + 3, 26, 8)
        mc.setBlock(self.x+3, self.y, self.z+2, 26, 0)

        #bedside table
        mc.setBlock(self.x+2,self.y,self.z+3,85)
        mc.setBlock(self.x+2,self.y+1,self.z+3,72)
        
        """Level 1 roof"""
        mc.setBlocks(self.x, self.y+4, self.z-1, self.x+11, self.y+4, self.z+11, 251, concrete_colour)
        mc.setBlocks(self.x, self.y+4, self.z + 6, self.x + 4, self.y+4, self.z + 11, 0)
        mc.setBlocks(self.x+2,self.y+3,self.z+1,self.x+5,self.y+3,self.z+3, 95,glass_colour)

        """Level 2 walls with pillars and windows"""
        mc.setBlocks(self.x+6, self.y+5, self.z+10, self.x+6, self.y+7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z+10, self.x+10, self.y+7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+7, self.y+5, self.z+10, self.x+9, self.y+7, self.z+10, 95, glass_colour)
        mc.setBlocks(self.x+6, self.y+5, self.z+6, self.x+6, self.y+7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z, self.x+10, self.y+7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+5, self.z+5, self.x+10, self.y+7, self.z+5, 5, plank_colour)
        mc.setBlock(self.x+9, self.y+6, self.z+5, 50, 2)
        mc.setBlock(self.x+7, self.y+6, self.z+5, 50, 1)
        mc.setBlocks(self.x+8, self.y+3, self.z+9, self.x+8, self.y+4, self.z+9, 0)
        mc.setBlocks(self.x+7, self.y, self.z+9, self.x+9, self.y, self.z+9, 53, 2)
        mc.setBlocks(self.x+7, self.y+1, self.z+9, self.x+9, self.y+3, self.z+9, 65)
        mc.setBlocks(self.x+8, self.y+3, self.z+9, self.x+8, self.y+4, self.z+9, 65)
        mc.setBlock(self.x+8, self.y+5, self.z+9, 96)
        mc.setBlocks(self.x+6, self.y+5, self.z+5, self.x+6, self.y+7, self.z+5, 5, plank_colour)
        mc.setBlocks(self.x+5, self.y+5, self.z-1, self.x+11, self.y+7, self.z-1, 251, concrete_colour)

        """Glass pane railing for balcony"""
        mc.setBlocks(self.x+4, self.y+5, self.z-1, self.x, self.y+5, self.z-2, 102)
        mc.setBlocks(self.x+4, self.y+5, self.z-2, self.x, self.y+5, self.z-2, 0)
        mc.setBlocks(self.x+5, self.y+5, self.z+5, self.x, self.y+5, self.z+6, 102)
        mc.setBlocks(self.x+5, self.y+5, self.z+6, self.x, self.y+5, self.z+6, 0)
        mc.setBlocks(self.x, self.y+5, self.z-1, self.x-1, self.y+5, self.z+5, 102)
        mc.setBlocks(self.x-1, self.y+5, self.z-1, self.x-1, self.y+5, self.z+6, 0)

        """Swimming pool"""
        mc.setBlocks(self.x+2, self.y+4, self.z+1, self.x+5, self.y+4, self.z+3, 0)
        mc.setBlocks(self.x+2, self.y+4, self.z+1, self.x+5, self.y+4, self.z+3, 8)

        """Bench"""
        mc.setBlocks(self.x+7, self.y+5, self.z,self.x+8,self.y+5,self.z, 53,7)

        """Level 2 roof"""
        mc.setBlocks(self.x+5,self.y+8,self.z-2, self.x+11, self.y+8,self.z+11,251, concrete_colour)

        """Level 3 walls with pillars and windows"""
        mc.setBlocks(self.x+6, self.y+4 +5, self.z+10, self.x+6, self.y+4 +7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+10, self.y+4 +5, self.z+10, self.x+10, self.y+4 +7, self.z+10, 5, plank_colour)
        mc.setBlocks(self.x+7, self.y+4 +5, self.z+10, self.x+9, self.y+4 +7, self.z+10, 95, glass_colour)
        mc.setBlocks(self.x+6, self.y+4 +5, self.z, self.x+6, self.y+4 +7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+4 +5, self.z, self.x+10, self.y+4 +7, self.z+9, 95, glass_colour)
        mc.setBlocks(self.x+10, self.y+4 +5, self.z+5, self.x+10, self.y+4 +7, self.z+5, 5, plank_colour)
        mc.setBlock(self.x+9, self.y+4 +6, self.z+5, 50, 2)
        mc.setBlock(self.x+7, self.y+4 +6, self.z+5, 50, 1)
        mc.setBlocks(self.x+8, self.y+4 +3, self.z+9, self.x+8, self.y+4 +4, self.z+9, 0)
        mc.setBlocks(self.x+8, self.y+4 +2, self.z+9, self.x+8, self.y+4 +4, self.z+9, 65)
        mc.setBlock(self.x+8, self.y+4 +5, self.z+9, 96)
        mc.setBlocks(self.x+6, self.y+4 +5, self.z+5, self.x+6, self.y+4 +7, self.z+5, 5, plank_colour)
        mc.setBlocks(self.x+6, self.y+4 +5, self.z-1, self.x+10, self.y+4 +7, self.z-1, 5, plank_colour)

        """Enchantment room"""
        mc.setBlocks(self.x+7, self.y+4 +5, self.z, self.x+9, self.y+4 +7, self.z, 47)
        mc.setBlock(self.x + 8, self.y+9, self.z+1, 116)
        mc.setBlock(self.x + 7, self.y+9, self.z+1, 117)
        mc.setBlock(self.x + 9, self.y+9, self.z+1, 118)


        """Level 3 roof"""
        mc.setBlocks(self.x+5,self.y+12,self.z-2, self.x+11, self.y+12,self.z+11,251, concrete_colour)

    def generateHouse(self):
        house = random.randint(0, 1)
        if house == 0:
            self.small_house()
        else:
            self.big_house()

    def getDoorPos(self):
        return [self.x, self.z + 7, self.y]

if __name__ == '__main__':
    x, y, z = mc.player.getTilePos()
    y = mc.getHeight(x,z)

    house = HanisHouse(x, y, z)

    house.generateHouse()

