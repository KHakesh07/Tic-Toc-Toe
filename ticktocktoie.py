import random
import os, time

board = [ "-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "x"
winner = None
gameRunning = True

print('\033[35m')
print(" Welcome To Tic Tac Toe")
print()
print('\033[39m', "let's Start the GAME!")
time.sleep(3)
#printing the game board
def printBoard(board):
    print('\033[31m')
    print("  -------------------")
    print('\033[33m')
    print(('\033[31m'),"| ",('\033[33m'), board[0] + ('\033[31m')," | " + ('\033[33m'), board[1] + ('\033[31m')," | " + ('\033[33m'), board[2], ('\033[31m')," |")
    print('\033[31m')
    print("  -------------------")
    print('\033[33m')
    print(('\033[31m'),"| ", ('\033[33m'),board[3] + ('\033[31m')," | " + ('\033[33m'),board[4] + ('\033[31m')," | " + ('\033[33m'),board[5] ,('\033[31m')," |")
    print('\033[31m')
    print("  -------------------")
    print('\033[33m')
    print(('\033[31m'),"| ", ('\033[33m'),board[6] + ('\033[31m')," | " + ('\033[33m'),board[7] + ('\033[31m')," | " + ('\033[33m'),board[8] ,('\033[31m')," |")
    print('\033[31m')
    print("  -------------------")
    print('\033[34m')



#take the player input
def playerInput(board):
    inp = int(input("enter a no 1-9: "))
    time.sleep(1)
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in the spot!")

#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"the winner is of this GAME Is {winner}")

#switch the palyer
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

#computer
def computer(board):
    while currentPlayer == "o":
        position =random.randint(0,8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()
#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)