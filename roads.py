from mcpi import minecraft
import mcpi.block as block
from math import sqrt
import random
mc = minecraft.Minecraft.create()

p = mc.player.getTilePos()

class Lamp_Post:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def create_lamp(self, xc, yc, zc):
        mc.setBlock(xc, yc, zc, 120, 5) # Frame
        mc.setBlocks(xc, yc + 1, zc, xc, yc + 3, zc, 139) # Fence
        mc.setBlock(xc, yc + 4, zc, 169) # Sea Lantern
        mc.setBlock(xc, yc + 5, zc, block.STONE_SLAB) # Top

    def set_lamps(self):
        #mc.setBlocks(self.x - 12, self.y + 15, self.z - 12, self.x + 12, self.y + 15, self.z + 12, block.WOOL) # Area
        #mc.setBlocks(self.x - 24, self.y, self.z - 24, self.x + 24, self.y, self.z + 24, block.AIR) # Air

        # This algorithm below scans a small area in the centre of the foundation for any stone brick blocks. If the block is a stone brick then it will have a chance of setting a lamp 2 blocks next to it.
        for xa in range(-12, 13, 5):
            for za in range(-12, 13):
                if mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za), self.z + za) == 98:
                    
                    if mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 1), self.z + za - 1) == 2:
                        curr_arr1 = mc.getBlocks(self.x + xa - 1, mc.getHeight(self.x + xa - 1, self.z + za - 2), self.z + za - 2, self.x + xa + 1, mc.getHeight(self.x + xa + 1, self.z + za - 3), self.z + za - 3) # if there are no stone bricks around the lamp spot
                        
                        if 98 not in curr_arr1 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) + 2, self.z + za - 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) + 4, self.z + za - 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3), self.z + za - 3) == 2:
                            if random.randint(1, 4) == 4:                   
                                self.create_lamp(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) + 1, self.z + za - 3)

                        # For Nature        
                        if 98 not in curr_arr1 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) + 2, self.z + za - 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) + 4, self.z + za - 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3), self.z + za - 3) in [31, 37, 38]:
                            if random.randint(1, 4) == 4:                
                                self.create_lamp(self.x + xa, mc.getHeight(self.x + xa, self.z + za - 3) - 1, self.z + za - 3)


                    if mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 1), self.z + za + 1) == 2:
                        curr_arr2 = mc.getBlocks(self.x + xa - 1, mc.getHeight(self.x + xa - 1, self.z + za + 3) , self.z + za + 3, self.x + xa + 1, mc.getHeight(self.x + xa + 1, self.z + za + 4), self.z + za + 4) # if there are no stone bricks around the lamp spot
                        
                        if 98 not in curr_arr2 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) + 2, self.z + za + 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) + 4, self.z + za + 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3), self.z + za + 3) == 2:
                            if random.randint(1, 4) == 4:
                                #mc.setBlock(self.x + xa, self.y, self.z + za + 3, block.DIAMOND_BLOCK)
                                self.create_lamp(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) + 1, self.z + za + 3)

                        # For Nature
                        if 98 not in curr_arr2 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) + 2, self.z + za + 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) + 4, self.z + za + 3) == 0 and mc.getBlock(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3), self.z + za + 3) in [31, 37, 38]:
                            if random.randint(1, 4) == 4:
                                #mc.setBlock(self.x + xa, self.y, self.z + za + 3, block.DIAMOND_BLOCK)
                                self.create_lamp(self.x + xa, mc.getHeight(self.x + xa, self.z + za + 3) - 1, self.z + za + 3)


class Roads:
    def __init__(self,x,y,z):
        self.x = x
        self.y = mc.getHeight(x,z)
        self.z = z
        self.xPos = xPos(self.x,self.y,self.z)
        self.xNeg = xNeg(self.x,self.y,self.z)
        self.zPos = zPos(self.x,self.y,self.z)
        self.zNeg = zNeg(self.x,self.y,self.z)

        self.coords = {
            'xPos': {'x': self.xPos.x, 'z': self.xPos.z, 'taken': False},

            'xNeg': {'x': self.xNeg.x, 'z': self.xNeg.z, 'taken': False},

            'zPos': {'x': self.zPos.x, 'z': self.zPos.z, 'taken': False},

            'zNeg': {'x': self.zNeg.x, 'z': self.zNeg.z, 'taken': False}
        }

        self.pos_x = 1
        self.neg_x = 2
        self.pos_z = 3
        self.neg_z = 4
    """Creates a path from the forge to the main road"""
    def forge_road(self):
        forgecount = 0
        xforge,yforge,zforge = self.x-2,self.y,self.z+26
        while True:
            if mc.getBlock(xforge,mc.getHeight(xforge,zforge),zforge) != 98:
                forgecount += 1
                zforge -= 1
            else:
                return forgecount +1

    """Creates a path from the church to the main road"""
    def church_road(self):
        churchcount = 0
        xchurch,ychurch,zchurch = self.x,self.y,self.z-22

        while True:
            if mc.getBlock(xchurch,mc.getHeight(xchurch,zchurch),zchurch) != 98:
                churchcount += 1
                zchurch += 1
            else:
                return churchcount +1
                
    """Creates roads in a randomised order in the x and z axis"""
    def create_roads(self):
        list = ['s', 'r' ,'l']
        for i in range(2):
            xpos = random.choice(list)
            xneg = random.choice(list)
            zpos = random.choice(list)
            zneg = random.choice(list)

            if xpos == 's':
                self.xPos.straight(5)
            elif xpos == 'r':
                self.xPos.right(5)
            else:
                self.xPos.left(5)

            if xneg == 's':
                self.xNeg.straight(5)
            elif xneg == 'r':
                self.xNeg.right(5)
            else:
                self.xNeg.left(5)

            if zpos == 's':
                self.zPos.straight(5)
            elif zpos == 'r':
                self.zPos.right(5)
            else:
                self.zPos.left(5)

            if zneg == 's':
                self.zNeg.straight(5)
            elif zneg == 'r':
                self.zNeg.right(5)
            else:
                self.zNeg.left(5)
            
        self.coords = {
            'xPos': {'x': self.xPos.x, 'z': self.xPos.z, 'taken': False},

            'xNeg': {'x': self.xNeg.x, 'z': self.xNeg.z, 'taken': False},

            'zPos': {'x': self.zPos.x, 'z': self.zPos.z, 'taken': False},

            'zNeg': {'x': self.zNeg.x, 'z': self.zNeg.z, 'taken': False}
        }
        
    def closestRoad(self, door_pos):
        road_point = {}
        shortest = 1000
        orientation = None
        for road_orientaion, pos in self.coords.items():
            if pos['taken'] == False:
                pos['distance'] =  sqrt(((pos['x'] - door_pos[0])**2) + (pos['z'] - door_pos[1])**2)
                
                if pos['distance'] < shortest:
                    shortest = pos['distance']
                    orientation = road_orientaion
                    road_point = pos
                
        road_point['taken'] = True

        return [road_point['x'], road_point['z'], orientation]

    def isRoadBehind(self, door_pos, road_pos, direction, orientation):
        check = None
        if orientation == self.pos_x or orientation == self.pos_z:
            check = road_pos[direction] < door_pos[direction]
        elif orientation == self.neg_x or orientation == self.neg_z:
            check = road_pos[direction] > door_pos[direction]
        
        return check

    # checks if road is left or right to the house
    def checkPosition(self, door_pos, road_pos, direction, orientation):
        check = None

        if orientation == self.pos_x or orientation == self.neg_z:
            check = road_pos[direction] < door_pos[direction]
        elif orientation == self.neg_x or orientation == self.pos_z:
            check = road_pos[direction] > door_pos[direction]
        
        return check

    # Builds road straight across house check if road is no longer next to house
    def aroundHouse(self, door_pos, pos, addition_x, addition_z):
        x = 0
        z = 1
        while (
            (mc.getBlock(door_pos[x] + addition_x, mc.getHeight(door_pos[x] + addition_x, door_pos[z] + addition_z) + 1, door_pos[z] + addition_z) != block.AIR.id 
                or mc.getBlock(door_pos[x] + addition_x, mc.getHeight(door_pos[x] + addition_x, door_pos[z] + addition_z), door_pos[z] + addition_z) != block.GRASS.id) 
            or 
            (mc.getBlock(door_pos[x] - addition_x, mc.getHeight(door_pos[x] - addition_x, door_pos[z] - addition_z) + 1, door_pos[z] - addition_z) != block.AIR.id 
                or mc.getBlock(door_pos[x] - addition_x, mc.getHeight(door_pos[x] - addition_x, door_pos[z] - addition_z), door_pos[z] - addition_z) != block.GRASS.id)
            ):
                pos.straight(1)
                door_pos[x] = pos.x
                door_pos[z] = pos.z

    def placeRoads(self, door_pos, road_pos, pos, vert, horiz, orientation):
        x = 0
        z = 1
        y = 2
        road_orientaion = 2
        expand = 2
        
        # First checks if road is not in front of the door
        # then checks if road is to the left or right and wraps around house
        if self.isRoadBehind(door_pos, road_pos, vert, orientation):
            if self.checkPosition(door_pos, road_pos, horiz, orientation):
                pos.left(expand)

                door_pos[x] = pos.x
                door_pos[z] = pos.z
                door_y = mc.getHeight(door_pos[x], door_pos[z])
                
                if orientation == self.pos_x:
                    pos = zNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_z
                elif orientation == self.neg_x:
                    pos = zPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_z
                elif orientation == self.pos_z:
                    pos = xPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_x
                elif orientation == self.neg_z:
                    pos = xNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_x
            else:
                pos.right(expand)
                
                door_pos[x] = pos.x
                door_pos[z] = pos.z
                door_y = mc.getHeight(door_pos[x], door_pos[z])

                if orientation == self.pos_x:
                    pos = zPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_z
                elif orientation == self.neg_x:
                    pos = zNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_z
                elif orientation == self.pos_z:
                    pos = xNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_x
                elif orientation == self.neg_z:
                    pos = xPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_x
                
            tmp = vert
            vert = horiz
            horiz = tmp
            
            if orientation == self.pos_x or orientation == self.neg_x:
                addition_z = 3
                addition_x = 0

            elif orientation == self.pos_z  or orientation == self.neg_z:
                addition_z = 0
                addition_x = 3
                
            self.aroundHouse(door_pos, pos, addition_x, addition_z)
            
            
        while door_pos[vert] != road_pos[vert]:
            if door_pos[horiz] > road_pos[horiz]:
                if orientation == self.pos_x or orientation == self.neg_z:
                    pos.left(1)
                elif orientation == self.neg_x or orientation == self.pos_z:
                    pos.right(1)
            elif door_pos[horiz] < road_pos[horiz]:
                if orientation == self.pos_x or orientation == self.neg_z:
                    pos.right(1)
                elif orientation == self.neg_x or orientation == self.pos_z:
                    pos.left(1)
            else:
                pos.straight(1)
            
            door_pos[x] = pos.x
            door_pos[z] = pos.z
        
        # Switches orientation if road point has not been reached after moving vertically
        if door_pos[horiz] != road_pos[horiz]:
            door_y = mc.getHeight(door_pos[x], door_pos[z])
            if self.checkPosition(door_pos, road_pos, horiz, orientation):
                if orientation == self.pos_x:
                    pos = zNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_z
                elif orientation == self.neg_x:
                    pos = zPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_z
                elif orientation == self.pos_z:
                    pos = xPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_x
                elif orientation == self.neg_z:
                    pos = xNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_x
            else:
                if orientation == self.pos_x:
                    pos = zPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_z
                elif orientation == self.neg_x:
                    pos = zNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_z
                elif orientation == self.pos_z:
                    pos = xNeg(door_pos[x], door_y, door_pos[z])
                    orientation = self.neg_x
                elif orientation == self.neg_z:
                    pos = xPos(door_pos[x], door_y, door_pos[z])
                    orientation = self.pos_x
            
            tmp = vert
            vert = horiz
            horiz = tmp

            while door_pos[vert] != road_pos[vert]:
                # Check used to see if house under pitched roof - did not work as intended
                # if pos.y > self.y:
                #     pos.y = self.y
                #     while mc.getBlock(door_pos[x], pos.y, door_pos[x]) != block.GRASS.id:
                #         pos.y -= 1
                pos.straight(1)
                door_pos[x] = pos.x
                door_pos[z] = pos.z
        
        # places last block/s to create seamless connection
        if ((orientation == self.pos_x and road_pos[road_orientaion] == 'xNeg') or (orientation == self.neg_x and road_pos[road_orientaion] == 'xPos')
            or (orientation == self.pos_z and road_pos[road_orientaion] == 'zNeg') or (orientation == self.neg_z and road_pos[road_orientaion] == 'zPos')
        ):
            pos.straight(1)
        else:
            mc.setBlock(door_pos[x], pos.y, door_pos[z], block.STONE_BRICK)

    # spawns a road connecting to a house, is mostly seamless, edge case occurs where road endpoint is directly horizontal to the house, could not find a fix
    def connectToHouse(self, house, orientation):
        door_pos = house.getDoorPos()
        pos = None
        
        x = 0
        z = 1
        y = 2

        road_pos = self.closestRoad(door_pos)
        height = door_pos[y] - 1
        if orientation == self.pos_x:
            door_pos[x] += 1
            pos = xPos(door_pos[x], height, door_pos[z])
            self.placeRoads(door_pos, road_pos, pos, x, z, orientation)
        elif orientation == self.neg_x:
            door_pos[x] += 1
            pos = xNeg(door_pos[x], height, door_pos[z])
            self.placeRoads(door_pos, road_pos, pos, x, z, orientation)
        elif orientation == self.pos_z:
            door_pos[z] += 1
            pos = zPos(door_pos[x], height, door_pos[z])
            self.placeRoads(door_pos, road_pos, pos, z, x, orientation)
        elif orientation == self.neg_z:
            door_pos[z] += 1
            pos = zNeg(door_pos[x], height, door_pos[z])
            self.placeRoads(door_pos, road_pos, pos, z, x, orientation)

"""Generates road in the x positive direction that climbs over hills as needed"""
class xPos:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def straight(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z-1,self.x,self.y,self.z+1, 98)
            self.x += 1
            height = (mc.getHeight(self.x,self.z-1),mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z+1))
            self.y = max(height)

    def right(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x,self.y,self.z+2, 98)
            self.x += 1
            self.z += 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z+2),mc.getHeight(self.x,self.z+1))
            self.y = max(height)
            

    def left(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x,self.y,self.z-2, 98)
            self.x += 1
            self.z -= 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z-2),mc.getHeight(self.x,self.z-1))
            self.y = max(height)

"""Generates road in the x negative direction that climbs over hills as needed"""
class xNeg:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def straight(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z-1,self.x,self.y,self.z+1, 98)
            self.x -= 1
            height = (mc.getHeight(self.x,self.z-1),mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z+1))
            self.y = max(height)

    def left(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x,self.y,self.z+2, 98)
            self.x -= 1
            self.z += 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z+2),mc.getHeight(self.x,self.z+1))
            self.y = max(height)
    def right(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x,self.y,self.z-2, 98)
            self.x -= 1
            self.z -= 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x,self.z-2),mc.getHeight(self.x,self.z-1))
            self.y = max(height)

"""Generates road in the z positive direction that climbs over hills as needed"""
class zPos:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def straight(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x+1,self.y,self.z,self.x-1,self.y,self.z, 98)
            self.z += 1
            height = (mc.getHeight(self.x-1,self.z),mc.getHeight(self.x,self.z),mc.getHeight(self.x+1,self.z))
            self.y = max(height)

    def right(self, repetitions):

        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x-2,self.y,self.z, 98)
            self.z += 1
            self.x -= 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x-1,self.z),mc.getHeight(self.x-2,self.z))
            self.y = max(height)

    def left(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x+2,self.y,self.z, 98)
            self.x += 1
            self.z += 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x+1,self.z),mc.getHeight(self.x+2,self.z))
            self.y = max(height)

"""Generates a road in the z negative direction that climbs over hills as needed"""
class zNeg:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def straight(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x+1,self.y,self.z,self.x-1,self.y,self.z, 98)
            self.z -= 1
            height = (mc.getHeight(self.x-1,self.z),mc.getHeight(self.x,self.z),mc.getHeight(self.x+1,self.z))
            self.y = max(height)

    def right(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x+2,self.y,self.z, 98)
            self.x += 1
            self.z -= 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x+1,self.z),mc.getHeight(self.x+2,self.z))
            self.y = max(height)
            

    def left(self, repetitions):
        for i in range(repetitions):
            mc.setBlocks(self.x,self.y,self.z,self.x-2,self.y,self.z, 98)
            self.z -= 1
            self.x -= 1
            height = (mc.getHeight(self.x,self.z),mc.getHeight(self.x-1,self.z),mc.getHeight(self.x-2,self.z))
            self.y = max(height)

# if __name__ == '__main__':
#     x, y, z = mc.player.getTilePos()
    
#     road = Roads(x,y,z)
#     road.create_roads()
