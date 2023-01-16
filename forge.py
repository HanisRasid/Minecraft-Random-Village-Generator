from mcpi import minecraft
from mcpi import block
import random

mc = minecraft.Minecraft.create()

class Forge:
    def __init__(self,x,y,z):
        self.x = x - 2
        self.y = y
        self.z = z - 4

    def generate_forge(self):
        """Randomises the materials of the forge"""
        bases = [24,4]
        log = random.randint(0,4)
        baseblock = random.choice(bases)
        plankcolour = random.randint(1,15)
        
        if baseblock == 4:
            stairtype = 67 
        else:
            stairtype = 128

        """Foundation and structure"""
        mc.setBlocks(self.x - 2, self.y, self.z +1, self.x + 7, self.y+5, self.z + 8, 0)
        mc.setBlocks(self.x-1,self.y,self.z+1,self.x+1,self.y,self.z+1, stairtype,2)
        mc.setBlocks(self.x-2,self.y,self.z+2,self.x+7,self.y,self.z+8,baseblock)
        mc.setBlocks(self.x-2,self.y+4,self.z+2,self.x+7,self.y+4,self.z+8,baseblock)
        mc.setBlocks(self.x-2,self.y+5,self.z+2,self.x+7,self.y+5,self.z+8,44)
        mc.setBlocks(self.x-1,self.y+5,self.z+3,self.x+6,self.y+5,self.z+7, 0)
        mc.setBlocks(self.x-2,self.y+1,self.z+6,self.x+1,self.y+3,self.z+8,baseblock)
        mc.setBlocks(self.x+2,self.y+1,self.z+8,self.x+6,self.y+3,self.z+8,5, plankcolour)
        mc.setBlocks(self.x+7,self.y+1,self.z+3,self.x+7,self.y+3,self.z+7,5, plankcolour)
        mc.setBlocks(self.x+5,self.y+1,self.z+2,self.x+6,self.y+3,self.z+2,5, plankcolour)
        mc.setBlocks(self.x+2,self.y+1,self.z+5,self.x+3,self.y+3,self.z+5,5, plankcolour)
        mc.setBlocks(self.x+4,self.y+1,self.z+3,self.x+4,self.y+3,self.z+4,5, plankcolour)
        mc.setBlocks(self.x+4,self.y+1,self.z+2,self.x+4,self.y+4,self.z+2,17, log)
        mc.setBlocks(self.x+7,self.y+1,self.z+2,self.x+7,self.y+4,self.z+2,17, log)
        mc.setBlocks(self.x+7,self.y+1,self.z+8,self.x+7,self.y+4,self.z+8,17, log)
        mc.setBlock(self.x+3,self.y+2,self.z+8,20)
        mc.setBlock(self.x+5,self.y+2,self.z+8,20)
        mc.setBlock(self.x+7,self.y+2,self.z+4,20)
        mc.setBlocks(self.x+7,self.y+2,self.z+6,20)

        """Furniture"""
        mc.setBlock(self.x+5,self.y+1,self.z+7,53,2)
        mc.setBlock(self.x+6,self.y+1,self.z+6,53)
        mc.setBlock(self.x+5,self.y+1,self.z+6,85)
        mc.setBlock(self.x+5,self.y+2,self.z+6,72)
        mc.setBlock(self.x+6,self.y+1,self.z+7,54)
        mc.setBlock(self.x+2,self.y+1,self.z+7,14)
        mc.setBlock(self.x+2,self.y+1,self.z+7,14)
        mc.setBlock(self.x+2,self.y+2,self.z+7,15)
        mc.setBlock(self.x+2,self.y+3,self.z+7,16)
        mc.setBlock(self.x+2,self.y+1,self.z+6,21)
        mc.setBlock(self.x+2,self.y+2,self.z+6,56)
        mc.setBlock(self.x+2,self.y+3,self.z+6,129)

        """Decoration"""
        mc.setBlocks(self.x-2,self.y+2,self.z+6,self.x,self.y+2,self.z+7,101)
        mc.setBlocks(self.x-1,self.y+2,self.z+7,self.x,self.y+2,self.z+7,0)
        mc.setBlocks(self.x-1,self.y+1,self.z+7,self.x,self.y+1,self.z+7,11)
        mc.setBlocks(self.x-2,self.y+1,self.z+2,self.x-2,self.y+3,self.z+2,85)
        mc.setBlocks(self.x+2,self.y+1,self.z+2,self.x+2,self.y+3,self.z+2,85)
        mc.setBlock(self.x+1,self.y+1,self.z+5,baseblock)
        mc.setBlocks(self.x+1,self.y+2,self.z+5,self.x+1,self.y+3,self.z+5,61,4)
        mc.setBlock(self.x-1,self.y+1,self.z+3,145,3)
        mc.setBlocks(self.x+4,self.y+1,self.z+3,self.x+4,self.y+2,self.z+3,0)
        mc.setBlock(self.x+6,self.y+2,self.z+3,50,2)
        mc.setBlock(self.x+4,self.y+2,self.z+7,50,4)



# x, y, z = mc.player.getTilePos()

# forge = Forge(x,y,z)

# forge.generate_forge()
