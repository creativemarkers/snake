from snake import Snake

class Map:

    size = None

    mapCords = None

    emptyMapSpaceSymbol = "-"



    def __init__(self,size:int):
        self.size = size
        self.createMap()

    def createMap(self):
    
        self.mapCords = [[] for _ in range(self.size)]

        for i in range(len(self.mapCords)):
            self.mapCords[i] = [self.emptyMapSpaceSymbol] * self.size
            # next 3 lines prints the map to console
            # for j in range(len(self.mapCords)):
            #     print(self.mapCords[i][j],end=" ")
            # print("")

    def printMap(self):
        for i in range(len(self.mapCords)):
            for j in range(len(self.mapCords)):
                 print(self.mapCords[i][j],end="  ")
            print("")
        print("=================")


    def changeSymbol(self,y,x,symbol):
        #will prob change this to be print cookie
        self.mapCords[y][x] = symbol

    def printSnake(self, snake:list):

        for i in range(len(snake)):
            x,y = snake[i]
            if i == 0:
                self.mapCords[y][x] = "O"
            else:
                self.mapCords[y][x] = "S"

    #def deleteSnake():
            