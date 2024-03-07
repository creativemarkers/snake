"""
work in progress
"""
import random

class Cookie:
    
    currentPosition = (0,0)
    canSpawn = False

    def __init__(self,mapSize, snake:list):

        self.generateSpawn(mapSize, snake)
        

    def generateSpawn(self, mapSize, snake:list):
        self.canSpawn = False

        attempts = 0

        while self.canSpawn == False:

            randomX = random.randint(0, mapSize-1)
            randomY = random.randint(0, mapSize-1)

            potentialSpawn = (randomX,randomY)

            if potentialSpawn not in snake:
                self.currentPosition = potentialSpawn
                self.canSpawn = True
            elif attempts >= mapSize * mapSize:
                return IndexError

            
            attempts += 1