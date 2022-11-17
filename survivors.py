import pygame as pg
import numpy as np
import sys
import os

class Vector2:
    def __init__(self, x, y):

        self.x = float(x)
        self.y = float(y)

        self.components = [self.x, self.y]

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter > 1:
            raise StopIteration
        component = self.components[self.counter]
        self.counter += 1
        return component

    def __getitem__(self, item):
        return self.components[item]

    def __add__(self, Vec2):
        return Vector2(self.x + Vec2.x, self.y + Vec2.y)

    def __sub__(self, Vec2):
        return Vector2(self.x - Vec2.x, self.y - Vec2.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def VectorMag(self):
        mag = 0
        for component in self:
            mag = math.sqrt(mag * mag + component * component)
        return mag

    def VectorNorm(self):
        mag = self.VectorMag()
        if mag == 0:
            return Vector2(0, 0)
        return Vector2(self.x / mag, self.y / mag)

    def VectorDot(self, vec2):
        return self.x * vec2.x + self.y * vec2.y

class Profile:
    def __init__(self):
        #Read file with profile stats
        #Update below with info
        pass

class Session:
    def __init__(self):
        self.InitGame()
        self.entities = []
        self.camera = None
        
    def RenderGame(self):
        pass
     
    def addEntity(self, entity):
        if(type(entity) is Entity):
            self.entities.append(entity)
            entity.session = self
            
        else:
            raise(f"addEntity can only be used to add entities, got {type(entity)} instead")
     
    def addMap(self):
        self.map = Map(self)
    
     
    def InitGame(self):
        pass
        
    def Update(self):
        pass

class Map:
    def __init__(self, session, width=100, height=100):
        self.origin = Vector2(width/2,height/2)
        self.width = width
        self.height = height
        self.grid = [[Cell(self,Vector2(0,0))]]
        for i in range(width-1):
            self.addCellRow()
        for j in range(height-1):
            self.addCellColumn()
            
        self.camera = Camera(self)
        
    def addCellRow(self):
        self.grid.append([Cell(self, Vector2(i, len(self.grid))) for i in range(len(self.grid[0]))])
            
        
        
    def addCellColumn(self):
        for j, row in enumerate(self.grid):
            row.append(Cell(self, Vector2(len(row), j)))
            
            
            
class Cell:
    def __init__(self, map, position):
        self.map = map
        self.sprite = None
        self.position = position
        
    def setSprite(self, sprite):
        self.sprite = sprite        
        

class Camera:
    def __init__(self, map):
    
        self.defaultCameraFOV = Vector2(20,20)
    
        self.map = map
        self.position = self.map.origin
        self.zoom = Vector2(1,1)
        
        
        self.viewGrid = self.map.grid[int(self.map.origin.x - self.defaultCameraFOV.x/2):int(self.map.origin.x + self.defaultCameraFOV.x/2)][int(self.map.origin.y - self.defaultCameraFOV.y/2):int(self.map.origin.y + self.defaultCameraFOV.y/2)]
        print(int(self.map.origin.x - self.defaultCameraFOV.x/2), int(self.map.origin.x + self.defaultCameraFOV.x/2))
        print(self.map.grid[40:60][5])
        
        self.display = pg.display
        self.display.set_mode((1000,600))
        
        self.UpdateDisplay()
        
    def UpdateDisplay(self):
        self.display.flip()
        

class Entity:
    def __init__(self, collisionBox, sprite):
        self.ID = None
        self.collisionBox = collisionBox
        self.sprite = sprite
        self.session = None
    
    def genID(self):
        self.ID = len(self.session.entities)
        
    
    def pickup(self):
        pass
    
    def despawn(self):
        pass
                
    
        
class Enemy(Entity):
    
    def __init__(self):
        pass

class Item(Entity):
    def __init__(self):
        super().__init__()
        

class Player(Entity):
    def __init__(self):
        super().__init__("CB", "Sprite")


def Main():
    
    mySession = Session()
    mySession.addMap()
    myPlayer = Player()
    print(myPlayer.ID)
    print(myPlayer.collisionBox)
    print(myPlayer.sprite)
    print(mySession.map.camera.viewGrid)
    for j in range(len(mySession.map.camera.viewGrid)):
        print([mySession.map.camera.viewGrid[j][i].position for i in range(len(mySession.map.camera.viewGrid[j]))])
    # for i, row in enumerate(mySession.map.grid):    
        # for j, col in enumerate(row):
            # print(mySession.map.grid[i][j].position)
    

    fps = 60
    mySession.InitGame()
    running = True
    while running:
        mySession.Update()
    
if __name__ == "__main__":
    Main()
