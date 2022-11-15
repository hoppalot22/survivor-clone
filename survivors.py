import pygame as pg
import sys
import os




class Session:
    def __init__(self):
        self.InitGame():
        
    def RenderGame(self):
        

class Camera:
    def __init__(self):
        position = [0,0]
        

class Entity:
    def __init__(self, ID, collisionBox, sprite):
        self.collisionBox = collisionBox
        self.sprite = sprite
        
    def pickup(self):
        pass
    
    def despawn(self):
        pass
                
    
        
class Enemy(Entity):
    
    def 
    __init__(self):
        

class Item(Entity):
    def __init__(self)

class Player(Entity):
    def __init__(self):


def Main():

    fps = 60
    InitGame()
    while running:
    Update()
    
if __name__ == "__main__":
    Main()
