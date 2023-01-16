import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event as event
import random

mc = minecraft.Minecraft.create()

class HenryHouse:
    def __init__(self, x, y, z):
        self.x = x - 28
        self.y = y + random.randint(0, 2)
        self.z = z - 23
        self.doorx = self.x
        self.doorz = self.z

    def House1(self):
        Materials = [[block.WOOD_PLANKS, 17, 53], [block.BRICK_BLOCK, block.STONE_BRICK, 109], [block.STONE_BRICK, block.STONE_BRICK, 109]]
        CurrentMaterial = random.choice(Materials)

        mc.setBlocks(self.x + 15, self.y - 1 , self.z + 15, self.x + 41, self.y - 10, self.z + 31, block.GRASS) # Grass
        mc.setBlocks(self.x + 15 - 1 - random.randint(0, 2), self.y - 2, self.z + 15 - 1 - random.randint(0, 2), self.x + 41 + 1 + random.randint(0, 2), self.y - 2, self.z + 31 + 1 + random.randint(0, 2), block.GRASS) # Grass

        mc.setBlocks(self.x + 15, self.y, self.z + 15, self.x + 41, self.y + 20, self.z + 31, block.AIR) # Air Space

        #mc.setBlocks(self.x + 14, self.y - 1 , self.z + 14, self.x + 31, self.y - 2, self.z + 31, block.WATER) # Water

        mc.setBlocks(self.x + 18, self.y - 1, self.z + 23, self.x + 27, self.y + 7, self.z + 28, CurrentMaterial[0]) # Walls 1
        mc.setBlocks(self.x + 23, self.y - 1, self.z + 18, self.x + 27, self.y + 7, self.z + 28, CurrentMaterial[0]) # Walls 2

        mc.setBlocks(self.x + 19, self.y, self.z + 24, self.x + 26, self.y + 6, self.z + 27, block.AIR) # Air
        mc.setBlocks(self.x + 24, self.y, self.z + 19, self.x + 26, self.y + 6, self.z + 27, block.AIR) # Air

        mc.setBlocks(self.x + 19, self.y - 1 , self.z + 24, self.x + 26, self.y - 1, self.z + 27, block.WOOD_PLANKS) # Wood Base 1
        mc.setBlocks(self.x + 24, self.y - 1 , self.z + 19, self.x + 26, self.y - 1, self.z + 27, block.WOOD_PLANKS) # Wood Base 2

        mc.setBlocks(self.x + 18, self.y + 3, self.z + 24, self.x + 27, self.y + 3, self.z + 28, block.WOOD_PLANKS) # Upstairs base 1 
        mc.setBlocks(self.x + 23, self.y + 3, self.z + 18, self.x + 27, self.y + 3, self.z + 28, block.WOOD_PLANKS) # Upstairs base 2

        mc.setBlocks(self.x + 21, self.y + 3, self.z + 26, self.x + 24, self.y + 3, self.z + 28, block.AIR) # Stairs Hole 1
        mc.setBlocks(self.x + 20, self.y + 4, self.z + 25, self.x + 24, self.y + 4, self.z + 27, block.FENCE) # Stairs Fence
        mc.setBlocks(self.x + 21, self.y + 4, self.z + 26, self.x + 24, self.y + 4, self.z + 27, block.AIR) # Stairs Hole 2
        mc.setBlocks(self.x + 19, self.y + 4, self.z + 25, self.x + 19, self.y + 4, self.z + 25, block.FENCE) # Stairs Corner
        mc.setBlocks(self.x + 19, self.y + 4, self.z + 25, self.x + 19, self.y + 4, self.z + 25, block.AIR) # Stairs Corner Air


        mc.setBlock(self.x + 24, self.y + 4, self.z + 19, 26, 10) # bed 1 top half
        mc.setBlock(self.x + 24, self.y + 4, self.z + 20, 26, 2) # bed 1 bottom half

        mc.setBlock(self.x + 26, self.y + 4, self.z + 19, 26, 10) # bed 2 top half
        mc.setBlock(self.x + 26, self.y + 4, self.z + 20, 26, 2) # bed 2 bottom half

        mc.setBlock(self.x + 26, self.y, self.z + 19, 61, 3) # furnace 

        if random.randint(0, 1) == 1:
            mc.setBlock(self.x + 25, self.y, self.z + 19, 62, 3) # furnace 

        else:
            mc.setBlock(self.x + 25, self.y, self.z + 19, 118) # cauldron

        mc.setBlock(self.x + 24, self.y, self.z + 19, block.CRAFTING_TABLE) # crafting table

        mc.setBlock(self.x + 26, self.y, self.z + 27, 54) # chest
        mc.setBlock(self.x + 25, self.y, self.z + 27, 54) # chest

        for i in range(4):
            mc.setBlocks(self.x + 21 + i, self.y + i, self.z + 26, self.x + 21 + i, self.y + i, self.z + 27, 53) # Stairs

        mc.setBlocks(self.x + 18, self.y - 1, self.z + 23, self.x + 18, self.y + 6, self.z + 23, CurrentMaterial[1]) # Corners 1
        mc.setBlocks(self.x + 18, self.y - 1, self.z + 28, self.x + 18, self.y + 6, self.z + 28, CurrentMaterial[1]) # Corners 2
        mc.setBlocks(self.x + 23, self.y - 1, self.z + 18, self.x + 23, self.y + 6, self.z + 18, CurrentMaterial[1]) # Corners 3
        mc.setBlocks(self.x + 27, self.y - 1, self.z + 18, self.x + 27, self.y + 6, self.z + 18, CurrentMaterial[1]) # Corners 4
        mc.setBlocks(self.x + 27, self.y - 1, self.z + 28, self.x + 27, self.y + 6, self.z + 28, CurrentMaterial[1]) # Corners 5

        mc.setBlocks(self.x + 18, self.y + 3, self.z + 24, self.x + 18, self.y + 3, self.z + 27, CurrentMaterial[1], 8) # Side Support 1
        mc.setBlocks(self.x + 19, self.y + 3, self.z + 23, self.x + 23, self.y + 3, self.z + 23, CurrentMaterial[1], 4) # Side Support 2
        mc.setBlocks(self.x + 19, self.y + 3, self.z + 28, self.x + 26, self.y + 3, self.z + 28, CurrentMaterial[1], 4) # Side Support 3
        mc.setBlocks(self.x + 24, self.y + 3, self.z + 18, self.x + 26, self.y + 3, self.z + 18, CurrentMaterial[1], 4) # Side Support 4
        mc.setBlocks(self.x + 23, self.y + 3, self.z + 19, self.x + 23, self.y + 3, self.z + 22, CurrentMaterial[1], 8) # Side Support 5
        mc.setBlocks(self.x + 27, self.y + 3, self.z + 19, self.x + 27, self.y + 3, self.z + 27, CurrentMaterial[1], 8) # Side Support 6


        if random.randint(0, 1) == 0:
            mc.setBlocks(self.x + 19, self.y + 3, self.z + 19, self.x + 23, self.y + 3 , self.z + 22, CurrentMaterial[0]) # Balcony 
            mc.setBlocks(self.x + 19, self.y + 4, self.z + 19, self.x + 22, self.y + 4 , self.z + 22, 85) # Balcony Fence
            mc.setBlocks(self.x + 20, self.y + 4, self.z + 20, self.x + 22, self.y + 4 , self.z + 22, block.AIR) # Balcony Fence Spaces
            mc.setBlocks(self.x + 18, self.y + 4, self.z + 19, self.x + 18, self.y + 4 , self.z + 19, 85) # Balcony Fence Fiself.x
            mc.setBlocks(self.x + 18, self.y + 4, self.z + 19, self.x + 18, self.y + 4 , self.z + 19, block.AIR) # Balcony Fence Fiself.x 2

            mc.setBlock(self.x + 22, self.y + 5, self.z + 22, 50, 4) # Balc torch left
            mc.setBlock(self.x + 20, self.y + 5, self.z + 22, 50, 4) # Balc torch right

            mc.setBlock(self.x + 21, self.y + 5, self.z + 23, 64, 9) # Balc Door 1 Top Half
            mc.setBlock(self.x + 21, self.y + 4, self.z + 23, 64, 1) # Balc Door 1 Bottom Half
        else:
            mc.setBlocks(self.x + 19, self.y + 5, self.z + 19, self.x + 23, self.y + 5, self.z + 23, block.GLASS) # No Balc Window
            mc.setBlocks(self.x + 19, self.y + 5, self.z + 19, self.x + 22, self.y + 5, self.z + 22, block.AIR) # No Balc Window

        mc.setBlock(self.x + 24, self.y + 5, self.z + 22, 50, 0) # Up stairs torch 1
        mc.setBlock(self.x + 22, self.y + 5, self.z + 24, 50, 3) # Up stairs torch 2 
        mc.setBlock(self.x + 25, self.y + 5, self.z + 27, 50, 4) # Up stairs torch 3

        mc.setBlock(self.x + 25, self.y + 1, self.z + 27, 50, 4) # Down Stairs torch 1
        mc.setBlock(self.x + 25, self.y + 2, self.z + 19, 50, 3) # Down Stairs torch 2
        mc.setBlock(self.x + 22, self.y + 1, self.z + 24, 50, 3) # Down Stairs torch 3
        


        mc.setBlocks(self.x + 17, self.y + 7, self.z + 22, self.x + 17, self.y + 7, self.z + 29, CurrentMaterial[2]) # Roof 1
        mc.setBlocks(self.x + 22, self.y + 7, self.z + 17, self.x + 22, self.y + 7, self.z + 22, CurrentMaterial[2]) # Roof 2
        mc.setBlocks(self.x + 18, self.y + 7, self.z + 22, self.x + 21, self.y + 7, self.z + 22, CurrentMaterial[2], 2) # Roof 3
        mc.setBlocks(self.x + 23, self.y + 7, self.z + 17, self.x + 27, self.y + 7, self.z + 17, CurrentMaterial[2], 2) # Roof 4
        mc.setBlocks(self.x + 28, self.y + 7, self.z + 17, self.x + 28, self.y + 7, self.z + 17, CurrentMaterial[2], 1) # Roof Corner 1
        mc.setBlocks(self.x + 28, self.y + 7, self.z + 18, self.x + 28, self.y + 7, self.z + 28, CurrentMaterial[2], 1) # Roof 5
        mc.setBlocks(self.x + 18, self.y + 7, self.z + 29, self.x + 27, self.y + 7, self.z + 29, CurrentMaterial[2], 3) # Roof 6
        mc.setBlocks(self.x + 28, self.y + 7, self.z + 29, self.x + 28, self.y + 7, self.z + 29, CurrentMaterial[2], 1) # Roof Corner 2

        # Upper roof
        mc.setBlocks(self.x + 18, self.y + 8, self.z + 23, self.x + 18, self.y + 8, self.z + 28, CurrentMaterial[2]) # Roof 1
        mc.setBlocks(self.x + 23, self.y + 8, self.z + 18, self.x + 23, self.y + 8, self.z + 23, CurrentMaterial[2]) # Roof 2
        mc.setBlocks(self.x + 19, self.y + 8, self.z + 23, self.x + 22, self.y + 8, self.z + 23, CurrentMaterial[2], 2) # Roof 3
        mc.setBlocks(self.x + 24, self.y + 8, self.z + 18, self.x + 26, self.y + 8, self.z + 18, CurrentMaterial[2], 2) # Roof 4
        mc.setBlocks(self.x + 27, self.y + 8, self.z + 18, self.x + 27, self.y + 8, self.z + 28, CurrentMaterial[2], 1) # Roof 5
        mc.setBlocks(self.x + 19, self.y + 8, self.z + 28, self.x + 26, self.y + 8, self.z + 28, CurrentMaterial[2], 3) # Roof 6

        mc.setBlocks(self.x + 19, self.y + 8, self.z + 24, self.x + 26, self.y + 8, self.z + 27, CurrentMaterial[0]) # Roof Apeself.x 1
        mc.setBlocks(self.x + 24, self.y + 8, self.z + 19, self.x + 26, self.y + 8, self.z + 27, CurrentMaterial[0]) # Roof Apeself.x 2


        mc.setBlocks(self.x + 23, self.y + 1, self.z + 19, self.x + 23, self.y + 1, self.z + 22, block.GLASS) # Small Window 1
        mc.setBlocks(self.x + 18, self.y + 5, self.z + 24, self.x + 18, self.y + 5, self.z + 27, block.GLASS) # Small Window 2
        mc.setBlocks(self.x + 18, self.y + 1, self.z + 24, self.x + 18, self.y + 1, self.z + 27, block.GLASS) # Small Window 3
        mc.setBlocks(self.x + 24, self.y + 1, self.z + 18, self.x + 26, self.y + 1, self.z + 18, block.GLASS) # Small Window 4
        mc.setBlocks(self.x + 24, self.y + 5, self.z + 18, self.x + 26, self.y + 5, self.z + 18, block.GLASS) # Small Window 5    

        mc.setBlock(self.x + 20, self.y + 1, self.z + 23, 64, 9) # Door 1 Top Half
        mc.setBlock(self.x + 20, self.y, self.z + 23, 64, 1) # Door 1 Bottom Half
        self.doorx = self.x + 22
        self.doorz = self.z + 17
        mc.setBlock(self.x + 21, self.y + 1, self.z + 23, 64, 9) # Door 2 Top Half
        mc.setBlock(self.x + 21, self.y, self.z + 23, 64, 6) # Door 2 Bottom Half

        mc.setBlock(self.x + 22, self.y + 1, self.z + 22, 50, 4) # Outside torch left
        mc.setBlock(self.x + 19, self.y + 1, self.z + 22, 50, 4) # Outside torch right

        mc.setBlocks(self.x + 19, self.y - 1, self.z + 18, self.x + 22, self.y - 1, self.z + 23, block.WOOD_PLANKS) # Walk Waself.y

        mc.setBlocks(self.x + 28, self.y, self.z + 18, self.x + 38, self.y + 1, self.z + 28, random.choice([block.FENCE, block.FENCE_ACACIA, block.FENCE_BIRCH, block.FENCE_DARK_OAK, block.FENCE_JUNGLE, block.FENCE_SPRUCE])) # Pool Fence
        mc.setBlocks(self.x + 28, self.y, self.z + 19, self.x + 37, self.y + 1, self.z + 27, block.AIR) # Fence Air
        mc.setBlocks(self.x + 33, self.y - 1, self.z + 19, self.x + 37, self.y - 4, self.z + 24, block.STONE_BRICK) # Pool Base
        mc.setBlocks(self.x + 34, self.y - 1, self.z + 20, self.x + 36, self.y - 2, self.z + 23, block.WATER) # Pool Tub
        mc.setBlocks(self.x + 34, self.y - 3, self.z + 20, self.x + 36, self.y - 3, self.z + 23, 169) # Pool Light

        mc.setBlock(self.x + 27, self.y - 1, self.z + 24, block.WOOD_PLANKS) # Door Base
        mc.setBlock(self.x + 27, self.y + 1, self.z + 24, 64, 9) # Back self.yard Door Top Half
        mc.setBlock(self.x + 27, self.y, self.z + 24, 64, 0) # Back self.yard Door Bottom Half

    def House2(self):
        Materials = [[block.WOOD_PLANKS, 17, 53], [block.BRICK_BLOCK, block.STONE_BRICK, 109], [block.STONE_BRICK, block.STONE_BRICK, 109]]
        CurrentMaterial = random.choice(Materials)

        mc.setBlocks(self.x + 15, self.y - 1 , self.z + 15, self.x + 41, self.y - 3, self.z + 31, block.GRASS) # Grass
        mc.setBlocks(self.x + 15 - 1 - random.randint(0, 2), self.y - 2, self.z + 15 - 1 - random.randint(0, 2), self.x + 41 + 1 + random.randint(0, 2), self.y - 2, self.z + 31 + 1 + random.randint(0, 2), block.GRASS) # Grass

        # for i in range(1, 10):
        #     mc.setBlocks(self.x + 15 - i - random.randint(0, 2), self.y - i, self.z + 15 - i - random.randint(0, 2), self.x + 41 + i + random.randint(0, 2), self.y - 10, self.z + 31 + i + random.randint(0, 2), block.GRASS) # Grass

        mc.setBlocks(self.x + 15, self.y, self.z + 15, self.x + 41, self.y + 20, self.z + 31, block.AIR) # Air Space

        mc.setBlocks(self.x + 18, self.y - 1, self.z + 18, self.x + 27, self.y + 7, self.z + 28, CurrentMaterial[0]) # Walls 1

        mc.setBlocks(self.x + 19, self.y, self.z + 19, self.x + 26, self.y + 6, self.z + 27, block.AIR) # Air

        mc.setBlocks(self.x + 19, self.y - 1 , self.z + 19, self.x + 26, self.y - 1, self.z + 27, block.WOOD_PLANKS) # Wood Base 1
    

        mc.setBlocks(self.x + 18, self.y + 3, self.z + 18, self.x + 27, self.y + 3, self.z + 28, block.WOOD_PLANKS) # Upstairs base 

        mc.setBlocks(self.x + 21, self.y + 3, self.z + 26, self.x + 24, self.y + 3, self.z + 28, block.AIR) # Stairs Hole 1
        mc.setBlocks(self.x + 20, self.y + 4, self.z + 25, self.x + 24, self.y + 4, self.z + 27, block.FENCE) # Stairs Fence
        mc.setBlocks(self.x + 21, self.y + 4, self.z + 26, self.x + 24, self.y + 4, self.z + 27, block.AIR) # Stairs Hole 2
        mc.setBlocks(self.x + 19, self.y + 4, self.z + 25, self.x + 19, self.y + 4, self.z + 25, block.FENCE) # Stairs Corner
        mc.setBlocks(self.x + 19, self.y + 4, self.z + 25, self.x + 19, self.y + 4, self.z + 25, block.AIR) # Stairs Corner Air

        mc.setBlock(self.x + 26, self.y, self.z + 19, 61, 3) # furnace 

        if random.randint(0, 1) == 1:
            mc.setBlock(self.x + 25, self.y, self.z + 19, 62, 3) # furnace 

        else:
            mc.setBlock(self.x + 25, self.y, self.z + 19, 118) # cauldron

        mc.setBlock(self.x + 24, self.y, self.z + 19, block.CRAFTING_TABLE) # crafting table

        mc.setBlock(self.x + 26, self.y, self.z + 27, 54) # chest
        mc.setBlock(self.x + 25, self.y, self.z + 27, 54) # chest

        mc.setBlocks(self.x + 23, self.y, self.z + 22, self.x + 23, self.y, self.z + 23, block.FENCE_SPRUCE) # Table legs 1
        mc.setBlocks(self.x + 23, self.y, self.z + 21, self.x + 23, self.y, self.z + 21, block.FENCE_SPRUCE) # Table legs 1 Fix
        mc.setBlocks(self.x + 23, self.y, self.z + 21, self.x + 23, self.y, self.z + 21, block.AIR) # Table legs 1 Fix 2
        mc.setBlocks(self.x + 21, self.y, self.z + 22, self.x + 21, self.y, self.z + 23, block.FENCE_SPRUCE) # Table legs 2
        mc.setBlocks(self.x + 21, self.y, self.z + 21, self.x + 21, self.y, self.z + 21, block.FENCE_SPRUCE) # Table legs 2 Fix
        mc.setBlocks(self.x + 21, self.y, self.z + 21, self.x + 21, self.y, self.z + 21, block.AIR) # Table legs 2 Fix 2
        mc.setBlocks(self.x + 22, self.y, self.z + 22, self.x + 22, self.y, self.z + 23, 166) # Table Gap
        mc.setBlocks(self.x + 21, self.y + 1, self.z + 22, self.x + 23, self.y + 1, self.z + 23, 72, 3) # Table Top

        mc.setBlock(self.x + 22, self.y, self.z + 21, 53, 3) # Seat 1
        mc.setBlock(self.x + 22, self.y, self.z + 24, 53, 2) # Seat 2

        for i in range(4):
            mc.setBlocks(self.x + 21 + i, self.y + i, self.z + 26, self.x + 21 + i, self.y + i, self.z + 27, 53) # Stairs

        mc.setBlocks(self.x + 18, self.y - 1, self.z + 18, self.x + 18, self.y + 6, self.z + 18, CurrentMaterial[1]) # Corners 1
        mc.setBlocks(self.x + 18, self.y - 1, self.z + 28, self.x + 18, self.y + 6, self.z + 28, CurrentMaterial[1]) # Corners 2
        mc.setBlocks(self.x + 27, self.y - 1, self.z + 18, self.x + 27, self.y + 6, self.z + 18, CurrentMaterial[1]) # Corners 4
        mc.setBlocks(self.x + 27, self.y - 1, self.z + 28, self.x + 27, self.y + 6, self.z + 28, CurrentMaterial[1]) # Corners 5

        mc.setBlocks(self.x + 18, self.y + 3, self.z + 19, self.x + 18, self.y + 3, self.z + 27, CurrentMaterial[1], 8) # Side Support 1
        mc.setBlocks(self.x + 19, self.y + 3, self.z + 28, self.x + 26, self.y + 3, self.z + 28, CurrentMaterial[1], 4) # Side Support 3
        mc.setBlocks(self.x + 19, self.y + 3, self.z + 18, self.x + 26, self.y + 3, self.z + 18, CurrentMaterial[1], 4) # Side Support 4
        mc.setBlocks(self.x + 27, self.y + 3, self.z + 19, self.x + 27, self.y + 3, self.z + 27, CurrentMaterial[1], 8) # Side Support 6

        mc.setBlocks(self.x + 20, self.y + 8, self.z + 20, self.x + 25, self.y + 7, self.z + 26, block.GLOWSTONE_BLOCK) # Upstairs Glow Stone

        if random.randint(0, 1) == 1:
            mc.setBlocks(self.x + 19, self.y + 4, self.z + 22, self.x + 26, self.y + 7, self.z + 22, block.WOOD_PLANKS) # Upstairs Room Wall
            mc.setBlocks(self.x + 23, self.y + 4, self.z + 19, self.x + 23, self.y + 7, self.z + 22, block.WOOD_PLANKS) # Upstairs Room Wall Divider
            
            mc.setBlock(self.x + 26, self.y + 4, self.z + 19, 26, 10) # room bed 1 top half
            mc.setBlock(self.x + 26, self.y + 4, self.z + 20, 26, 2) # room bed 1 bottom half

            mc.setBlock(self.x + 19, self.y + 4, self.z + 19, 26, 10) # room bed 2 top half
            mc.setBlock(self.x + 19, self.y + 4, self.z + 20, 26, 2) # room bed 2 bottom half


            mc.setBlock(self.x + 25, self.y + 5, self.z + 22, 64, 9) # room 1 door top half
            mc.setBlock(self.x + 25, self.y + 4, self.z + 22, 64, 3) # room 1 door bottom half

            mc.setBlock(self.x + 21, self.y + 5, self.z + 22, 64, 9) # room 2 door top half
            mc.setBlock(self.x + 21, self.y + 4, self.z + 22, 64, 3) # room 2 door bottom half

        else:
            mc.setBlock(self.x + 25, self.y + 4, self.z + 19, 26, 10) # bed 1 top half
            mc.setBlock(self.x + 25, self.y + 4, self.z + 20, 26, 2) # bed 1 bottom half

            mc.setBlock(self.x + 26, self.y + 4, self.z + 19, 26, 10) # bed 2 top half
            mc.setBlock(self.x + 26, self.y + 4, self.z + 20, 26, 2) # bed 2 bottom half

            mc.setBlocks(self.x + 23, self.y + 4, self.z + 19, self.x + 19, self.y + 4, self.z + 19, block.BOOKSHELF) # Bookshelves


        mc.setBlock(self.x + 25, self.y + 1, self.z + 27, 50, 4) # Down Stairs torch 1
        mc.setBlock(self.x + 25, self.y + 2, self.z + 19, 50, 3) # Down Stairs torch 2
        mc.setBlock(self.x + 19, self.y + 2, self.z + 26, 50, 0) # Down stairs torch 3

        mc.setBlocks(self.x + 17, self.y + 7, self.z + 18, self.x + 17, self.y + 7, self.z + 29, CurrentMaterial[2]) # Roof 1
        mc.setBlocks(self.x + 17, self.y + 7, self.z + 17, self.x + 28, self.y + 7, self.z + 17, CurrentMaterial[2], 2) # Roof 4
        mc.setBlocks(self.x + 28, self.y + 7, self.z + 18, self.x + 28, self.y + 7, self.z + 29, CurrentMaterial[2], 1) # Roof 5
        mc.setBlocks(self.x + 18, self.y + 7, self.z + 29, self.x + 27, self.y + 7, self.z + 29, CurrentMaterial[2], 3) # Roof 6


        # Upper roof
        mc.setBlocks(self.x + 18, self.y + 8, self.z + 19, self.x + 18, self.y + 8, self.z + 28, CurrentMaterial[2]) # Roof 1
        mc.setBlocks(self.x + 18, self.y + 8, self.z + 18, self.x + 26, self.y + 8, self.z + 18, CurrentMaterial[2], 2) # Roof 4
        mc.setBlocks(self.x + 27, self.y + 8, self.z + 18, self.x + 27, self.y + 8, self.z + 28, CurrentMaterial[2], 1) # Roof 5
        mc.setBlocks(self.x + 19, self.y + 8, self.z + 28, self.x + 26, self.y + 8, self.z + 28, CurrentMaterial[2], 3) # Roof 6

        mc.setBlocks(self.x + 19, self.y + 8, self.z + 19, self.x + 26, self.y + 8, self.z + 27, CurrentMaterial[0]) # Roof Apeself.x 
    

        mc.setBlocks(self.x + 18, self.y + 5, self.z + 19, self.x + 18, self.y + 5, self.z + 27, block.GLASS) # Upper Window 1
        mc.setBlocks(self.x + 18, self.y + 1, self.z + 19, self.x + 18, self.y + 1, self.z + 27, block.GLASS) # Lower Window 1
        mc.setBlocks(self.x + 23, self.y + 1, self.z + 18, self.x + 26, self.y + 1, self.z + 18, block.GLASS) # Lower Window 2
        mc.setBlocks(self.x + 19, self.y + 5, self.z + 18, self.x + 26, self.y + 5, self.z + 18, block.GLASS) # Upper Window 2  

        mc.setBlock(self.x + 20, self.y + 1, self.z + 18, 64, 9) # Door 1 Top Half
        mc.setBlock(self.x + 20, self.y, self.z + 18, 64, 1) # Door 1 Bottom Half
        self.doorx = self.x + 22
        self.doorz = self.z + 16
        mc.setBlock(self.x + 21, self.y + 1, self.z + 18, 64, 9) # Door 2 Top Half
        mc.setBlock(self.x + 21, self.y, self.z + 18, 64, 6) # Door 2 Bottom Half

        mc.setBlocks(self.x + 19, self.y - 1, self.z + 17, self.x + 21, self.y - 1, self.z + 17, block.STONE_BRICK) # Stone patio 
        mc.setBlocks(self.x + 20, self.y - 1, self.z + 18, self.x + 21, self.y - 1, self.z + 18, block.WOOD_PLANKS) # Door Base

        mc.setBlock(self.x + 22, self.y + 1, self.z + 17, 50, 4) # Outside torch left
        mc.setBlock(self.x + 19, self.y + 1, self.z + 17, 50, 4) # Outside torch right
        mc.setBlock(self.x + 22, self.y + 1, self.z + 19, 50, 3) # Inside door torch 1
        mc.setBlock(self.x + 19, self.y + 1, self.z + 19, 50, 3) # Inside door torch 2


        mc.setBlocks(self.x + 28, self.y, self.z + 18, self.x + 38, self.y + 1, self.z + 28, random.choice([block.FENCE, block.FENCE_ACACIA, block.FENCE_BIRCH, block.FENCE_DARK_OAK, block.FENCE_JUNGLE, block.FENCE_SPRUCE])) # Pool Fence
        mc.setBlocks(self.x + 28, self.y, self.z + 19, self.x + 37, self.y + 1, self.z + 27, block.AIR) # Fence Air
        mc.setBlocks(self.x + 33, self.y - 1, self.z + 19, self.x + 37, self.y - 4, self.z + 24, block.STONE_BRICK) # Pool Base
        mc.setBlocks(self.x + 34, self.y - 1, self.z + 20, self.x + 36, self.y - 2, self.z + 23, block.WATER) # Pool Tub
        mc.setBlocks(self.x + 34, self.y - 3, self.z + 20, self.x + 36, self.y - 3, self.z + 23, 169) # Pool Light

        mc.setBlock(self.x + 27, self.y - 1, self.z + 24, block.WOOD_PLANKS) # Door Base
        mc.setBlock(self.x + 27, self.y + 1, self.z + 24, 64, 9) # Back self.yard Door Top Half
        mc.setBlock(self.x + 27, self.y, self.z + 24, 64, 0) # Back self.yard Door Bottom Half

    def generateHouse(self):
        
        if random.randint(0, 1):
            self.House1()
        else:
            self.House2()

    def getDoorPos(self):
        # print(self.doorx, self.doorz)
        return [self.doorx, self.doorz, self.y]


#p = mc.player.getTilePos()
#HenryHouse(p.x, p.y, p.z).generateHouse()  

# HenryHouse(p.x, p.y, p.z).House2()


