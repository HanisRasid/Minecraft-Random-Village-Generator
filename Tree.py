from mcpi import minecraft
from mcpi import block
from random import randint
from random import choice

mc = minecraft.Minecraft.create()

p = mc.player.getTilePos()

class Tree:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.height = mc.getHeight(self.x, self.z)

        self.wood  = block.WOOD.id
        self.leaves = block.LEAVES.id

        self.tree_type = randint(0, 3)

        self.tree_height = randint(2, 4)
    
    def setTree(self):
        mc.setBlocks(self.x - 1, self.height + self.tree_height + 4, self.z - 1, self.x + 1, self.height + self.tree_height + 4, self.z + 1, self.leaves, self.tree_type)
        mc.setBlocks(self.x - 2, self.height + self.tree_height + 1, self.z - 2, self.x + 2, self.height + self.tree_height + 3, self.z + 2, self.leaves, self.tree_type)
        mc.setBlocks(self.x - 1, self.height + self.tree_height, self.z - 1, self.x + 1, self.height + self.tree_height, self.z + 1, self.leaves, self.tree_type)

        #  removes random parts of leaves to make trees look more natural and random 
        removed_leaves = randint(10, 20)
        for i in range(removed_leaves): 
            removed_width = randint(-2, 2)
            removed_height = randint(1, 3)
            if removed_width == -2 or removed_width == 2:
                mc.setBlock(self.x + removed_width, self.height + self.tree_height + removed_height, self.z + randint(-2, 2), block.AIR)
            else:
                mc.setBlock(self.x + removed_width, self.height + self.tree_height + removed_height, self.z + choice([-2, 2]), block.AIR)

        mc.setBlocks(self.x, self.height + 1, self.z, self.x, self.height + self.tree_height + randint(2,3), self.z, self.wood, self.tree_type)

    def Forest(self):
        # In a range of 25 the area where the tree will spawn is checked to see if there any blocks other than nature objects and dirt that the tree might obstruct. If there are none then the tree will be set
        for i in range(25):
            Invalid = False 
            randX = randint(-50, 50)
            randZ = randint(-50, 50)

            self.x = p.x + randX
            self.z = p.z + randZ

            self.height = mc.getHeight(self.x, self.z) 
            

            if mc.getBlock(self.x, self.height, self.z) == 2 and len([i for i in mc.getBlocks(self.x - 2, self.height + 1, self.z - 2, self.x + 2, self.height + 10, self.z + 2) if i not in [0, 2, 31, 37, 38]]) == 0:

                self.setTree()