import sys

b = sys.argv[1]
# b="........."
def printboard(a):
    print(a[0:3] + "     012")
    print(a[3:6] + "     345")
    print(a[6:9] + "     678")
def worl(a,b):
    if a==0:
        return "tie"
    elif(a==1 and b=='X' or a==-1 and b=='O'):
        return "win"
    else:
        return "loss"
def gameover(a):
    
    if (a[0:3]) == 'XXX' or a[3:6] == 'XXX' or a[6:9] == 'XXX' :
        return 1
    elif (a[0:3]) == 'OOO' or (a[3:6]) == 'OOO' or  (a[6:9]) == 'OOO':
        return -1
    elif(a[0] +a[4] + a[8]== 'XXX' or a[2] +a[4] + a[6]== 'XXX' or a[0] +  a[3] + a[6] == 'XXX' or  a[1] +  a[4] + a[7] == 'XXX' or  a[2] +  a[5] + a[8] == 'XXX'):
        return 1
    elif( a[0] +a[4] + a[8]== 'OOO'or a[2] +a[4] + a[6]== 'OOO' or  a[0] +  a[3] + a[6] == 'OOO' or a[1] +  a[4] + a[7] == 'OOO' or a[2] +  a[5] + a[8] == 'OOO'):
        return -1
    if '.' not in a:
        return 0
    return None
def possible_next_boards(a,b):
    z = []
    zz=[]
    count =0
    for l in a:
        if(l=='.'):
            
            z.append((a[0:count] + b +a[count+1: 9],count))
        count=count+1
    return z
def max_step(board):
    if not gameover(board) == None:
        return gameover(board)
    results = list()
    for next_board in (possible_next_boards(board, 'X')):
        results.append(min_step(next_board[0]))
    return max(results)
def min_step(board):
    if not gameover(board) == None:
        return gameover(board)
    results = list()
    for next_board in (possible_next_boards(board, 'O')):
        results.append(max_step(next_board[0]))
    return min(results)
a = 0
w='X'
turn = 'X'

if(b=='.........'):
    w = input("Should I be X or O?")
else:
    cx=0
    co=0
    for j in b:
        if(j=='O'):
            co=co+1
        elif(j=="X"):
            cx=cx+1
    if(not co==cx):
        w='O'
        turn='O'
bo = b
while(gameover(bo)==None):
    print("Current board:")
    printboard(bo)
    if(turn=='X'):
        if(w=='O'):
            l = ' '
            for n in range (len(bo)):
                if bo[n] =='.':
                    l=l+ str(n) + " "
            p = int(input("You can move to any of these spaces:"+ l))
            bo= bo[0:p] + turn + bo[p+1:9] 
            turn='O'
        else:
            best = -2
            bests = tuple()
            c=0
            for q in (possible_next_boards(bo, 'X')):
                bigw=min_step(q[0])
                print("Moving at ",q[1]," results in" , worl(bigw,"X"))
                # print (best)
                # print(bigw)
                if best <bigw:
                    best=bigw
                    # print("a")
                    bests = q
                c=c+1
            bo=bests[0]
            print("I choose space", bests[1])
            turn='O'
    else:
        if(w=='X'):
            l = ' '
            for n in range (len(bo)):
                if bo[n] =='.':
                    l=l+ str(n) + " "
            print("You can move to any of these spaces:"+ l)
            p = int(input("Your choice?"))
            bo= bo[0:p] + turn + bo[p+1:9] 
            turn='X'
        else:
                best = 2
                bests = tuple()
                c=0
                for q in (possible_next_boards(bo, 'O')):
                    bigw=max_step(q[0])
                    print("Moving at ",q[1]," results in" , worl(bigw,"O"))
                    # print (best)
                    # print(bigw)
                    if best >bigw:
                        best=bigw
                        # print("a")
                        bests = q
                    c=c+1
                bo=bests[0]
                print("I choose space", bests[1])
                turn='X'
printboard(bo)
if((gameover(bo)==1 and w== "X") or (gameover(bo)==-1 and  w=="O")):
    print("I win!")
elif(gameover(bo)==0):
    print("We tied!")
else:
    print("You win!")