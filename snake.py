import random

class Snake:
    snakemapSize = None
    headSymbolUp = "^"
    headSymbolDown = ""
    headSymbolLeft = "<"
    headSymbolRight = ">"
    snake = [(0,0)] * 4
    currentHeadPosition = None
    lastDirection = None
    moveKey = ["w", "a", "s", "d"]
    potentialHeadCords = None
    cookiesEaten = 0
    lastTailPosition = (0,0)

    SNAKEHEAD = snake[0]
    

    def __init__(self, mapSize):
        self.snakemapSize = mapSize
        #inorder to create a snake you need to give it the mapsize it will operate in to determine it's spawn location
        self.setSnakeStartingPosition(mapSize)

    def setSnakeStartingPosition(self, mapSize):
        #generates a random position to set snake along the y axis

        # randomX = random.randint(4, self.mapSize - 4)
        randomY = random.randint(4, mapSize - 4)

        self.snake[0] = (5,randomY)

        self.currentHeadPosition = self.snake[0]
        
        #calls the below function to set cords for rest of the snake body
        self.setSnakeBody()

    def setSnakeBody(self):
        #should only be used to iniatlize the snake array
        #i can get these cords from the function that calls it, but it works like that too
        x,y = self.currentHeadPosition

        for i in range(1,len(self.snake)):
            #goes through loop to set cords for the body based on the position of the head
            self.snake[i] = (x-1,y)

            x -= 1

    def moveSnakeHead(self, input):
        """
        the function name is a bit of a lie does a bit more then just move the snake head, it moves the whole body
        """
        oldSnake = self.snake
        #grabs the cords of the current position of the snake head to do calculations
        x,y = self.snake[0]

        if input == None:
            #checks if user has input 
            if self.lastDirection in self.moveKey:
                #checks if the user has ever input anything if it hasn't then the snake stays still

                #changes body cords before we change the value of the head
                self.moveSnakeBody()
                #if user has never input snake will stay still
                if self.lastDirection == "w":
                    self.snake[0] = (x,y-1)
                elif self.lastDirection == "s":
                    self.snake[0] = (x, y+1)
                elif self.lastDirection == "a":
                    self.snake[0] = (x-1,y)
                elif self.lastDirection == "d": 
                    self.snake[0] = (x + 1,y)
        else:
            #user has input a valid key, next else if clauses determine the potential position of the new head location
            if input == "w":
                self.potentialHeadCords = (x,y-1)
            elif input == "s":
                self.potentialHeadCords = (x, y+1)
            elif input == "a":
                self.potentialHeadCords = (x-1,y)
            elif input == "d": 
                self.potentialHeadCords = (x + 1,y)

            if self.verifySnakeCanMove() == True:
                #changes body cords before we change the value of the head
                self.moveSnakeBody()
                self.snake[0] = self.potentialHeadCords
                self.lastDirection = input

        
            
    def moveSnakeBody(self):
        #moves the rest of the snake body to the cords of it's previous index, 
        #the for loop starts iterating from back to front and stop at index 1
        self.lastTailPosition = self.snake[-1]

        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i] = self.snake[i-1]
        

    def verifySnakeCanMove(self):
        #verifies that the snake head isn't moving into it's self
        if self.potentialHeadCords == self.snake[1]:
            return False
        else:
            return True
        
    def checkIfSnakeAteItself(self):

        for i in range(1, len(self.snake)):
            if self.snake[0] == self.snake[i]:
                return True
            
        return False
    
    def ateCookie(self, cookieCords:tuple):

        if self.snake[0] == cookieCords:
            self.cookiesEaten += 1
            print("Cookie ate!")
            return True
        return False
    
    def grow(self):
        self.snake.append(self.lastTailPosition)

    def outOfBounds(self):

        x,y = self.snake[0]
        if x == -1 or x == self.snakemapSize:
            return True
        elif y == -1 or y == self.snakemapSize:
            return True
        return False