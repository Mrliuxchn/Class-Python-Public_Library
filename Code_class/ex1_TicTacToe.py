#Tic Tac Toe
import random

def drawBoard(board):
    #this function prints out the board that it was passed.

    #"board" is a list of 10 strings representing the board(ignore index0)

    print("    |    |")
    print("  "+board[1]+" |"+board[2]+"   |  "+board[3])
    print("    |    |")
    print("-------------")
    print("  "+board[4]+" |"+board[5]+"   |  "+board[6])
    print("    |    |")
    print("-------------")
    print("  "+board[7]+" |"+board[8]+"   |  "+board[9])
    print("    |    |")
    print("-------------")

def inputPlayerLetter():
    #Lets the player type which letter they want to be.
    #Returns a list with the player's letter as the first item,and the
    #computer's letter as the second

    letter=""
    while not(letter == "X" or letter =="O" ):
        print("Do you want to be X or O?")
        letter=input().upper()

    #the first element in the list is the player's letter
    #the second is computer's letter
    if letter == "X" :
        return ["X","O"]
    else:
        return ["O","X"]

def whoGoesFirst():
    #Randomly choose the player who goes first.
    if random.randint(0,1) ==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #this function returns True if the player wants  to play again.
    #otherwise it returns False
    print("Do you want to play again?(yes or no)")
    return input().lower().startswith('y')

  

def makeMove(board,letter,move):
    board[move] =letter

def isWinner(board,letter):
    #Given a board and a player's letter, this function returns True
    #if that player has won.
    
    return ((board[7] == letter and board[8]== letter and board[9]==letter) or #across the top
            (board[4] == letter and board[5]== letter and board[6]==letter) or #across the middle
            (board[1] == letter and board[2]== letter and board[3]==letter) or #across the bottom

            (board[1] == letter and board[4]== letter and board[7]==letter) or #down the left side
            (board[2] == letter and board[5]== letter and board[8]==letter) or #down the middle side
            (board[3] == letter and board[6]== letter and board[9]==letter) or #down the right side
            (board[7] == letter and board[5]== letter and board[3]==letter) or #diagonal
            (board[1] == letter and board[5]== letter and board[9]==letter))  #diagona

def getBoardCopy(board):
    #Make a duplicate of the board list and return it the duplicate.
    dupBoard=[]

    for i in board:
          dupBoard.append(i)
    return dupBoard

def isSpaceAvailable(board,move):
    #Return True if the passed move is available on the passed board.
    return (board[move]==" ")

def getPlayerMove(board):
    #Let the player type in their move.
    move=""
    while move not in "1,2,3,4,5,6,7,8,9".split(",") or not isSpaceAvailable(board,int(move)):
        print("What is your next move?(1--9))")
        move=input()
        
    return int(move)

def chooseRandomMoveFromList(board,moveList):
    #Returns a valid move from the passed list on the passed board.
    #Returns None if there is no valid move.
    possibleMoves=[]
    for i in moveList:
        if isSpaceAvailable(board,i):
              possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return possibleMoves[random.randint(0,len(possibleMoves)-1)]
    else:
        return None

def getComputerMove(board,computerLetter):
    #Given a board and the computer's letter
    #determine where to move and return that move
    if computerLetter == "X" :
        playerLetter="O"
    else:
        playerLetter="X"

    #here is our algorithm for our Tic Tac Toe AI:
    #First, check if we can win in the next move
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceAvailable(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i;

    #check if the palyer could win on their next move,and block them.
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceAvailable(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i;


    #Try to take one of the corners,if they are available
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    #Try to take the center,if it is available
    if isSpaceAvailable(board,5):
        return 5

    #Move on one of the sides.
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #Return True if every space on the board has been taken,
    #otherwise return False
    for i in range(1,10):
        if isSpaceAvailable(board,i):
              return False

    return True

#Program start

print("Welcome to Tic Tac Toe!")

while True:
    #Reset the board
    theBoard=[" "] * 10
    playerLetter,computerLetter=inputPlayerLetter()
    turn=whoGoesFirst()
    print("The "+turn +" will go first.")
    gameIsPlaying =True

    while gameIsPlaying:
        if turn == 'player':
                #Player's turn
                #drawBoard(theBoard)
                move=getPlayerMove(theBoard)
                makeMove(theBoard,playerLetter,move)
                print("the player has placed at %d" % move)
                drawBoard(theBoard)

                if isWinner(theBoard,playerLetter):
                    #drawBoard(theBoard)
                    print("Bravo! You win!")
                    gameIsPlaying=False
                else:
                    if isBoardFull(theBoard):
                        #drawBoard(theBoard)
                        print("The game is a tie!")
                        break
                    else:
                        turn='computer'
        else:
              #computer's turn
              move=getComputerMove(theBoard,computerLetter)
              makeMove(theBoard,computerLetter,move)
              print("the computer has placed at %d" % move)
              drawBoard(theBoard)

              if isWinner(theBoard,computerLetter):
                  #drawBoard(theBoard)
                  print("The computer has beaten you! You lose!")
                  gameIsPlaying=False
              else:
                  if isBoardFull(theBoard):
                      #drawBoard(theBoard)
                      print("The game is a tie!")
                      break
                  else:
                      turn="player"

    if not playAgain():
        break
              
              
              


              
              
              
              
              
          
          


          
    
    
    
