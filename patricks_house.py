from mcpi.minecraft import Minecraft
from random import randint
import random
from random import choice 
from random import randrange
from math import ceil
from mcpi import block

mc = Minecraft.create()

class PatrickHouse:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.height = y - 1 + randint(0 , 2)
        self.length = randrange(6, 10, 2)
        self.width = randrange(6, 10, 2)      

        randomizer = choice([1, 2, 3])
        if randomizer == 1:
            self.log_type = 1
            self.wall_mat = block.WOOD_PLANKS
            self.stair_type = block.STAIRS_STONE_BRICK.id
            self.furnishing = block.STAIRS_WOOD.id
            self.slab_type = 10
            self.glass_colour = 15
        elif randomizer == 2:
            self.log_type = 0
            self.wall_mat = block.SANDSTONE
            self.stair_type = block.STAIRS_STONE_BRICK.id
            self.furnishing = block.STAIRS_SANDSTONE.id
            self.slab_type = 9
            self.glass_colour = 14
        elif randomizer == 3:
            self.log_type = 2
            self.wall_mat = block.NETHER_BRICK
            self.stair_type = block.STAIRS_STONE_BRICK.id
            self.furnishing = block.STAIRS_NETHER_BRICK.id
            self.slab_type = 14
            self.glass_colour = 0
        
        self.single_story = 4
        self.double_story = 8
        self.stories = choice([self.single_story, self.double_story, self.double_story])
    
    def getDoorPos(self):
        return [self.x, self.z - self.length - 2, self.height + 1]

    def generateHouse(self):

        # Grass Foundation
        mc.setBlocks(self.x - self.width - 2, self.height, self.z - self.length - 2, self.x + self.width + 2, self.height, self.z + self.length + 9, block.GRASS)
        mc.setBlocks(self.x - self.width - 3 - randint(0, 2), self.height - 1, self.z - self.length - 3 - randint(0, 2), self.x + self.width + 3 + randint(0, 2), self.height - 5, self.z + self.length + 10 + randint(0, 2), block.GRASS)

        # Clearing out air and placing foundation
        mc.setBlocks(self.x - self.width, self.height + 1, self.z - self.length, self.x + self.width, self.height + 1 + self.stories * 2, self.z + self.length, block.AIR)
        mc.setBlocks(self.x - self.width, self.height, self.z - self.length, self.x + self.width, self.height, self.z + self.length, block.STONE_BRICK)
        mc.setBlock(self.x, self.height, self.z, 169)

        # Placing walls and windows
        mc.setBlocks(self.x - self.width, self.height + 1, self.z - self.length, self.x + self.width, self.height + 5, self.z + self.length, self.wall_mat)
        mc.setBlocks(self.x - self.width, self.height + 2, self.z - self.length, self.x + self.width, self.height + 3, self.z + self.length, block.STAINED_GLASS.id, self.glass_colour)

        # Fixing edge of windows
        mc.setBlocks(self.x - self.width + 1, self.height + 2, self.z - self.length, self.x - self.width + 1, self.height + 3, self.z + self.length, self.wall_mat)
        mc.setBlocks(self.x + self.width - 1, self.height + 2, self.z - self.length, self.x + self.width - 1, self.height + 3, self.z + self.length, self.wall_mat)
        mc.setBlocks(self.x - self.width, self.height + 2, self.z - self.length + 1, self.x + self.width, self.height + 3, self.z - self.length + 1, self.wall_mat)
        mc.setBlocks(self.x - self.width, self.height + 2, self.z + self.length - 1, self.x + self.width, self.height + 3, self.z + self.length - 1, self.wall_mat)
        mc.setBlocks(self.x - self.width, self.height + 2, self.z - 1, self.x + self.width, self.height + 3, self.z + 1, self.wall_mat)
        
        # Placing corner pieces
        log = 17
        mc.setBlocks(self.x - self.width, self.height + 1, self.z - self.length, self.x - self.width, self.height + 5, self.z - self.length, log, self.log_type)
        mc.setBlocks(self.x - self.width, self.height + 1, self.z + self.length, self.x - self.width, self.height + 5, self.z + self.length, log, self.log_type)
        mc.setBlocks(self.x + self.width, self.height + 1, self.z - self.length, self.x + self.width, self.height + 5, self.z - self.length, log, self.log_type)
        mc.setBlocks(self.x + self.width, self.height + 1, self.z + self.length, self.x + self.width, self.height + 5, self.z + self.length, log, self.log_type)

        # Placing doors
        mc.setBlock(self.x, self.height + 2, self.z - self.length, 64, 12) # Front Door, top
        mc.setBlock(self.x, self.height + 1, self.z - self.length, 64, 1) # Front Door, back
        mc.setBlock(self.x, self.height + 2, self.z + self.length, 64, 11) # Back Door, top
        mc.setBlock(self.x, self.height + 1, self.z + self.length, 64, 3) # Back Door, back

        # Stone Patio
        #mc.setBlocks(self.x - 2, self.height, self.z - 7, self.x + 2, self.height, self.z - 7, 98)
        mc.setBlocks(self.x - 2, self.height, self.z - self.length, self.x + 2, self.height, self.z - self.length - 1, 98)

        # Clearing out air
        mc.setBlocks(self.x - self.width + 1, self.height + 1, self.z - self.length + 1, self.x + self.width - 1, self.height + 4, self.z + self.length - 1, block.AIR)

        # Adding centre wall
        mc.setBlocks(self.x - self.width, self.height + 1, self.z, self.x + self.width, self.height + 4, self.z, self.wall_mat)
        mc.setBlock(self.x + 1, self.height + 3, self.z, self.furnishing, 4)
        mc.setBlock(self.x, self.height + 3, self.z, 44, self.slab_type)
        mc.setBlock(self.x - 1, self.height + 3, self.z, self.furnishing, 5)
        mc.setBlocks(self.x - 1, self.height + 1, self.z, self.x + 1, self.height + 2, self.z, 0)

        # Placing roof
        mc.setBlocks(self.x - self.width - 1, (self.height + 5), self.z - self.length - 1, self.x - self.width - 1, (self.height + 5), self.z + self.length + 1, self.stair_type, 0)
        mc.setBlocks(self.x + self.width + 1, (self.height + 5), self.z - self.length - 1, self.x + self.width + 1, (self.height + 5), self.z + self.length + 1, self.stair_type, 1)
        mc.setBlocks(self.x - self.width - 1, (self.height + 5), self.z - self.length - 1, self.x + self.width, (self.height + 5), self.z - self.length - 1, self.stair_type, 2)
        mc.setBlocks(self.x - self.width - 1, (self.height + 5), self.z + self.length + 1, self.x + self.width, (self.height + 5), self.z + self.length + 1, self.stair_type, 3)
        if self.stories == self.single_story:
            for i in range(1, 3):
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 5 + i), self.z - self.length - 1 + i, self.x - self.width - 1 + i, (self.height + 5 + i), self.z + self.length + 1 - i, self.stair_type, 0)
                mc.setBlocks(self.x + self.width + 1 - i, (self.height + 5 + i), self.z - self.length - 1 + i, self.x + self.width + 1 - i, (self.height + 5 + i), self.z + self.length + 1 - i, self.stair_type, 1)
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 5 + i), self.z - self.length - 1 + i, self.x + self.width - i, (self.height + 5 + i), self.z - self.length - 1 + i, self.stair_type, 2)
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 5 + i), self.z + self.length + 1 - i, self.x + self.width - i, (self.height + 5 + i), self.z + self.length + 1 - i, self.stair_type, 3)
            mc.setBlocks(self.x - self.width + 2, self.height + 7, self.z - self.length + 2, self.x + self.width - 2, self.height + 7, self.z + self.length - 2, block.STONE_BRICK)

        # Placing table
        mc.setBlock(self.x + self.width - 3, self.height + 1, self.z + ceil(self.length / 2), 169) # centre of table
        mc.setBlocks(self.x + self.width - 2, self.height + 1, self.z + ceil(self.length / 2) - 1, self.x + self.width - 2, self.height + 1, self.z + ceil(self.length / 2) + 1, self.furnishing, 5)
        mc.setBlocks(self.x + self.width - 4, self.height + 1, self.z + ceil(self.length / 2) - 1, self.x + self.width - 4, self.height + 1, self.z + ceil(self.length / 2) + 1, self.furnishing, 4)
        mc.setBlock(self.x + self.width - 3, self.height + 1, self.z + ceil(self.length / 2) + 1, self.furnishing, 7)
        mc.setBlock(self.x + self.width - 3, self.height + 1, self.z + ceil(self.length / 2) - 1, self.furnishing, 6)

        # Placing bookshelves
        furnishing = [block.CRAFTING_TABLE, block.FURNACE_INACTIVE, block.CHEST, 145]
        random_furnishing = random.choice(furnishing)
        mc.setBlocks(self.x + self.width - 1, self.height + 1, self.z + 1, self.x + self.width - 4, self.height + 3, self.z + 1, 47)
        for i in range(0, self.length - 1, 2):
            random_furnishing = random.choice(furnishing)
            mc.setBlock(self.x - self.width + 1, self.height + 1, self.z + 1 + i, random_furnishing, 5)

        # First level bed-room
        mc.setBlock(self.x + self.width - 3, self.height, self.z - ceil(self.length / 2), 169) # lamp
        mc.setBlock(self.x + self.width - 1, self.height + 1, self.z - ceil(self.length / 2), 26, 11) # Top of bed
        mc.setBlock(self.x + self.width - 2, self.height + 1, self.z - ceil(self.length / 2), 26, 3) # Bottom of bed
        
        # Placing pool
        mc.setBlocks(self.x - self.width, self.height - 3, self.z + self.length, self.x + self.width, self.height, self.z + self.length + 6, block.STONE_BRICK)
        mc.setBlocks(self.x - self.width, self.height + 1, self.z + self.length + 1, self.x + self.width, self.height + 1, self.z + self.length + 6, self.wall_mat)
        mc.setBlocks(self.x - self.width, self.height + 2, self.z + self.length + 1, self.x + self.width, self.height + 2, self.z + self.length + 6, block.FENCE)
        mc.setBlocks(self.x - self.width + 1, self.height + 1, self.z + self.length + 1, self.x + self.width - 1, self.height + 2, self.z + self.length + 5, block.AIR)
        mc.setBlocks(self.x - self.width + 2, self.height - 3, self.z + self.length + 1, self.x + self.width - 2, self.height - 3, self.z + self.length + 5, 169)
        mc.setBlocks(self.x - self.width + 2, self.height, self.z + self.length + 2, self.x + self.width - 2, self.height - 2, self.z + self.length + 4, block.WATER)

        if self.stories == self.double_story:
            # Stairs to second level
            for i in range(1, 4):
                mc.setBlocks(self.x - self.width + 1, self.height + 1, self.z - 4 + i, self.x - self.width + 1, self.height + i, self.z - 4 + i, 47)
            for i in range(5):  
                mc.setBlock(self.x - self.width + 1, self.height + 1 + i, self.z - 4 + i, self.furnishing, 2)
            mc.setBlocks(self.x - self.width + 1, self.height + 5, self.z - 1,self.x - self.width + 1, self.height + 5, self.z - 3, 0)

            # Walls and windows for second storey
            mc.setBlocks(self.x - self.width, self.height + 6, self.z - ceil(self.length / 2), self.x + self.width, self.height + 9, self.z + ceil(self.length / 2), self.wall_mat)
            mc.setBlocks(self.x - self.width, self.height + 7, self.z - ceil(self.length / 2), self.x + self.width, self.height + 8, self.z + ceil(self.length / 2), block.STAINED_GLASS.id, self.glass_colour)
            
            # Fixing windows
            mc.setBlocks(self.x - self.width, self.height + 6, self.z - ceil(self.length / 2), self.x - self.width + 1, self.height + 9, self.z - ceil(self.length / 2) + 1, self.wall_mat)
            mc.setBlocks(self.x - self.width, self.height + 6, self.z + ceil(self.length / 2), self.x - self.width + 1, self.height + 9, self.z + ceil(self.length / 2) - 1, self.wall_mat)
            mc.setBlocks(self.x + self.width, self.height + 6, self.z - ceil(self.length / 2), self.x + self.width - 1, self.height + 9, self.z - ceil(self.length / 2) + 1, self.wall_mat)
            mc.setBlocks(self.x + self.width, self.height + 6, self.z + ceil(self.length / 2), self.x + self.width - 1, self.height + 9, self.z + ceil(self.length / 2) - 1, self.wall_mat)

            # Adding wooden logs to corners
            mc.setBlocks(self.x - self.width, self.height + 6, self. z - ceil(self.length / 2), self.x - self.width, self.height + 9, self. z - ceil(self.length / 2), log, self.log_type)
            mc.setBlocks(self.x - self.width, self.height + 6, self. z + ceil(self.length / 2), self.x - self.width, self.height + 9, self. z + ceil(self.length / 2), log, self.log_type)
            mc.setBlocks(self.x + self.width, self.height + 6, self. z - ceil(self.length / 2), self.x + self.width, self.height + 9, self. z - ceil(self.length / 2), log, self.log_type)
            mc.setBlocks(self.x + self.width, self.height + 6, self. z + ceil(self.length / 2), self.x + self.width, self.height + 9, self. z + ceil(self.length / 2), log, self.log_type)

            # Clearing out middle of second storey
            mc.setBlocks(self.x - self.width + 1, self.height + 6, self.z - ceil(self.length / 2) + 1, self.x + self.width - 1, self.height + 9, self.z + ceil(self.length / 2) - 1, block.AIR)

            # Adding a roof to the second storey
            for i in range(3):
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 9 + i), self.z - ceil(self.length / 2) - 1 + i, self.x - self.width - 1 + i, (self.height + 9 + i), self.z + ceil(self.length / 2) + 1 - i, self.stair_type, 0)
                mc.setBlocks(self.x + self.width + 1 - i, (self.height + 9 + i), self.z - ceil(self.length / 2) - 1 + i, self.x + self.width + 1 - i, (self.height + 9 + i), self.z + ceil(self.length / 2) + 1 - i, self.stair_type, 1)
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 9 + i), self.z - ceil(self.length / 2) - 1 + i, self.x + self.width - i, (self.height + 9 + i), self.z - ceil(self.length / 2) - 1 + i, self.stair_type, 2)
                mc.setBlocks(self.x - self.width - 1 + i, (self.height + 9 + i), self.z + ceil(self.length / 2) + 1 - i, self.x + self.width - i, (self.height + 9 + i), self.z + ceil(self.length / 2) + 1 - i, self.stair_type, 3)                
            mc.setBlocks(self.x - self.width + 2, self.height + 11, self.z - ceil(self.length / 2) + 2, self.x + self.width - 2, self.height + 11, self.z + ceil(self.length / 2) - 2, block.STONE_BRICK)

            # Adding doors to the second storey
            mc.setBlock(self.x, self.height + 7, self.z - ceil(self.length / 2), 64, 12) # Front Door, top
            mc.setBlock(self.x, self.height + 6, self.z - ceil(self.length / 2), 64, 1) # Front Door, back
            mc.setBlock(self.x, self.height + 7, self.z + ceil(self.length / 2), 64, 11) # Back Door, top
            mc.setBlock(self.x, self.height + 6, self.z + ceil(self.length / 2), 64, 3) # Back Door, back

            # Adding fences to balcony
            mc.setBlocks(self.x - self.width, self.height + 6, self.z - ceil(self.length / 2) - 1, self.x + self.width, self.height + 6, self.z - self.length, block.FENCE)
            mc.setBlocks(self.x - self.width + 1, self.height + 6, self.z - ceil(self.length / 2) - 1, self.x + self.width - 1, self.height + 6, self.z - self.length + 1, block.AIR)
            # Back balcony
            mc.setBlocks(self.x - self.width, self.height + 6, self.z + ceil(self.length / 2) + 1, self.x + self.width, self.height + 6, self.z + self.length, block.FENCE)
            mc.setBlocks(self.x - self.width + 1, self.height + 6, self.z + ceil(self.length / 2) + 1, self.x + self.width - 1, self.height + 6, self.z + self.length - 1, block.AIR)
            mc.setBlocks(self.x - 1, self.height + 6, self.z + self.length + 1, self.x + 1, self.height + 6, self.z + self.length, block.AIR)
        
        
if __name__ == '__main__':
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    house = PatrickHouse(x, y, z)

    house.generateHouse()

