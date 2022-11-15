import pygame as pg
import sys
import os


class Profile:
    def __init__(self):
        #Read file with profile stats
        #Update below with info
        pass

class Session:
    def __init__(self):
        self.InitGame()
        self.entities = []
        
    def RenderGame(self):
        pass
     
    def addEntity(self, entity):
        if(type(entity) is Entity):
            self.entities.append(entity)
            entity.session = self
            
        else:
            raise("Can only add entities with addEntity")
     
    def InitGame(self):
        pass
        
    def Update(self):
        pass

class Camera:
    def __init__(self):
        position = [0,0]
        

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
    myCamera = Camera()
    myPlayer = Player()
    print(myPlayer.ID)
    print(myPlayer.collisionBox)
    print(myPlayer.sprite)
    print(Camera.position())
    

    fps = 60
    InitGame()
    while running:
        mySession.Update()
    
if __name__ == "__main__":
    Main()
