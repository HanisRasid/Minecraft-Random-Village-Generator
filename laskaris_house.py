from random import randint
from random import choice 
from random import randrange
from mcpi import block
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

class LaskarisHouse:
    def __init__(self, x, y, z):
        # self.x, self.y, self.z = mc.player.getTilePos() # probably will need to move this somewhere else, 
                                                        # so it is more accessible for entire program
        
        self.length = randrange(14, 20, 2)
        self.width = randrange(12, 20, 2)

        self.x = x - self.width / 2
        self.y = y
        self.z = z + self.length / 2

        self.height = y - 1 + randint(0, 2)

        self.single_story = 4
        self.double_story = 8

        self.stories = choice([self.single_story, self.double_story])

    def createFoundation(self):
        door = 64
        door_type = 12

        # Grass Foundation
        #mc.setBlocks(self.x - 4, self.height, self.z - 28, self.x + 16, self.height, self.z + 2, block.GRASS)
        mc.setBlocks(self.x - 2, self.height, self.z + 2, self.x + self.width + 2, self.height, self.z - self.length - 11, block.GRASS)
        mc.setBlocks(self.x - 3 - randint(0, 2), self.height - 1, self.z + 3 + randint(0, 2), self.x + self.width + 3 + randint(0, 2), self.height - 5, self.z - self.length - 12 - randint(0, 2), block.GRASS)


        # clear area and foundation
        mc.setBlocks(self.x, self.height + 1, self.z, self.x + self.width, self.height + 1 + self.stories * 2, self.z - self.length - 9, block.AIR)
        mc.setBlocks(self.x, self.height, self.z, self.x + self.width, self.height, self.z - self.length - 2, block.STONE_BRICK)

        # base walls, corners and doors
        if self.stories == self.single_story:
            wood = 17
            wood_type = 1

            mc.setBlocks(self.x, self.height + 1, self.z, self.x + self.width, self.height + 1 + self.stories, self.z - self.length, block.WOOD_PLANKS)

            mc.setBlocks(self.x, self.height + 1, self.z, self.x, self.height + 1 + self.stories, self.z, wood, wood_type)
            mc.setBlocks(self.x, self.height + 1, self.z - self.length, self.x, self.height + 1 + self.stories, self.z - self.length, wood, wood_type)
            mc.setBlocks(self.x + self.width, self.height + 1, self.z, self.x + self.width, self.height + 1 + self.stories, self.z, wood, wood_type)
            mc.setBlocks(self.x + self.width, self.height + 1, self.z - self.length, self.x + self.width, self.height + 1 + self.stories, self.z - self.length, wood, wood_type)

            
            mc.setBlock(self.x + 3, self.height + 2, self.z - self.length, door, door_type)

            door_type = 6
            mc.setBlock(self.x + 3, self.height + 1, self.z - self.length, door, door_type)
        else: 
            mc.setBlocks(self.x, self.height + 1, self.z, self.x + (self.width / 2), self.height + self.single_story + 1, self.z - (self.length / 2), block.WOOD_PLANKS)
            mc.setBlocks(self.x + (self.width / 2), self.height + 1, self.z , self.x + self.width, self.height + self.single_story + 1, self.z - self.length, block.WOOD_PLANKS) 

            mc.setBlock(self.x + 3, self.height + 2, self.z - self.length / 2, door, door_type)
            
            door_type = 6
            mc.setBlock(self.x + 3, self.height + 1, self.z - self.length / 2, door, door_type)
        
        
        door_type = 12
        mc.setBlock(self.x + 3, self.height + 2, self.z, door, door_type)
        mc.setBlock(self.x + 4, self.height + 2, self.z, door, door_type)
        

        door_type = 4
        mc.setBlock(self.x + 3, self.height + 1, self.z, door, door_type)


        door_type = 3
        mc.setBlock(self.x + 4, self.height + 1, self.z, door, door_type)

    def createRoof(self):        
        if self.stories == self.single_story:
            pass
            stair  = 109

            right = 1
            left = 0
            back = 2
            front = 3

            edge_x = self.x + (self.width + 1) 
            edge_z = self.z - (self.length + 1)

            slab = 44
            slab_type = 13

            
            for i in range(3):
                mc.setBlocks(edge_x - i, self.height + 1 + (self.stories + 1) + i, self.z + 1 - i, edge_x - i, self.height + 1 + (self.stories + 1) + i, edge_z + i, stair, right)
                mc.setBlocks(self.x - 1 + i, self.height + 1 + (self.stories + 1) + i, self.z - i, self.x - 1 + i, self.height + 1 + (self.stories + 1) + i, edge_z + i, stair, left)

                mc.setBlocks(self.x - 1 + i, self.height + 1 + self.stories + 1 + i, self.z + 1 - i, self.x + self.width - i, self.height + 1 + self.stories + 1 + i, self.z + 1 - i, stair, front)
                mc.setBlocks(self.x + i, self.height + 1 + self.stories + 1 + i, self.z - self.length - 1 + i, self.x + self.width - i, self.height + 1 + self.stories + 1 + i, self.z - self.length - 1 + i, stair, back)

            mc.setBlocks(self.x + 2, self.height + 1 + self.stories + 3, self.z - 2, self.x + self.width - 2, self.height + 1 + self.stories + 3, self.z - self.length + 2, slab, slab_type)
        else:
            wood = 17
            wood_type = 1

            mc.setBlocks(self.x, self.height + 1 + self.single_story, self.z, self.x + self.width, self.height + 1+ self.single_story, self.z - (self.length / 2), wood, wood_type)
            mc.setBlocks(self.x + (self.width / 2), self.height + 1 + self.single_story, self.z, self.x + self.width, self.height + 1 + self.single_story, self.z - self.length, wood, wood_type)


    def clearInside(self):
        if self.stories == self.single_story:
            mc.setBlocks(self.x + 1, self.height + 1, self.z - 1, self.x + (self.width / 2 - 1), self.height + 1 + self.stories - 1, self.z - (self.length / 2) + 1, block.AIR)
            mc.setBlocks(self.x + 1, self.height + 1, self.z - (self.length / 2) - 1, self.x + (self.width / 2 - 1), self.height + 1 + self.stories - 1, self.z - self.length + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + 1, self.height + 1, self.z - 1, self.x + self.width - 1, self.height + 1 + self.stories - 1, self.z - (self.length / 2) + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + 1, self.height + 1, self.z - (self.length / 2) - 1, self.x + self.width - 1, self.height + 1 + self.stories - 1,  self.z - self.length + 1, block.AIR)

            mc.setBlocks(self.x + (self.width / 2) / 2, self.height + 1, self.z - self.length/2, self.x + ((self.width / 2) / 2) + 1, self.height + 3, self.z - self.length/2, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + ((self.width / 2) / 2), self.height + 1, self.z - self.length/2, self.x + (self.width / 2) + ((self.width / 2) / 2) + 1, self.height + 3, self.z - self.length/2, block.AIR)
            mc.setBlocks(self.x + (self.width / 2), self.height + 1, self.z - (self.length / 2) / 2, self.x + ((self.width / 2) / 2) + 1, self.height + 3, self.z - ((self.length / 2) / 2) + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2), self.height + 1, self.z - (self.length / 2) - ((self.length / 2) / 2), self.x + (self.width / 2) + ((self.width / 2) / 2) + 1, self.height + 3, self.z - (self.length / 2) - ((self.length / 2) / 2) + 1, block.AIR)
        else:
            mc.setBlocks(self.x + 1, self.height + 1, self.z - 1, self.x + self.width / 2 - 1, self.height + self.single_story, self.z - (self.length / 2) + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + 1, self.height + 1, self.z - 1, self.x + self.width - 1, self.height + 1 + self.stories - 1, self.z - (self.length / 2) + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + 1, self.height + 1, self.z - (self.length / 2) - 1, self.x + self.width - 1, self.height + 1 + self.stories - 1,  self.z - self.length + 1, block.AIR)

            mc.setBlocks(self.x + (self.width / 2), self.height + 1, self.z - (self.length / 2) / 2, self.x + ((self.width / 2) / 2) + 1, self.height + 3, self.z - ((self.length / 2) / 2) + 1, block.AIR)
            mc.setBlocks(self.x + (self.width / 2) + ((self.width / 2) / 2), self.height + 1, self.z - self.length/2, self.x + (self.width / 2) + ((self.width / 2) / 2) + 1, self.height + 3, self.z - self.length/2, block.AIR)
            

    def createRoom(self, room_num, room_type):
        x = self.x
        z = self.z
        
        length = self.length // 2
        width = self.width // 2

        x_mod = 1

        chest_orient = 5

        # changes orientation of objects depending on which room they are placed in
        if room_num == 2:
            x = self.x + self.width
            width = -width 
            x_mod = -1
            chest_orient = 4
        elif room_num == 3:
            x = self.x + self.width
            width = -width
            if self.length % 2 == 0:
                z = self.z - length
            x_mod = -1
            chest_orient = 4
        elif room_num == 4:
            z = self.z - length

        # places objects in room 
        if room_type == 1:
            bed = 26
            bottom = 2
            top = 10
            orient = 4
            mc.setBlock(x + x_mod, self.height + 1, z - length / 2 - 1, bed, top)
            mc.setBlock(x + x_mod, self.height + 1, z - length / 2, bed, bottom)

            mc.setBlock(x + x_mod, self.height + 1, z - 1, block.CRAFTING_TABLE)
            mc.setBlock(x + x_mod, self.height + 1, z - 2, block.CHEST.id, chest_orient)

            orient = 3
            mc.setBlock(x + width - x_mod, self.height + 1, z - length + 1, block.FURNACE_ACTIVE.id, orient)

            mc.setBlocks(x, self.height + 2, z - 2, x, self.height + 3, z - length + 2, block.GLASS)

        elif room_type == 2:
            orient = 3

            mc.setBlock(x + x_mod, self. height + 3, z - length + 1, block.TORCH.id, orient)

            mc.setBlock(x + width - x_mod, self. height + 3, z - length + 1, block.TORCH.id, orient)

        elif room_type == 3:
            i = 1
            while mc.getBlock(x + x_mod, self.height + 1, z - i) != block.WOOD_PLANKS.id:
                num = randint(1,3)
                mc.setBlocks(x + x_mod, self.height + 1, z - i, x + x_mod, self.height + 1 + num, z - i, block.BOOKSHELF)
                i += 1

            orient = 4
            mc.setBlock(x + width - x_mod, self. height + 3, z - 1, block.TORCH.id, orient)

        elif room_type == 4:
            stair = 114
            direction = 2
            mc.setBlock(x + x_mod, self.height + 1, z - 1, stair, direction)

            direction = 3
            mc. setBlock(x + x_mod, self.height + 1, z - length + 1, stair, direction)

            stair = 156
            direction = 7
            mc.setBlock(x + x_mod, self.height + 1, z - 2, stair, direction)

            direction = 6
            mc.setBlock(x + x_mod, self.height + 1, z - length + 2, stair, direction)

            if mc.getBlock(x + x_mod, self.height + 1, z - 3) != stair:
                slab = 44
                slab_type = 15
                mc.setBlocks(x + x_mod, self.height + 1, z - 3, x + x_mod, self.height + 1, z - length + 3, slab, slab_type)

            mc.setBlocks(x, self.height + 2, z - 2, x, self.height + 3, z - length + 2, block.GLASS)

    def createSecondStory(self):
        # randomly chooses orientaion of second story and placement of balcony
        num = randint(1,2)

        stair  = 109
        door = 64
        door_type = 12

        mid = self.width // 4
        x = self.x + self.width / 2
        width = self.width // 2
        length = self.length 
        stair_orient_1 = 0
        stair_orient_2 = 1
        stair_orient_3 = 2

        if num == 2:
            x = self.x
            width = self.width
            length = self.length / 2

            stair_orient_1 = 3
            stair_orient_2 = 2

            stair_orient_3 = 0

            mid = self.length // 4

        mc.setBlocks(x, self.height + self.single_story + 2, self.z, x + width, self.height + self.double_story + 1, self.z - length, block.WOOD_PLANKS)

        # clear inside
        mc.setBlocks(x + 1, self.height + self.single_story + 2, self.z - 1, x + width - 1, self.height + self.double_story + 1, self.z - length + 1, block.AIR)

        # stairs
        for i in range(self.single_story + 1):
            if num == 1:
                mc.setBlock(x + 1, self.height + 1 + i, self.z - length + 3 + i, stair, stair_orient_3)
                mc.setBlock(x + 1, self.height + self.single_story + 1, self.z - length + 2 + i, block.AIR)
                
            else:
                mc.setBlock(x + width / 2 + 1 + i, self.height + 1 + i, self.z - 1, stair, stair_orient_3)
                mc.setBlock(x + width / 2 + i, self.height + self.single_story + 1, self.z - 1, block.AIR)

        # roof for second floor
        wood = 17
        wood_type = 1
        for i in range(mid):
            if num == 1:
                mc.setBlocks(x + 1 + i, self.height + self.stories + 2 + i, self.z, x + width - 1 - i, self.height + self.stories + 2 + i, self.z - length, wood, wood_type)
            else:
                mc.setBlocks(x, self.height + self.stories + 2 + i, self.z - 1 - i, x + width, self.height + self.stories + 2 + i, self.z - length + 1 + i, wood, wood_type)

        # stairs
        for i in range(mid + 1):
            if num == 1:
                mc.setBlocks(x + width - i, self.height + self.stories + 2 + i, self.z + 1, x + width - i, self.height + self.stories + 2 + i, self.z - length - 1, stair, stair_orient_2)
                mc.setBlocks(x  + i, self.height + self.stories + 2 + i, self.z + 1, x + i, self.height + self.stories + 2 + i, self.z - length - 1, stair, stair_orient_1)
            else:
                mc.setBlocks(x - 1, self.height + self.stories + 2 + i, self.z - length + i, x + width + 1, self.height + self.stories + 2 + i, self.z - length + i, stair, stair_orient_2)
                mc.setBlocks(x - 1, self.height + self.stories + 2 + i, self.z - i, x + width + 1 , self.height + self.stories + 2 + i, self.z - i, stair, stair_orient_1)

        # doors and decoration
        if num == 1:
            mc.setBlock(x, self.height + self.single_story + 3, self.z - length / 4, door, door_type)
            mc.setBlock(x, self.height + self.single_story + 3, self.z - length / 4 + 1, door, door_type)
            
            door_type = 5
            mc.setBlock(x , self.height + self.single_story + 2, self.z - length / 4, door, door_type)
        
            door_type = 0
            mc.setBlock(x, self.height + self.single_story + 2, self.z - length / 4 + 1, door, door_type)

            # windows
            for i in range(3, length + 1, 4):
                mc.setBlocks(self.x + self.width, self.height + self.single_story +  3, self.z  - i, self.x + self.width, self.height + self.single_story + 4, self.z - i, block.GLASS)

            
            mc.setBlocks(x, self.height + self.single_story +  3, self.z  - length + 2, x, self.height + self.single_story +  4, self.z - length / 2 - 1, block.GLASS)
            mc.setBlocks(x +  2, self.height + self.single_story +  3, self.z, x + width - 2, self.height + self.single_story +  4, self.z, block.GLASS)  
            mc.setBlocks(x +  2, self.height + self.single_story +  3, self.z - length, x + width - 2, self.height + self.single_story +  4, self.z - length, block.GLASS)

            mc.setBlocks(x + 2, self.height + self.single_story + 2, self.z - 1, x + width - 2, self.height + self.single_story + 2, self.z - 1, stair, stair_orient_3)
            mc.setBlocks(x + 2, self.height + self.single_story + 2, self.z - 2, x + 2,  self.height + self.single_story + 2, self.z - 3, stair, 4)
            mc.setBlocks(x + width - 2, self.height + self.single_story + 2, self.z - 2, x + width - 2, self.height + self.single_story + 2, self.z - 3, stair, 5)

            # table
            if mc.getBlock(x + 3, self.height + self.single_story + 2, self.z - 2) != stair:
                slab = 44
                slab_type = 13
                mc.setBlocks(x + 3, self.height + self.single_story + 2, self.z - 2, x + width - 3, self.height + self.single_story + 2, self.z - 3, slab, slab_type) 
        else:
            mc.setBlock(x + width - width / 4, self.height + self.single_story + 3, self.z - length , door, door_type)
            mc.setBlock(x + width - width / 4 + 1, self.height + self.single_story + 3, self.z - length , door, door_type)
            
            door_type = 1
            mc.setBlock(x + width - width / 4, self.height + self.single_story + 2, self.z - length, door, door_type)
        
            door_type = 6
            mc.setBlock(x + width - width / 4 + 1, self.height + self.single_story + 2, self.z - length, door, door_type)

            # windows
            for i in range(3, width + 1, 4):
                mc.setBlocks(self.x + i, self.height + self.single_story +  3, self.z, self.x + i, self.height + self.single_story + 4, self.z, block.GLASS)

            
            mc.setBlocks(x, self.height + self.single_story +  3, self.z  - 2, x, self.height + self.single_story +  4, self.z - length + 2, block.GLASS)
            mc.setBlocks(x + width, self.height + self.single_story +  3, self.z - 2, x + width, self.height + self.single_story +  4, self.z - length + 2, block.GLASS)  
            mc.setBlocks(x +  2, self.height + self.single_story +  3, self.z - length, x + width / 2, self.height + self.single_story +  4, self.z - length, block.GLASS)

            mc.setBlocks(x + 1, self.height + self.single_story + 2, self.z - 2, x + 1, self.height + self.single_story + 2, self.z - length + 2, stair, 1)
            mc.setBlocks(x + 2, self.height + self.single_story + 2, self.z - 2, x + 3,  self.height + self.single_story + 2, self.z - 2, stair, 7)
            mc.setBlocks(x + 2, self.height + self.single_story + 2, self.z - length + 2, x + 3, self.height + self.single_story + 2, self.z - length + 2, stair, 6)

            # table
            if mc.getBlock(x + 2, self.height + self.single_story + 2, self.z - 3) != stair:
                slab = 44
                slab_type = 13
                mc.setBlocks(x + 2, self.height + self.single_story + 2, self.z - 3, x + 3, self.height + self.single_story + 2, self.z - length + 3, slab, slab_type)  

        # balcony
        if num == 1:
            mc.setBlocks(self.x, self.height + self.single_story + 2, self.z, self.x + (self.width / 2) - 1, self.height + self.single_story + 2, self.z - (self.length / 2), block.FENCE_BIRCH)
            mc.setBlocks(self.x + 1, self.height + self.single_story + 2, self.z - 1, self.x + (self.width / 2) - 1, self.height + self.single_story + 2, self.z - (self.length / 2 - 1), block.AIR)
        else:
            mc.setBlocks(self.x + (self.width / 2), self.height + self.single_story + 2, self.z - (self.length / 2) - 1, self.x + self.width, self.height + self.single_story + 2, self.z - self.length, block.FENCE_BIRCH)
            mc.setBlocks(self.x + (self.width / 2) + 1, self.height + self.single_story + 2, self.z - (self.length / 2) - 1, self.x + self.width - 1, self.height + self.single_story + 2, self.z - self.length + 1, block.AIR)

    def createRooms(self):
        num_rooms = 4

        if self.stories == self.double_story:
            num_rooms = 3
            self.createSecondStory()

        for i in range(num_rooms): 
            room_type = randint(1, num_rooms)
            self.createRoom(i + 1, room_type)

    def createPool(self):
        pool_length = 9

        mc.setBlocks(self.x, self.height, self.z - self.length - 3, self.x + pool_length, self.height - 2, self.z - self.length - pool_length, block.STONE_BRICK)
        mc.setBlocks(self.x + 1, self.height, self.z - self.length - 4 , self.x + pool_length - 1, self.height - 1, self.z - self.length - pool_length + 1, block.WATER_STATIONARY)
        mc.setBlocks(self.x , self.height + 1, self.z - self.length - 3, self.x + pool_length, self.height + 1, self.z - self.length - pool_length, block.FENCE_DARK_OAK)
        mc.setBlocks(self.x + 1, self.height + 1, self.z - self.length - 4, self.x + pool_length - 1, self.height + 1,  self.z - self.length - pool_length + 1, block.AIR)
        mc.setBlock(self.x + pool_length // 2, self.height + 1,  self.z - self.length - 3, block.FENCE_GATE)

    def generateHouse(self):
        self.createFoundation()
        self.clearInside()
        self.createRoof()
        self.createRooms()
        
        self.createPool()
    
    def getDoorPos(self):
        return [self.x + 3, self.z, self.height + 1]


# main for using by file by itself, can be commented out/ remove
# if __name__ == '__main__':
#     mc = Minecraft.create() 
#     x, y, z = mc.player.getTilePos()
#     house = LaskarisHouse(x, y, z)
    
#     house.generateHouse()
