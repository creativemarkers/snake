import time
from map import Map
from snake import Snake
from input import Input


mapSize = 20
m = Map(mapSize)

snake = Snake(mapSize)

x,y = snake.currentHeadPosition

m.changeSymbol(y,x,">")



startTime = time.time()
elapsedTime = 0.0
timeOut = 10

input = Input()

while elapsedTime <= timeOut:

    m.printMap()
    snake.moveSnakeHead(input.get_input(0.2))
    m.createMap()
    m.printSnake(snake.snake)
    # x,y = snake.snake[0]
    # m.createMap()
    # m.changeSymbol(y,x,">")
    time.sleep(0.05)
    elapsedTime = time.time() - startTime
