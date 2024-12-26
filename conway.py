#CONWAYS GAME OF LIFE, KESHAV
import turtle as t
#important variables
tileSize = 40
status = "notRunning"
#Change is set to 1 so that the loop runs at least once
change = 1
generation = 1
#Making Screen
sc = t.Screen()
class Tile():
   def __init__(self, x, y, color,size):
       '''
       makes a tile with the given properties
       preconditions: x, y, color, and size are defined by user
       parameters: int x, int y, str color, int size (from self)
       returns nothing
       '''
       self.x = x
       self.y = y
       self.color = color
       self.size = size
   def draw(self):
       '''
       draws tile with its properties
       preconditions: x, y, color, and size are defined
       parameters: int x, int y, str color, int size (from self)
       returns nothing    
       '''
       tile = t.Turtle()
       tile.ht()
       tile.pu()
       tile.speed(0)
       tile.color(self.color)
       tile.goto(self.x, self.y)
       tile.begin_fill()
       for _ in range(4):
           tile.pd()
           tile.fd(self.size)
           tile.rt(90)
       tile.end_fill()
def makeBoard(size):
    '''
    makes a board of the given size
    preconditions: size is a positive integer
    parameters: int size
    returns a 2D list of the given size
    '''
    row = []
    board = []
    for _ in range(size):
        row.append("W")
    for _ in range(size):
        board.append(list(row))
    return board
def drawLevel(l,xCor,y):
   '''
   draws the level on the screen based on level provided
   preconditions: lev is a 2D list, xCor and y are ints representing coordinates on the screen
   parameters: list lev, int xCor, int y
   returns Nothing
   '''
   t.tracer(0, 0)
   for row in l:
       x = xCor
       for tile in row:
           if tile == "W" or tile == 1 :
               tile = Tile(x, y, "white", tileSize)
               tile.draw()
           elif tile == "B" or tile == 2 :
               tile = Tile(x, y, "black",  tileSize)
               tile.draw()
           x+=tileSize
       y-=tileSize
   t.tracer(1, 1)
#Setting up the Screen & Drawing the Level
def setup(lev):
    '''
    sets up the screen and draws the level based on the size
    preconditions: lev is a 2D list
    parameters: list lev
    returns Nothing
    '''
    sc.setup(width=(len(lev[0])*tileSize ), height=(len(lev)*tileSize))
    sc._root.resizable(False, False)
    x = -(len(lev[0])*tileSize)/2
    y = (len(lev)*tileSize)/2
    drawLevel(lev, x, y)
def checkNeighbors(r,c):
    '''
    checks neighbors of a given cell
    preconditions: r and c are ints representing the row and column of the cell
    parameters: int r, int c
    returns an int representing the number of live neighbors
    '''

    liveNeighbors = 0

    if conway[r-1][c-1] == "B":

        liveNeighbors += 1

    if conway[r-1][c] == "B":

        liveNeighbors += 1

    if conway[r-1][c+1] == "B":

        liveNeighbors += 1

    if conway[r][c-1] == "B":

        liveNeighbors += 1

    if conway[r+1][c-1] == "B":

        liveNeighbors += 1

    if conway[r+1][c] == "B":

        liveNeighbors += 1

    if conway[r+1][c+1] == "B":

        liveNeighbors += 1

    if conway[r][c+1] == "B":

        liveNeighbors += 1

    return liveNeighbors









def highlight(x, y):

    '''

    highlights the cell at the given coordinates

    preconditions: x and y are ints representing coordinates on the screen

    parameters: int x, int y

    returns Nothing    

    '''

    #Makes it so that tracer is turned off so that the screen doesn't update

    t.tracer(0,0)

    #Makinf sure the mouse can do anything while running

    if status != "running" :

        #Translating the current coordinates system so that the origin is top right

        middle = (boardLen*tileSize)/2

        y = y * -1

        newX = middle + x

        newY = middle + y  

        #Using new coordinates to find the tile that the mouse is over

        row = newX // tileSize

        col = newY // tileSize

        #highlighting the tile that the mouse is over

        if conway[int(col)][int(row)] == "W":

            conway[int(col)][int(row)] = "B"

        else:

            conway[int(col)][int(row)] = "W"

        #Drawing Board

        x = -(len(conway[0])*tileSize)/2

        y = (len(conway)*tileSize)/2

        drawLevel(conway, x, y)

    #So the screen updates when eveerything is done.

    t.tracer(1,1)



def evolve(board):

    '''

    evolves the board based on the rules of Conway's Game of Life

    preconditions: board is valid 2D list

    parameters: list board

    returns an int representing the number of changes made to the board

   

    '''

    #Lists to store the squares that need to be erased and added to the board and the change value

    toEraseList = []

    toAddList = []

    changeNum = 0

    #Iterating through the board and checking the rules of the game of life

    for row in range(boardLen-1):

        for column in range(boardLen-1):

            r = row

            c = column

            #Checking rules of the game of life

            if board[r][c] == "B":

                liveNeighbors = checkNeighbors(r, c)

                if liveNeighbors > 3 or liveNeighbors < 2:

                    toEraseList.append((r,c))

            if conway[r][c] == "W":

                liveNeighbors = checkNeighbors(r, c)

                if liveNeighbors == 3:

                    toAddList.append((r,c))

    #Changing all the squares that need to be erased and added to the board

    for square in toEraseList:

        conway[square[0]][square[1]] = "W"

        changeNum += 1

    for square in toAddList:

        conway[square[0]][square[1]] = "B"

        changeNum += 1

    #Drawing the board

    x = -(len(conway[0])*tileSize)/2

    y = (len(conway)*tileSize)/2

    drawLevel(conway, x, y)

    #returning the number of changes made to the board so that the screen stays on only if

    #changes are still being made

    return changeNum



def userInput(mode):

    '''

    simply takes in user input for the board size or the number of generations

    preconditions: mode is either "board" or "generations"

    parameters: string mode

    returns an int representing the size of the board or the number of generations

    '''

    #Taking in user input for the board size or the number of generations based on mode

    if mode == "board":

        data = input("Enter the size of the board: ")

        #Data validation

        while data.isdigit() == False or int(data) < 20 or int(data) > 40:

            data = input("Please input a valid boardLen in between 20 and 40: ")

        return int(data)  

    elif mode == "generations":

        data = input("Enter the number of generations you want this simulation to run until: ")

        #Data validation

        while data.isdigit() == False or int(data) > 200 or int(data) <= 0:

            data = input("Please input a valid number of generations (Under 200): ")

        return int(data)  









#Main Program



print('\nRules:\nAny live cell lives on if it has 2 or 3 neighbors otherwise it dies of over or underpopulation\nAny Dead cell becomes alive if it has exactly 3 Neighbors')

#Data Input & Valdiation

boardLen =  25 #the userInput function can be used here, however for simplicity and performances sake the boardLen is set to 25

maxGenerations = userInput("generations")

#Setting up the Board

conway = makeBoard(boardLen)

setup(conway)

#Setting up the mouse input

t.onscreenclick(highlight)

input("\n\nWelcome to Conway's Game of life!\nClick on the board to make the tile black(Recommend <= 10).\nThen after you have finished, enter anything to start!.")





#Status is set to "running" so that the mouse input can be used

status = "running"

#Main Loop

while change > 0 and generation < maxGenerations:

    change = evolve(conway)

    print(f"Generation: {generation}")

    generation += 1

#Feedback to the user

if generation < maxGenerations:

    print(f"Game Over, your tiles died or stagnated out before generation goal: {maxGenerations}")

else:

    print("Congratulations! Your Tiles have lasted till your desired Generations")



