"""
this file will need to be refactored
"""

import random
from map import Map
from snake import Snake
from cookie import Cookie

class drawer:

    #sets game size
    mapSize = 20
    #creates map
    m = Map(mapSize)
    #creates starting length of snake might put it back into a class we'll see
    # snake = [(0,0)] * 4
    #creates cookie might nto need it's own class
    cookie = cookie()
    start = True

    def drawMap():
    
    def snakeStartingPosition(self):
        # randomX = random.randint(4, self.mapSize - 4)
        randomY = random.randint(4, self.mapSize - 4)
        return 6, randomY
    
    def calculateSnakePosition(self):
        # start from last index to second to first Index
        #     assign the the current index value to the next index value 
        #     ie: index 4 will take index 3 value and so on

        for i in in range(len(self.snake))

    
    def drawSnakeOnMap(self):
        for i in range(len(self.snake)):
            x,y = self.snake[i]
            if i == 0:
                self.m.changeSymbol(y,x,"^")
            else:
                self.m.changeSymbol(y,x,"+")
    

    def cookiePosition():

    def drawGame(self, input):
        if self.start == True:
            x,y = self.snakeStartingPosition()
            self.drawSnakeOnMap(x, y)
            self.start = False

        snake.CalculatePosition():

        calculateCookiePosition and add to map

    

        return DrawnGame
        




            

if __name__ == "__main__":
    main()