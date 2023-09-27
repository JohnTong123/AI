from os import kill

# from othello_imports import possible_moves, make_move
import sys
def possible_moves(board,token):
    boarders_ha = "" # its a board with borders so its BOARDers ha ha  
    for i in range(0,len(board), 8):
        boarders_ha = boarders_ha+"?" + board[i:i+8] + "?"
    boarders_ha = "?"*10 + boarders_ha +"?"*10
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]
    borderpossible = []
    opposite = "x"
    if token == opposite:
        opposite= "o"
    # print(len(boarders_ha))
    for a in range(11,len(boarders_ha)-11,1):
        
        if(boarders_ha[a] == '.'):
            for j in directions:
                # print("a" , len(boarders_ha))
                # print(a + j)
                if boarders_ha[a+j] == opposite:
                    s = a+j
                    while(boarders_ha[s] == opposite):
                        s=s+j
                    if boarders_ha[s] == token:
                        borderpossible.append(a)
                        break
    possible=[]
    for l in borderpossible:
        possible.append(l - 10 - 2* (l//10-1) -1)
    return possible
# print(possible_moves("xxoo.xox.....oox......oxo..ooxooo..oox.ox.xxx..oxoox...o.....xox", "x"))
def make_move(board, token, index):
    boarders_ha = "" # its a board with borders so its BOARDers ha ha  
    for i in range(0,len(board), 8):
        boarders_ha = boarders_ha+"?" + board[i:i+8] + "?"
    boarders_ha = "?"*10 + boarders_ha +"?"*10
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]
    borderpossible = []
    opposite = "x"
    newindex = index + 10 + 2* (index//8) +1
    boarders_ha = boarders_ha[0:newindex] + token + boarders_ha[newindex+1: 100]
    if token == opposite:
        opposite= "o"
    for j in directions:
        if boarders_ha[newindex+j] == opposite:
            s=newindex+j
            while(boarders_ha[s] == opposite):
                s=s+j
            if boarders_ha[s] == token:
                for k in range(newindex,s,j):
                    boarders_ha = boarders_ha[0:k] + token + boarders_ha[k+1: 100]
    bord = boarders_ha[11: 19] + boarders_ha[21: 29] +boarders_ha[31: 39] + boarders_ha[41: 49] +boarders_ha[51: 59] + boarders_ha[61: 69] +boarders_ha[71: 79] + boarders_ha[81: 89]
    # bord = bord[0:index] + token + bord[index+1: 64]
    return bord
corners_dict = {
    0: {1, 8, 9},
    7: {6, 14, 15},
    56: {57, 48, 49},
    63: {62, 54, 55}
}
cornerss_dict = {
    0: {2, 10, 18,16,17},
    7: {5, 13, 21,22,23},
    56: {40, 41, 42,50,58},
    63: {47, 45, 46,61,53}
}
ringofsadge={9,10,11,12,13,14,17,22,25,30, 33,38,41,46,49,50,51,52,53,54}

edges = {1,2,3,4,5,6,57,58,59,60,61,62,8,16,24,32,40,48,15,23,31,39,47,55}
def score(board,token):
    wcorner = 65
    lcorner =95
    badge = 50
    badgee =15
    edgee =15
    rsad=10
    xstable = []
    movescounts = 64-board.count('.')
    ostable=[]
    opposite = 'x'
    if token == 'x':
        opposite='o'
    xcount =0
    ocount=0
    thedub = 0
    xfront =0
    ofront=0
    theway  = [-7,-8,-9,-1,1,7,8,9]
    for a in range(len(board)):
        iscorner = False
        if board[a]=="x":
            xcount=xcount+1
            # if xcount > 15:
            #     thedub=thedub + 2
            # else:
            #     thedub = thedub-2
            for z in corners_dict:
                if z==a:
                    iscorner=True
                    if token =='x':
                        thedub=thedub+wcorner
                    else:
                        thedub=thedub + lcorner
                    for frontierthing in corners_dict[a]:
                        if(board[frontierthing]=='.'):
                            xfront=xfront+1
                            break
                    xstable.append(z)
                    break
                elif a in corners_dict[z] and board[z] == '.':
                    thedub = thedub-badge
                    
                    break
                # elif a in cornerss_dict[z] and board[z] == '.':
                #     thedub = thedub+badgee
                #     break
            if a in edges:
                thedub=thedub+edgee
                if a//8==0:
                    if board[a-1] =='.' or board[a+1] =='.'or board[a+7] =='.'or board[a+8] =='.'or board[a+9] =='.':
                        xfront=xfront+1
                elif a//8 == 7:
                    if board[a-1] =='.' or board[a+1] =='.'or board[a-7] =='.'or board[a-8] =='.'or board[a-9] =='.':
                        xfront=xfront+1
                elif a%8==0 :
                    if board[a+8] =='.' or board[a+1] =='.'or board[a+9] =='.'or board[a-8] =='.'or board[a-7] =='.':
                        xfront=xfront+1
                else:
                     if board[a+8] =='.' or board[a-1] =='.'or board[a+7] =='.'or board[a-8] =='.'or board[a-9] =='.':
                        xfront=xfront+1
            elif not iscorner:
                for everything in theway:
                    if(board[a+everything]=='.'):
                        xfront=xfront+1
                        break
            if a in ringofsadge:
                if movescounts <= 52:
                    thedub=thedub - rsad
            
        elif board[a]=='o':
            ocount=ocount+1
            # if xcount > 15:
            #     thedub=thedub - 2
            # else:
            #     thedub = thedub+2
            for z in corners_dict:
                if z==a:
                    iscorner=True
                    if token =='o':
                        thedub=thedub-wcorner
                    else:
                        thedub=thedub-lcorner
                    ostable.append(z)
                    for frontierthing in corners_dict[a]:
                        if(board[frontierthing]=='.'):
                            ofront=ofront+1
                            break
                    break
                elif a in corners_dict[z] and board[z] == '.':
                    thedub = thedub+badge
                    
                    break
                # elif a in cornerss_dict[z] and board[z] == '.':
                #     thedub = thedub-badgee
                #     break
            if a in edges:
                thedub=thedub-edgee
                if a//8==0:
                    if board[a-1] =='.' or board[a+1] =='.'or board[a+7] =='.'or board[a+8] =='.'or board[a+9] =='.':
                        ofront=ofront+1
                elif a//8 == 7:
                    if board[a-1] =='.' or board[a+1] =='.'or board[a-7] =='.'or board[a-8] =='.'or board[a-9] =='.':
                        ofront=ofront+1
                elif a%8==0 :
                    if board[a+8] =='.' or board[a+1] =='.'or board[a+9] =='.'or board[a-8] =='.'or board[a-7] =='.':
                        ofront=ofront+1
                else:
                     if board[a+8] =='.' or board[a-1] =='.'or board[a+7] =='.'or board[a-8] =='.'or board[a-9] =='.':
                        ofront=ofront+1
            elif not iscorner:
                for everything in theway:
                    if(board[a+everything]=='.'):
                        ofront=ofront+1
                        break
            if a in ringofsadge:
                if movescounts <=52:
                    thedub=thedub + rsad
    goodmult = 1.5
    badmult = 3.5
    for a in xstable:
        stability=0
        if a == 0:
            height = 0
            prevrow = 7
            while height < 64 and board[height] == 'x':
                row = 0
                while(prevrow >=row and board[row + height] == 'x'):
                    row = row + 1
                    stability = stability+1
                # if row == 8 and height == 0:
                #     xstable.remove(7)
                prevrow = row-1
                height = height +8
                
            # if height == 64:
            #  xstable.remove(56)
            if token == 'x':
                thedub=thedub + int(stability*goodmult)
            else:
                thedub=thedub + int(stability*badmult)
            # sscore = sscore + int(stability*0.95)
        elif a == 7:
            height = 7
            prevrow = 7
            while height < 64 and board[height] == 'x':
                row = 0
                while(prevrow >=row and board[-row + height ] == 'x' ):
                    row = row + 1
                    stability = stability+1
                # if row == 8 and height==0:
                #     xstable.remove(0)
                prevrow = row-1
                height = height +8
            # if height == 64:
            #     xstable.remove(63)
            if token == 'x':
                thedub=thedub + int(stability*goodmult)
            else:
                thedub=thedub + int(stability*badmult)
            # sscore = sscore + int(stability*0.95)
        elif a == 56:
            height = 56
            prevrow = 7
            while height > -1 and board[height] == 'x' :
                row = 0
                while(prevrow >=row and board[row + height] == 'x' ):
                    row = row + 1
                    stability = stability+1
                prevrow = row-1
                height = height -8
            if token == 'x':
                thedub=thedub + int(stability*goodmult)
            else:
                thedub=thedub + int(stability*badmult)
            # sscore = sscore + int(stability*0.95)
        elif a == 63:
            height = 63
            prevrow = 7
            while height >-1 and board[height] == 'x' :
                row = 0
                while( prevrow >=row and board[-row + height] == 'x' ):
                    row = row +1
                    stability = stability+1
                prevrow = row-1
                height = height -8
            if token == 'x':
                thedub=thedub + int(stability*goodmult)
            else:
                thedub=thedub + int(stability*badmult)
            # sscore = sscore + int(stability*0.95)
    for a in ostable:
        stability=0
        if a == 0:
            height = 0
            prevrow = 7
            while height < 64 and board[height] == 'o':
                row = 0
                while(prevrow >=row and board[row + height] == 'o' ):
                    row = row + 1
                    stability = stability+1
                # if row == 8 and height ==0:
                #     xstable.remove(7)
                prevrow = row-1
                height = height +8
                
            # if height == 64:
            #     xstable.remove(56)
            if token == 'x':
                thedub=thedub - int(stability*badmult)
            else:
                thedub=thedub - int(stability*goodmult)
            # sscore = sscore - int(stability*0.95)
        elif a == 7:
            height = 7
            prevrow = 7
            while height < 64 and board[height] == 'o':
                row = 0
                while(prevrow >=row and board[-row + height] == 'o' ):
                    row = row + 1
                    stability = stability+1
                # if row == 8 and height ==0:
                #     xstable.remove(0)
                prevrow = row-1
                height = height +8
            # if height == 64:
            #     xstable.remove(63)
            if token == 'x':
                thedub=thedub - int(stability*badmult)
            else:
                thedub=thedub - int(stability*goodmult)
            # sscore = sscore - int(stability*0.95)

        elif a == 56:
            height = 56
            prevrow = 7
            while height > -1 and board[height] == 'o':
                row = 0
                while(prevrow >=row and board[row + height] == 'o'):
                    row = row + 1
                    stability = stability+1
                prevrow = row-1
                height = height -8
            if token == 'x':
                thedub=thedub - int(stability*badmult)
            else:
                thedub=thedub - int(stability*goodmult)
            # sscore = sscore - int(stability*0.95)

        elif a == 63:
            height = 63
            prevrow = 7
            while height >-1 and board[height] == 'o' :
                row = 0
                while(prevrow >=row and board[-row + height] == 'o' ):
                    row = row + 1
                    stability = stability+1
                prevrow = row-1
                height = height -8
            if token == 'x':
                thedub=thedub - int(stability*badmult)
            else:
                thedub=thedub - int(stability*goodmult)
            # sscore = sscore - int(stability*0.95)
    # posible = possible_moves(board,token)
    # thedub = 10 * len(posible) 
    movecount = 0
    moveecount = 0
    ofrontier = 2
    mfrontier= 1
    efrontier= 0
    endfrontier = 0
    emult=2
    eemult=4
    if(token == 'x'):
        movecount = len(possible_moves(board,'x'))
        moveecount = len(possible_moves(board,'o'))
        if movescounts <= 16:
            thedub=thedub+10*movecount - 11 * moveecount
            thedub = thedub - ofrontier *xfront + ofrontier*ofront
        elif movescounts <=46:
            thedub=thedub+8*movecount - 9 * moveecount
            thedub = thedub - mfrontier *xfront +mfrontier*ofront
        elif movescounts <= 62:
            thedub=thedub+8*movecount - 9 * moveecount
            thedub = thedub + 2 *xcount - 2*ocount
            thedub = thedub - efrontier *xfront +efrontier*ofront
        else: 
            thedub=thedub+7*movecount - 8 * moveecount
            thedub = thedub + 4 *xcount - 4*ocount
        if movecount == 0:
            if len(possible_moves(board,'o'))==0:
                if(xcount>ocount):
                    thedub=1e6 + 10*(xcount-ocount)
                elif xcount<ocount:
                    thedub=-1e6+10*(xcount-ocount)
            else:
                thedub=thedub-100
    else:
        movecount = len(possible_moves(board,'o'))
        moveecount = len(possible_moves(board,'x'))
        if movescounts <=16:
            thedub=thedub-10*movecount + 11*moveecount
            thedub = thedub +ofrontier *ofront - ofrontier *xfront
        elif movescounts <=46:
            thedub=thedub-8*movecount + 9 * moveecount
            thedub = thedub +mfrontier *ofront -mfrontier*xfront
        elif movescounts <= 62:
            thedub=thedub-8*movecount  + 9 * moveecount
            thedub = thedub - 2 *ocount +2*xcount
            thedub = thedub - efrontier *xfront +efrontier*ofront
        else:
            thedub=thedub-7*movecount  + 8 * moveecount
            thedub = thedub - 4 *ocount +4*xcount
        if movecount == 0:
            if len(possible_moves(board,'x'))==0:
                if(xcount>ocount):
                    thedub=1e6 + 10*(xcount-ocount)
                elif xcount<ocount:
                    thedub=-1e6+10*(xcount-ocount)
            else:
                thedub=thedub + 50
    
    return thedub
def max_step(board,depth,lim,alpha,beta):
    if depth==lim:
        return score(board,'x')
    results = list()
    for next_board in (possible_moves(board, 'x')):
        r=min_step(make_move(board,'x',next_board),depth+1,lim,alpha,beta)
        results.append(r)
        alpha = max(alpha,r)
        if alpha>=beta:
            break
    if len(results) ==0:
        return score(board,'x') 
    return max(results)
def min_step(board,depth,lim,alpha,beta):
    if depth==lim:
        return score(board,'o') 
    results = list()
    for next_board in (possible_moves(board, 'o')):
        r=max_step(make_move(board,'o',next_board),depth+1,lim,alpha,beta)
        results.append(r)
        beta = min(beta,r)
        if alpha>=beta:
            break
    if len(results) ==0:
        return score(board,'o') 
    return min(results)
# openings = {
#     "..........................xxx......xo...........................": 18,
#     "..................o.......xox......xo...........................": 19,  
#     "..................ox......xxx......xo...........................": 34, 
#     "..................ox......oxx.....ooo..........................." : 43,
#     "..................ox.....xxxx.....ooo..........................." : 11,
#     "...........o......oo.....xxox.....ooo..........................." : 43,
#     "..................ox......oxx.....oxo......x...................." : 29,
#     "..................ox......oooo....oxo......x...................." : 37,
#     "..................ox......ooxo....oxxx.....x...................." : 11,
#     "..........................xxx.....ooo...........................": 43,
#     "....................o.....xxo......xo...........................": 45,
#     "....................o.....xxo......xxx..........................": 25,
#     "....................o.....xxo......xx........x..................": 44,
#     "....................o.....xxo......xo.......ox.................." : 37,
#     "....................o.....xxo......xxx......ox.................." : 34,
#     "....................o.....xoo.....oxxx......ox.................." : 29,
#     "....................o.....xxxx....oxxx......ox.................." : 46,
#     "....................o.....xxxx....oxxx......ooo................." : 53,
#     "....................o.....xxxx....oxxx......xxo......x.........." : 19,
#     '...........................ox......xxx..........................':45,
# '...................x.......xx......xo...........................':18,
# '...........................ox......xx.......x...................':49,
# '...........................ox......xox.......o..................':44,
# '..................ox.......ox......xo...........................':26,
# '...........................ox......xo.......xo..................':41,
# '...........................ox......xxx......xo..................':29,
# '..................ox......xxx......xo...........................':20,
# '...........................ox......xxx......xo..................':51,
# '...........................ooo.....xxo......xo..................':20,
# '..................ooo.....xxo......xo...........................':29,
# '...........................ox......oxx.....ooo..................':44,
# '...........................ooo.....xxxx.....xo..................':52,
# '...........x......oxo.....xxo......xo...........................':25,
# '...........................ox......oxx.....oxo......x...........':40,
# '...........................ooo.....xoxx.....oo......o...........':20,
# '...........x......oxo....oooo......xo...........................':29,
# '...........................ox......oooo....oxo......x...........':44,
# '....................x......oxo.....xxo......xo..................':34,
# '..................ooo.....xxxx.....xo...........................':43,
# '...........................ox.....xxxx.....ooo..................':26,
# '....................x......oxo....oooo......xo..................':26,
# '..................ooo.....xoxx.....oo......o....................':44,
# '....................o......oo.....xxox.....ooo..................':27,
# '....................x.....xxxo....oxoo......xo..................':52,
# '..................ooo.....xoxx.....xx......ox...................':25,
# '...................xo......xx.....xxox.....ooo..................':40,
# '...........................ooo.....xxx..........................':20,
# '...................xo......xo......xo...........................':29,
# '...........................ox......ox......ox...................':44,
# '...........................ox......oxx.....o....................':18,
# '...................x.......xx.....ooo...........................':45,
# '...........................ooo.....xx.......x...................':28,
# '..........................xxx......oxx.....o....................':38,
# '...................x.......xx.....oox.......x...................':11,
# '...................x.......xoo.....xx.......x...................':58,
# '..................x........xx......oxx.....o....................':19,
# '...................x.......xx.....oox........x..................':37,
# '..................x........xoo.....xx.......x...................':36,
# '..................xo.......ox......oxx.....o....................':26,
# '...................x.......xx.....oooo.......x..................':44,
# '..................x.......oooo.....xx.......x...................':27,
# '..................xo......xxx......oxx.....o....................':29,
# '...................x.......xx.....ooxo......xx..................':20,
# '..................xx......oxoo.....xx.......x...................':51,
# '..................xo......xxxo.....oox.....o....................':34,
# '...................xo......ox.....ooxo......xx..................':43,
# '..................xx......oxoo.....xo......ox...................':26,
# '..................xo......xxxo....xxxx.....o....................':17,
# '...................xo......xx.....oxxo.....xxx..................':53,
# '..................xxx.....oxxo.....xx......ox...................':20,
# '.................ooo......xxxo....xxxx.....o....................':10,
# '...................xo......xx.....oxxo.....xxo.......o..........':46,
# '..........o.......oxx.....oxxo.....xx......ox...................':29,
# '..........x......oxx......xxxo....xxxx.....o....................':44,
# '...................xo......xx.....oxxx.....xxxx......o..........':26,
# '..........o......xxxx.....xxxo.....xx......ox...................':41,
    # }

def find_next_move(board,player,depth):
    # if board in openings:
    #     return openings[board]
    bo=board
    scores = 0
    move = None
    if player == 'o':
        scores = 1e9
        for b in possible_moves(bo,player):
            z=make_move(bo,player,b)
            l=max_step(z,1,depth+3 , -1e9, 1e9)
            if scores >l:
                scores=l
                move = b
    else:
        scores = -1e9
        for b in possible_moves(bo,player):
            z=make_move(bo,player,b)
            l=min_step(z,1,depth+3,-1e9, 1e9)
            if scores <l:
                scores=l
                move = b
    return move
results = []
board = sys.argv[1]
# board = "x.xxxx..oxoooo..ooooo...oooooo..ooooo.."
player = sys.argv[2]
# player = 'x'
depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

   print(find_next_move(board, player, depth))

   depth += 1
