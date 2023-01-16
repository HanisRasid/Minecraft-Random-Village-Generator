import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event as event
import random

mc = minecraft.Minecraft.create()

p = mc.player.getTilePos()

class Foundation:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
  
    def flatten(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + 90, self.y + 50, self.z + 90, 166) # Barrier
        mc.setBlocks(self.x, self.y, self.z, self.x + 90, self.y + 50, self.z + 90, block.AIR) # Air 
        mc.setBlocks(self.x, self.y - 1, self.z, self.x + 90, self.y - 10, self.z + 90, block.GRASS) # Grass

        for i in range(2, 11):
            mc.setBlocks(self.x - i - random.randint(0, 2), self.y - i, self.z - i - random.randint(0, 2), self.x + 90 + i + random.randint(0, 2), self.y - 10, self.z + 90 + i + random.randint(0, 2), block.GRASS) # Grass

    def hill(self):
        # The code below will set a randomly sized hill in the centre of the foundation
        topnegx, topposx, topnegz, topposz = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
        botnegx, botposx, botnegz, botposz = random.randint(10, 15), random.randint(10, 15), random.randint(10, 15), random.randint(10, 15)

        mc.setBlocks(self.x - 2 + 45 - topnegx, self.y + 1, self.z - 2 + 45 - topnegz, self.x + 2 + 45 + topposx, self.y + 1, self.z + 2 + 45 + topposz, block.GRASS) # Hill Top
        mc.setBlocks(self.x - 2 + 45 - topnegx, self.y + 1, self.z - 2 + 45 - topnegz, self.x - 2 + 45 - topnegx + random.randint(1, 5), self.y + 1, self.z - 2 + 45 - topnegz, block.AIR) # Hill Top Corner 1
        mc.setBlocks(self.x - 2 + 45 - topnegx, self.y + 1, self.z - 2 + 45 - topnegz, self.x - 2 + 45 - topnegx, self.y + 1, self.z - 2 + 45  - topnegz + random.randint(1, 5), block.AIR) # Hill Top Corner 2
        mc.setBlocks(self.x - 2 + 45 - topnegx, self.y + 1, self.z + 2 + 45 + topposz, self.x - 2 + 45 - topnegx + random.randint(1, 5), self.y + 1, self.z + 2 + 45 + topposz, block.AIR) # Hill Top Corner 3
        mc.setBlocks(self.x - 2 + 45 - topnegx, self.y + 1, self.z + 2 + 45 + topposz, self.x - 2 + 45 - topnegx, self.y + 1, self.z + 2 + 45 + topposz - random.randint(1, 5), block.AIR) # Hill Top Corner 4
        mc.setBlocks(self.x + 2 + 45 + topposx, self.y + 1, self.z - 2 + 45 - topnegz, self.x + 2 + 45 + topposx - random.randint(1, 5), self.y + 1, self.z - 2 + 45 - topnegz, block.AIR) # Hill Top Corner 5
        mc.setBlocks(self.x + 2 + 45 + topposx, self.y + 1, self.z - 2 + 45 - topnegz, self.x + 2 + 45 + topposx, self.y + 1, self.z - 2 + 45 - topnegz + random.randint(1, 5), block.AIR) # Hill Top Corner 6
        mc.setBlocks(self.x + 2 + 45 + topposx, self.y + 1, self.z + 2 + 45 + topposz, self.x + 2 + 45 + topposx - random.randint(1, 5), self.y + 1, self.z + 2 + 45 + topposz, block.AIR) # Hill Top Corner 7
        mc.setBlocks(self.x + 2 + 45 + topposx, self.y + 1, self.z + 2 + 45 + topposz, self.x + 2 + 45 + topposx, self.y + 1, self.z + 2 + 45 + topposz - random.randint(1, 5), block.AIR) # Hill Top Corner 8

        mc.setBlocks(self.x - 2 + 45 - botnegx, self.y, self.z - 2 + 45 - botnegz, self.x + 2 + 45 + botposx, self.y, self.z + 2 + 45 + botposz, block.GRASS) # Hill Mid
        mc.setBlocks(self.x - 2 + 45 - botnegx, self.y, self.z - 2 + 45 - botnegz, self.x - 2 + 45 - botnegx + random.randint(1, 10), self.y, self.z - 2 + 45 - botnegz, block.AIR) # Bot Corner 1
        mc.setBlocks(self.x - 2 + 45 - botnegx, self.y, self.z - 2 + 45 - botnegz, self.x - 2 + 45 - botnegx, self.y, self.z - 2 + 45  - botnegz + random.randint(1, 10), block.AIR) # Bot Corner 2
        mc.setBlocks(self.x - 2 + 45 - botnegx, self.y, self.z + 2 + 45 + botposz, self.x - 2 + 45 - botnegx + random.randint(1, 10), self.y, self.z + 2 + 45 + botposz, block.AIR) # Bot Corner 3
        mc.setBlocks(self.x - 2 + 45 - botnegx, self.y, self.z + 2 + 45 + botposz, self.x - 2 + 45 - botnegx, self.y, self.z + 2 + 45 + botposz - random.randint(1, 10), block.AIR) # Bot Corner 4
        mc.setBlocks(self.x + 2 + 45 + botposx, self.y, self.z - 2 + 45 - botnegz, self.x + 2 + 45 + botposx - random.randint(1, 10), self.y, self.z - 2 + 45 - botnegz, block.AIR) # Bot Corner 5
        mc.setBlocks(self.x + 2 + 45 + botposx, self.y, self.z - 2 + 45 - botnegz, self.x + 2 + 45 + botposx, self.y, self.z - 2 + 45 - botnegz + random.randint(1, 10), block.AIR) # Bot Corner 6
        mc.setBlocks(self.x + 2 + 45 + botposx, self.y, self.z + 2 + 45 + botposz, self.x + 2 + 45 + botposx - random.randint(1, 10), self.y, self.z + 2 + 45 + botposz, block.AIR) # Bot Corner 7
        mc.setBlocks(self.x + 2 + 45 + botposx, self.y, self.z + 2 + 45 + botposz, self.x + 2 + 45 + botposx, self.y, self.z + 2 + 45 + botposz - random.randint(1, 10), block.AIR) # Bot Corner 8
        

class Nature:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
  
    def set_grass(self):
        for xa in range(0, 90):
            for za in range(0, 90):
                if random.randint(1, 10) == 10:
                    mc.setBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za) + 1, self.z + za, 31, 1)

    def set_flowers(self):
        flowers = [[31, 2], [37, 0], [38, 0], [38, 1], [38, 2], [38, 3], [38, 4], [38, 5], [38, 6], [38, 7], [38, 8]]

        for xa in range(0, 90):
            for za in range(0, 90):
                if random.randint(1, 80) == 1:
                    flower = random.choice(flowers)
                    mc.setBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za) + 1, self.z + za, flower[0], flower[1])

class Well:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_well(self):
        while 1 > 0:
            randX = random.randint(-35, 35)
            randZ = random.randint(-35, 35)
            self.x = p.x + randX
            self.z = p.z + randZ

            arr = list(mc.getBlocks(self.x, mc.getHeight(self.x, self.z), self.z, self.x + 3, mc.getHeight(self.x + 3, self.z + 3) + 1, self.z + 3))
            print(arr)
            if 98 not in arr and 120 not in arr:
                self.well()
                break

    def centre_well(self):
        self.y = mc.getHeight(self.x, self.z) + 1
        mc.setBlocks(self.x - 1, self.y - 1, self.z - 1, self.x + 4, self.y - 3, self.z + 4, block.STONE_BRICK)
        self.well()

    def well(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + 3, self.y - 7, self.z + 3, block.COBBLESTONE) # Well
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + 2, self.y - 6, self.z + 2, block.AIR) # Well Hole
        mc.setBlocks(self.x + 1, self.y - 1, self.z + 1, self.x + 2, self.y - 6, self.z + 2, block.WATER) # Well Hole
        mc.setBlocks(self.x, self.y + 1, self.z, self.x + 3, self.y + 2, self.z + 3, block.FENCE) # Well Stand
        mc.setBlocks(self.x, self.y + 1, self.z + 1, self.x + 3, self.y + 2, self.z + 2, block.AIR) # Air 1
        mc.setBlocks(self.x + 1, self.y + 1, self.z, self.x + 2, self.y + 2, self.z + 3, block.AIR) # Air 2
        mc.setBlocks(self.x, self.y + 3, self.z, self.x, self.y + 3, self.z, 44, 3) # Well Corner 1
        mc.setBlocks(self.x + 3, self.y + 3, self.z, self.x + 3, self.y + 3, self.z, 44, 3) # Well Corner 2
        mc.setBlocks(self.x + 3, self.y + 3, self.z + 3, self.x + 3, self.y + 3, self.z + 3, 44, 3) # Well Corner 3
        mc.setBlocks(self.x, self.y + 3, self.z + 3, self.x, self.y + 3, self.z + 3, 44, 3) # Well Corner 4
        mc.setBlocks(self.x + 1, self.y + 3, self.z, self.x + 2, self.y + 3, self.z, 67, 6) # Well Side Bit 1
        mc.setBlocks(self.x + 3, self.y + 3, self.z + 1, self.x + 3, self.y + 3, self.z + 2, 67, 5) # Well Side Bit 2
        mc.setBlocks(self.x + 1, self.y + 3, self.z + 3, self.x + 2, self.y + 3, self.z + 3, 67, 7) # Well Side Bit 3
        mc.setBlocks(self.x, self.y + 3, self.z + 1, self.x, self.y + 3, self.z + 2, 67, 4) # Well Side Bit 4
        mc.setBlocks(self.x + 1, self.y + 3, self.z + 1, self.x + 2, self.y + 3, self.z + 2, block.COBBLESTONE) # Well Top


# Foundation(p.x - 45, p.y - 2, p.z - 45).flatten()
# Foundation(p.x - 45, p.y - 2, p.z - 45).hill()

