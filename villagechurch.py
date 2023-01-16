from mcpi.minecraft import Minecraft
from random import randint
from random import randrange
from math import ceil
from mcpi import block

mc = Minecraft.create()

class VillageChurch:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y - 1
        self.z = z
        
        self.width = 5
        self.height = 6
        self.length = 9
        
        self.stair_material = 203 # purpur stair
        self.wall_material = 155 # quartz block
        self.roof_material = 201 # purpur block
        self.corner_material = 202 # purpur pillar

    def churchFoundation(self):
        mc.setBlocks(self.x - self.width, self.y, self.z - self.length, self.x + self.width, self.y + (self.height * 2), self.z + self.length, block.AIR)
        mc.setBlocks(self.x - self.width, self.y, self.z - self.length, self.x + self.width, self.y, self.z + self.length, self.wall_material, 1)
        mc.setBlock(self.x, self.y, self.z, block.DIAMOND_BLOCK)
        mc.setBlock(self.x, self.y + 1, self.z + 1, 448)
        
    
    def churchWalls(self):

        mc.setBlocks(self.x - self.width, self.y + 1, self.z - self.length, self.x + self.width, self.y + self.height, self.z + self.length, self.wall_material) 
        mc.setBlocks(self.x - self.width + 1, self.y + 1, self.z - self.length + 1, self.x + self.width - 1, self.y + self.height, self.z + self.length - 1, block.AIR)   

        mc.setBlocks(self.x - self.width, self.y, self.z - self.length, self.x - self.width, self.y + self.height, self.z - self.length, self.corner_material, 2) # Quartz Pillar
        mc.setBlocks(self.x - self.width, self.y, self.z + self.length, self.x - self.width, self.y + self.height, self.z + self.length, self.corner_material, 2)
        mc.setBlocks(self.x + self.width, self.y, self.z - self.length, self.x + self.width, self.y + self.height, self.z - self.length, self.corner_material, 2)
        mc.setBlocks(self.x + self.width, self.y, self.z + self.length, self.x + self.width, self.y + self.height, self.z + self.length, self.corner_material, 2)

        mc.setBlock(self.x, self.y + 2, self.z + self.length, 64, 11) # Back Door, top
        mc.setBlock(self.x, self.y + 1, self.z + self.length, 64, 3)

    def innerPlatform(self):
        mc.setBlocks(self.x - self.width + 1, self.y + 1, self.z - ceil(self.length / 2), self.x + self.width - 1, self.y + 1, self.z - self.length, self.wall_material)
        mc.setBlocks(self.x - self.width + 1, self.y + 1, self.z - ceil(self.length / 2), self.x + self.width - 1, self.y + 1, self.z - ceil(self.length / 2), self.stair_material, 3)
        mc.setBlock(self.x , self.y + 2, self.z - ceil(self.length / 2) - 1, 116)

    def backStainedGlass(self):
        for i in range(self.width * 2 - 3):
            for j in range(self.height - 3):
                mc.setBlock(self.x - 3 + i, self.y + 2 + j, self.z - self.length, block.STAINED_GLASS.id, randint(0, 15))

    def sideStainedGlass(self):
        for i in range(self.length * 2 - 3):
            for j in range(self.height - 3):
                mc.setBlock(self.x - self.width, self.y + 2 + j, self.z + self.length - 2 - i, block.STAINED_GLASS.id, randint(0, 15))
                mc.setBlock(self.x + self.width, self.y + 2 + j, self.z + self.length - 2 - i, block.STAINED_GLASS.id, randint(0, 15))

    def frontStainedGlass(self):
        for i in range(self.width - 3):
            for j in range(self.height - 2):
                mc.setBlock(self.x - 2 - i, self.y + 2 + j, self.z + self.length, block.STAINED_GLASS.id, randint(0, 15))
                mc.setBlock(self.x + 2 + i, self.y + 2 + j, self.z + self.length, block.STAINED_GLASS.id, randint(0, 15))

    def churchRoof(self):
        for i in range(6):
            mc.setBlocks(self.x - self.width - 1 + i, self.y + self.height + i, self.z - self.length - 1, self.x - self.width - 1 + i, self.y + self.height + i, self.z + self.length + 1, self.stair_material, 0)
            mc.setBlocks(self.x + self.width + 1 - i, self.y + self.height + i, self.z - self.length - 1, self.x + self.width + 1 - i, self.y + self.height + i, self.z + self.length + 1, self.stair_material, 1)
        mc.setBlocks(self.x, self.y + self.height + 5, self.z - self.length - 1, self.x, self.y + self.height + 5, self.z + self.length + 1, self.roof_material)
        mc.setBlocks(self.x - self.width + 1, self.y + self.height, self.z - self.length + 1, self.x + self.width - 1, self.y + self.height, self.z + self.length - 1, self.wall_material)
        for i in range(4):
            mc.setBlocks(self.x - self.width + 1 + i, self.y + self.height + 1 + i, self.z + self.length, self.x + self.width - 1 - i, self.y + self.height + 1+ i , self.z + self.length, self.roof_material)
            mc.setBlocks(self.x - self.width + 1 + i, self.y + self.height + 1 + i, self.z - self.length, self.x + self.width - 1 - i, self.y + self.height + 1+ i , self.z - self.length, self.roof_material) 

    def setCross(self, x, y, z):
        mc.setBlocks(x, y - 3, z, x, y + 2, z, block.GOLD_BLOCK)
        mc.setBlocks(x - 2, y, z, x + 2, y, z, block.GOLD_BLOCK)

    def setPews(self):
        for i in range(0, 5, 2):
            mc.setBlocks(self.x - 3, self.y + 1, self.z + i, self.x + 3, self.y + 1, self.z + i, self.stair_material, 2)
        mc.setBlocks(self.x - 1, self.y + 1, self.z + ceil(self.length / 2), self.x + 1, self.y + 1, self.z, block.AIR)     
        mc.setBlocks(self.x - 3, self.y, self.z + ceil(self.length / 2), self.x + 3, self.y , self.z - 1, 169)
        mc.setBlocks(self.x - 1, self.y + 1, self.z + ceil(self.length / 2), self.x + 1, self.y + 1, self.z - 1, 171, 14)
        
        

    def generateChurch(self):
        self.churchFoundation()
        self.churchWalls()
        self.innerPlatform()
        self.backStainedGlass()
        self.sideStainedGlass()
        self.frontStainedGlass()
        self.churchRoof()
        self.setCross(self.x, self.y + 7, self.z - self.length - 1)
        self.setCross(self.x, self.y + 7, self.z + self.length + 1)
        self.setPews()


if __name__ == '__main__':
    mc = Minecraft.create()

    x, y, z = mc.player.getTilePos()
    church = VillageChurch(x, y, z)

    church.generateChurch()