import sys

start = sys.argv[1]
# b="........."
def printboard(board):
    print(board[0:3] + "     012")
    print(board[3:6] + "     345")
    print(board[6:9] + "     678")
def worl(result,side): #changes the result to text like win/lose
    if result==0:
        return "tie"
    elif(result==1 and side=='X' or result==-1 and side=='O'):
        return "win"
    else:
        return "loss"
def gameover(board,turn):
    oturns= "X"
    if turn == 'X':
        oturns = "O" #opposite turns
    if (board[0:3]) == turn*3 or board[3:6] == turn*3 or board[6:9] == turn*3 :
        return 1
    elif (board[0:3]) == oturns*3 or (board[3:6]) == oturns*3 or  (board[6:9]) == oturns*3:
        return -1
    elif(board[0] +board[4] + board[8]== turn*3 or board[2] +board[4] + board[6]== turn*3 or board[0] +  board[3] + board[6] == turn*3 or  board[1] +  board[4] + board[7] == turn*3 or  board[2] +  board[5] + board[8] == turn*3):
        return 1
    elif( board[0] +board[4] + board[8]== oturns*3 or board[2] +board[4] + board[6]== oturns*3 or  board[0] +  board[3] + board[6] == oturns*3 or board[1] +  board[4] + board[7] == oturns*3 or board[2] +  board[5] + board[8] == oturns*3 ):
        return -1
    if '.' not in board:
        return 0
    return None
def possible_next_boards(board,turn):
    boardlist = []
    count =0
    for l in board:
        if(l=='.'):
            
            boardlist.append((board[0:count] + turn +board[count+1: 9],count))
        count=count+1
    return boardlist

def negamax(board,turn): #NegaMax Code 
    if not gameover(board,turn) == None:#if the game is over return the value of the board
        return gameover(board,turn)
    results = list()
    turns = "X" #turns is just the opposite turn
    if turn == "X":# if the turn is x right now then the next turn will be o
        turns ="O"
    for next_board in (possible_next_boards(board, turn)):# for every possible board with the current turn append it to a list with a value multiplied by -1 
        results.append(-1*negamax(next_board[0],turns))
    return max(results) # return the greatest result number

letter='X'
turn = 'X'

if(start=='.........'): # if the board is empty ask for the side
    letter = input("Should I be X or O?")
else:
    countx=0 # if the board isnt empty determine which sides turn it is and play first
    counto=0
    for j in start:
        if(j=='O'):
            counto=counto+1
        elif(j=="X"):
            countx=countx+1
    if(not counto==countx):
        letter='O'
        turn='O'
board = start
while(gameover(board,letter)==None):
    print("Current board:")
    printboard(board)
    if(turn=='X'):
        if(letter=='O'): #if the turn is x but the letter for the computer is O have the user input
            l = ' '
            for n in range (len(board)): 
                if board[n] =='.':
                    l=l+ str(n) + " "
            user = int(input("You can move to any of these spaces:"+ l))
            board= board[0:user] + turn + board[user+1:9] 
            turn='O'
        else:
            best = -2 # have the computer move if the turn is x and the computer turn is x
            bests = tuple()
            c=0
            for q in (possible_next_boards(board, 'X')): # for every next possible board for x run negamax of O on it and multiply it by -1 since its finding the boards for O
                bigw=-1*negamax(q[0],'O')
                print("Moving at ",q[1]," results in" , worl(bigw,"X"))
                # print (best)
                # print(bigw)
                if best <bigw: #find the best possible move in possible next boards by seeing which one is the biggest
                    best=bigw
                    bests = q
                c=c+1
            board=bests[0]
            print("I choose space", bests[1])
            turn='O'
    else:
        if(letter=='X'):
            l = ' ' #if the turn is o but the letter for the computer is x have the user input
            for n in range (len(board)):
                if board[n] =='.':
                    l=l+ str(n) + " "
            print("You can move to any of these spaces:"+ l)
            user = int(input("Your choice?"))
            board= board[0:user] + turn + board[user+1:9] 
            turn='X'
        else: # have the computer move if the turn is o and the computer turn is o
                best = -1
                bests = tuple()
                c=0
                for q in (possible_next_boards(board, 'O')): # for every next possible board for o run negamax of x on it and multiply it by -1 since its finding the boards for x
                    bigw=-1*negamax(q[0],'X')
                    print("Moving at ",q[1]," results in" , worl(bigw,"X"))
                    # print (best)
                    # print(bigw)
                    if best <bigw: #find the best possible move in possible next boards by seeing which one is the biggest
                        best=bigw
                        # print("a")
                        bests = q
                    c=c+1
                board=bests[0]
                print("I choose space", bests[1])
                turn='X'
printboard(board)
if((gameover(board,letter)==1 and letter== "X") or (gameover(board,letter)==1 and  letter=="O")):
    print("I win!")
elif(gameover(board,letter)==0):
    print("We tied!")
else:
    print("You win!")