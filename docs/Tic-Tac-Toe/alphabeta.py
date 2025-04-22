#Implementation of Two Player Tic-Tac-Toe game in Python.
import time
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {1: ' ' , 2: ' ' , 3: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            7: ' ' , 8: ' ' , 9: ' ' }

tree_size =0


''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board): #we will have to print the board after 
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def max_alphabeta(turn,computer,player,alpha,beta):
    max_value=-999 
    bestMove = 0
    for key in theBoard.keys():
        if (theBoard[key] == ' '):
            theBoard[key] = turn
            score = alphabeta( False,turn,computer,player,alpha,beta)
            theBoard[key] = ' '
            if (score > max_value):
                max_value=score
                bestMove = key
    return bestMove

def alphabeta( isMaximizing,turn,computer,player,alpha,beta):
    global tree_size
    tree_size+=1
    if (checkWhichWon(computer)):
        return 1
    elif (checkWhichWon(player)):
        return -1
    elif (checkBoard()): 
        return 0

    if (isMaximizing):
         max_value=-100 
         for key in theBoard.keys():
             if (theBoard[key] == ' '):
                 theBoard[key] = computer
                 max_value =max(max_value, alphabeta( False,turn,computer,player,alpha,beta))
                 theBoard[key] = ' '
                 alpha=max(alpha,max_value)
                 if (alpha>=beta):
                    break               
         return max_value

    else:
        min_value = 100 
        for key in theBoard.keys():
             if (theBoard[key] == ' '):
                 theBoard[key] = player
                 min_value = min(min_value,alphabeta( True,turn,computer,player,alpha,beta))
                 theBoard[key] = ' '
                 beta=min(beta,min_value)                    
                 if (beta<=alpha):
                  break                 
        return min_value

def checkWhichWon(X_OR_O):
    if theBoard[1] == theBoard[2] and theBoard[1] == theBoard[3] and theBoard[1] == X_OR_O:
        return True
    elif (theBoard[4] == theBoard[5] and theBoard[4] == theBoard[6] and theBoard[4] == X_OR_O):
        return True
    elif (theBoard[7] == theBoard[8] and theBoard[7] == theBoard[9] and theBoard[7] == X_OR_O):
        return True
    elif (theBoard[1] == theBoard[4] and theBoard[1] == theBoard[7] and theBoard[1] == X_OR_O):
        return True
    elif (theBoard[2] == theBoard[5] and theBoard[2] == theBoard[8] and theBoard[2] == X_OR_O):
        return True
    elif (theBoard[3] == theBoard[6] and theBoard[3] == theBoard[9] and theBoard[3] == X_OR_O):
        return True
    elif (theBoard[1] == theBoard[5] and theBoard[1] == theBoard[9] and theBoard[1] == X_OR_O):
        return True
    elif (theBoard[7] == theBoard[5] and theBoard[7] == theBoard[3] and theBoard[7] == X_OR_O):
        return True
    else:
        return False

def checkBoard():
    for key in theBoard.keys():
        if (theBoard[key] == ' '):
            return False
    return True

def check_win(count, turn,total_time):
    # Now we will check if player X or O has won,for every move after 5 moves.
    depth=count
    if count >= 5:

        if theBoard[7] == theBoard[8] == theBoard[9] != ' ':  # across the bottom

            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':  # across the middle
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':  # across the top
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':  # down the left side
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':  # down the middle
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':  # down the right side
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':  # diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':  # diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")
            print("It's a Tie!!")
            print("The depth is = ",depth)
            print("the size is : ",tree_size)
            print("The Total Time is : ",total_time)
            exit()

# Now we'll write the main function which has all the gameplay functionality.
def game():
    player = 'O'
    computer = 'X'
    turn = 'X' #if we want to start before the AI, we switch the turn to 'O'.
    count = 0
    Time=0
    totalTime=0
    for i in range(100):
        printBoard(theBoard)
        print("------------------------------------------------")
        print("It's your turn " + turn + ".Move to which place?")
        print("------------------------------------------------")
        if turn == 'X': 
            start_time = time.time()
            move = max_alphabeta(turn,computer,player,-2000,2000)
            print("The AI played: ",move)
            print("------------------------------------------------")
            Time=(time.time() - start_time)
            totalTime=Time+totalTime
            #print("The AI spent: ",Time,"And chose the move",move) #the time the AI spent on the move.

        else:
            
            move = int(input())

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        check_win(count, turn,totalTime)

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    game()