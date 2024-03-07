import time
import os
from map import Map
from snake import Snake
from input import Input
from cookie import Cookie

def clear_screen():
    #to avoid jarring shaking visual from terminal call it at the beggining of the while loop
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    gameOver = False
    mapSize = 20
    m = Map(mapSize)
    snake = Snake(mapSize)
    cookie = Cookie(mapSize, snake.snake)
    input = Input()
    while gameOver == False:
        clear_screen()
        m.printSnake(snake.snake)
        m.printCookie(cookie.currentPosition)
        m.printMap()
        m.deleteSnake(snake.snake)
        
        snake.moveSnakeHead(input.get_input(0.2))

        time.sleep(0.01)

        if snake.checkIfSnakeAteItself() == True:
            print("You ate yourself!")
            gameOver = True

        if snake.outOfBounds() == True:
            print("You went out of Bounds!")
            gameOver = True

        if snake.ateCookie(cookie.currentPosition) == True:
            m.deleteCookie(cookie.currentPosition)
            snake.grow()
            cookie = Cookie(mapSize, snake.snake)
        
        time.sleep(0.05)

    print("GameOver, you ate %s cookies!" % snake.cookiesEaten)

main()