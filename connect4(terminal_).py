#Keshav Kumar

#Connect 4 Game

board = [[0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0],

         [0,0,0,0,0,0,0]]


turn = 0


def check_win():

    '''

    Checks If game has been won.

    

    Preconditions: NONE

    

    Paramaters: NONE

    

    Returns a list where list[0] is either 0 which means win or 1 which means no win. list[1] is the player that has won, and list[2] consists of a tuple that contains

    the coordinates of the base of the winning formation. and finally list[3] consists of how the player had won. i.e (horizantally, Verticly, etc.)


    '''

    #Iterate Through Each cell

    r = 0

    c = 0

    for row in board:

        c=0

        for column in row:

            #If it is a player coin then check for win

            if column == 1:

                #Vertical

                #Making sure that there is no Index Error When Checking as this is going to be impossible anyway

                if r >= 3:

                    if board[r][c] == 1 and board[r-1][c] == 1 and board[r-2][c] == 1 and board[r-3][c] == 1:

                        print("Player 1 has WON")

                        return [0, 1,(r,c), "Vertical"]

                #horizantal

                #Making sure that there is no Index Error When Checking as this is going to be impossible anyway

                if c <= 3:

                    if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:

                        print("Player 1 has WON")

                        return [0, 1,(r,c), "Horizantal"]

                #Diagonol Right

                #Making sure that there is no Index Error When Checking as this is going to be impossible anyway

                if r>=3 and c<=3:

                    if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:

                        print("Player 1 has WON")

                        return [0, 1,(r,c), "Diagonal Right"]

                #Diagonol Right

  #Making sure that there is no Index Error When Checking as this is going to be impossible anyway

                if r>=3 and c>=3:

                    if board[r][c] == 1 and board[r-1][c-1] == 1 and board[r-2][c-2] == 1 and board[r-3][c-3] == 1:

                        print("Player 1 has WON")

                        return [0, 1,(r,c), "Diagonal Left"]      

            if column == 2:     

                if r >= 3:

                    if board[r][c] == 2 and board[r-1][c] == 2 and board[r-2][c] == 2 and board[r-3][c] == 2:

                        print("Player 2 has WON")

                        return [0, 2,(r,c), "Vertical"]

                if c <= 3:

                    if board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:

                        print("Player 2 has WON")

                        return [0, 2,(r,c), "Horizantal"]

                if r>=3 and c<=3:

                    if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:

                        print("Player 2 has WON")

                        return [0, 2,(r,c), "Diagonal Right"]

                if r>=3 and c>=3:

                    if board[r][c] == 2 and board[r-1][c-1] == 2 and board[r-2][c-2] == 2 and board[r-3][c-3] == 2:

                        print("Player 2 has WON")

                        return [0, 3,(r,c), "Diagonal Left"]

            c+=1

        r+=1

    return [1, None]

            


def place(player, c):

    '''

Places a characters coin in given column

    

    Preconditions: Player Argument is either a integer 1 or 2

                        column argument is a integer value within 1-7

                   

    Parameters: Integer Player argument, and Integer column argument

    

    Returns a list with list[0] = 1 if sucsesffull and 0 if not. list[1] is which player this correseponds to,

    and list[2] is string which describes error for testing


    '''

    

    

    row = 0

    column = int(c)

    #Mode Checker

    if player == 1:

        #Checks if column is empty 

        if board[6][column-1] == 0:

            board[6][column-1] = 1

            return 0

        #Checks if column is full

        if board[0][column-1] == 1 or board[0][column-1] == 2:

            return [1, 1, f"Column #{column} is full."]

        #Checks if botton cell is empty moving the cell down

        while board[row+1][column-1] != 1 and board[row+1][column-1] != 2:

            row += 1

        #places coin

        board[row][column-1] = 1

        return [0,1,f"coin placed at column {column}"]

    

    elif player == 2:

        if board[6][column-1] == 0:

            board[6][column-1] = 2

            return [1, 2, f"Column #{column} is full."]

        if board[0][column-1] == 2:

            print("Invalid, this row is full")

            return 1

        

        while board[row+1][column-1] != 1 and board[row+1][column-1] != 2:

            row += 1

        board[row][column-1] = 2

        return [0,2,f"coin placed at column {column}"]

        



def validate(data, mode):

    '''

    Takes data and validates it, so as to cause no errors.

    

 Preconditons: Mode is a string that corresponds to one of the modes present.

    

    Paramters: str or int data

                    str mode

    returns the correct value of data provided. returns a integer dt

    

    '''

    dt = data

    if mode == "Column":        

        while dt.isdigit() == False or int(dt) > len(board[0]) or int(dt) <= 0 or board[0][int(dt)-1] == 1 or board[0][int(dt)-1] == 2:

            dt = input("Please Enter a Integer Value corresponding to a Empty Column: ")

            

        

        return int(dt)

    

def showBoard():

    '''

    simply shows/prints board for player

    

    preconditions: NONE

    

    Parameters: NONE

    

    Returns: NOTHING

    '''

    print("        BOARD")

    for i in board:

        print(i)

            

            


#main program

print("Welcome to the Connect 4 Game!\nWin by placing 4 coins on top of each other.")

showBoard()

# Main Game Loop

x = check_win()

while x[0] == 1 or turn > 49:

    #Data Validation 

    P1C = input(f"Player 1: Enter a Column where you want to place your coin: It is the #{turn} turn: ")

    PLayer1Choice = validate(P1C, "Column")

    #Placing Coin

    place(1, PLayer1Choice)

    

    showBoard()

    x = check_win()

    

    #Makings sure other person hasnt won

    if x[0] != 0 and x[1]!=1:
        #Data Validation
        P2C = input(f"Player 2: Enter a Column where you want to place your coin: It is the #{turn} turn: ")
        PLayer2Choice = validate(P2C, "Column")
        #Placing Coin2
        place(2, PLayer2Choice)
        showBoard()
        x = check_win()
    turn+=1

if turn > 49:

    print("Board Full, Tie Game!")
