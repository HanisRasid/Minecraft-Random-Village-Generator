from mcpi.minecraft import Minecraft
from random import randint
from random import choice
from random import randrange
from mcpi import block

# Farm class - need to be more advanced?
mc = Minecraft.create()

class Farm:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z
                                                        
        # self.farm_height = randint(0, 1)
        # self.x += x
        # self.y += y
        # self.z -= z

        self.height = mc.getHeight(self.x, self.z) # self.farm_height
        self.length = 10
        self.width = randrange(6, 10, 2)

    def setWater(self):
        # creates water pattern
        num = randint(1, 3)

        if num == 1:
            mc.setBlocks(self.x + self.width / 2, self.height, self.z + 1, self.x + self.width / 2, self.height, self.z + self.length - 1, block.WATER_STATIONARY)
            mc.setBlocks(self.x + 1, self.height, self.z + self.length / 2, self.x + self.width - 1, self.height, self.z + self.length / 2, block.WATER_STATIONARY)
        elif num == 2:
            mc.setBlocks(self.x + 1, self.height,  self.z + 1, self.x + 1, self.height, self.z + self.length - 1, block.WATER_STATIONARY)
            mc.setBlocks(self.x + self.width / 2, self.height, self.z + 1, self.x + self.width / 2, self.height, self.z + self.length - 1, block.WATER_STATIONARY)
            mc.setBlocks(self.x + self.width - 1, self.height, self.z + 1, self.x + self.width - 1, self.height, self.z + self.length - 1, block.WATER_STATIONARY)
        elif num == 3:
            mc.setBlocks(self.x + 2, self.height, self.z + 2, self.x + self.width - 2, self.height, self.z + self.length - 2, block.WATER_STATIONARY)
            mc.setBlocks(self.x + 3, self.height, self.z + 3, self.x + self.width - 3, self.height, self.z + self.length - 3, block.FARMLAND)
        
    def setProduce(self):
        wheat = 59
        potatoes = 142
        carrots = 141
        melon = 105
        beetroot = 207
        pumpkin = 104

        for i in range(self.width + 1):
            blk = choice([wheat, potatoes, carrots, melon, pumpkin, beetroot])
            for j in range(self.length + 1):
                if mc.getBlock(self.x + i, self.height, self.z + j) == block.FARMLAND.id:
                    blk_type = randint(1, 7)
                    mc.setBlock(self.x + i, self.height + 1, self.z + j, blk, blk_type)
                
    def placeFarm(self):
        mc.setBlocks(self.x - 1, self.height, self.z - 1, self.x + self.width + 1, self.height , self.z + self.length + 1, block.WOOD)
        mc.setBlocks(self.x, self.height, self.z, self.x + self.width, self.height , self.z + self.length, block.FARMLAND)
        self.setWater()
        self.setProduce()

# main for testing just file, can be removed/commented
# if __name__ == '__main__':
#     x, y, z = mc.player.getTilePos()
#     farm = Farm(x, y, z)
    
#     farm.placeFarm()
