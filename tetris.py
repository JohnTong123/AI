from cmath import sqrt
import sys
import random
# boardd=sys.argv[1]
# boardd = "XXXXXXXXXX#XXXXXXXXX#XXXXXXXXX#XXXXXX#XX#XXXXXX#XX#XXXXXX#XX#XXXXX##XX#XXXXX##XX#XXXXX##X##XXXXX##X#####XX########XX#########X#########X#########X#########X##########X####X#X#X#X#X#####X###XXX########"
boardd = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
piecedict = {}
piecedict[0] = [(0,0,0,0),(0,)] # STIK
piecedict[1] = [(0,0)]          # SQUAR
piecedict[2] = [(0,-1),(-1,0,-0)]   # Z
piecedict[3] = [(-1,0),(0,0,-1)]   #S
piecedict[4] = [(0,0,0),(0,0),(0,-2),(-1,-1,0)] #L REVERSE REVERSE
piecedict[5] = [(0,0,0),(0,0),(-2,0),(0,-1,-1)]  #L   D:
piecedict[6] = [(0,0,0),(0,-1),(-1,0),(-1,0,-1)] #T
# print(piecedict[0])
# boarddict = {}
# if "#" not in boardd:
#     boarddict[0] = 0
#     boarddict[1] = 0
#     boarddict[2] = 0
#     boarddict[3] = 0
#     boarddict[4] = 0
#     boarddict[5] = 0
#     boarddict[6] = 0
#     boarddict[7] = 0
#     boarddict[8] = 0
#     boarddict[9] = 0
# else:
#     boarddict[0] = 0
#     boarddict[1] = 0
#     boarddict[2] = 0
#     boarddict[3] = 0
#     boarddict[4] = 0
#     boarddict[5] = 0
#     boarddict[6] = 0
#     boarddict[7] = 0
#     boarddict[8] = 0
#     boarddict[9] = 0
#     for abcde in range(0,10):
#         found=True
#         for aa in range(0,20):
#             if boardd[aa * 10 + abcde] == "#":
#                 boarddict[abcde] = 20-aa
#                 found=False
#                 break
# # print(boarddict)
filething = open("tetrisouttt.txt" , "w")

ffthing = open("ttt.txt","w")
ffffffthing = open("tttt.txt","w")
def printboard(board):
    for a in range(0,200,10):
        print(board[a:a+10])
    print("")
def findavailable(board, p,heightdict):

    boardheights=heightdict.copy()
    piece=int(p)
    boardlist = []
    for a in range(0,10):

        for aa in range(len(piecedict[piece])):
            b=""
            boardheights=heightdict.copy()

            height = 0
            skore = 0
            numline = 0
            for aaa in range(len(piecedict[piece][int(aa)])):
                if(a+aaa < 10):
                    if boardheights[a+aaa] +piecedict[piece][aa][aaa]  > height:
                        height = boardheights[a+aaa] +piecedict[piece][aa][aaa]
                        # print(boarddict[a+aaa])
            sadge = "gg"
            if piece == 0 and aa == 1:
                if height <17:
                    b= board[0:200 - (height +4) * 10 +a ]+ "#"+board[200 - (height +4) * 10 +a +1 :200 - (height +3) * 10 +a ]+"#"+board[200 -(height +3) * 10 +a +1 :200 -
                    (height +2) * 10 +a ]+"#"+board[200 - (height +2) * 10 +a +1 :200 - (height +1) * 10 +a ] +"#"+board[200 - (height +1) * 10 +a +1 :200]

                    if b[200-(height+4)*10:200-(height+3)*10] == "##########":
                        b="          " +b[0:200-(height+4)*10] + b[200-(height+3)*10:200]
                        # print("a")
                        numline=numline+1
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                        numline=numline+1
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        numline=numline+1
                    boardheights[a] = height+4
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
                
            elif piece == 0 and aa == 0  and a<7:
                if height < 20:
                    b= board[0:200 - (height+1) * 10 +a] + "####" + board[200-(height+1) * 10 +a+4:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                    boardheights[a] = height+1
                    boardheights[a+1] = height+1
                    boardheights[a+2] = height+1
                    boardheights[a+3] = height+1
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece ==1 and a<9:
                if height<19:
                    b=board[0:200 - ((height+2) * 10) +a] + "##" + board[200-((height+2) * 10) +a+2:200 - ((height+1) * 10) +a]+ "##" + board[200-((height+1) * 10)+2 +a:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+2
                    boardheights[a+1] = height+2
                    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 2 and aa == 0 and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a+1] + "#" + board[200 - (height+3) * 10 +a+2:200 - (height+2) * 10 +a] + "##"+ board[200 - 
                    (height+2) * 10 +a+2:200 - (height+1) * 10 +a] + "#"+ board[200 - (height+1) * 10 +a+1:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+2
                    boardheights[a+1] = height+3
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 2 and aa == 1 and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a] + "##" + board[200 - (height+2) * 10 +a+2:200 - (height+1) * 10 +a+1] + "##"+ board[200 - (
                    height+1) * 10 +a+3:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+2
                    boardheights[a+1] = height+2
                    boardheights[a+2] = height+1
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 3 and aa == 0  and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a] + "#" + board[200 - (height+3) * 10 +a+1:200 - (height+2) * 10 +a] + "##"+ board[200 - 
                    (height+2) * 10 +a+2:200 - (height+1) * 10 +a+1] + "#"+ board[200 - (height+1) * 10 +a+2:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height +3
                    boardheights[a+1] = height+2
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 3 and aa == 1 and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a+1] + "##" + board[200 - (height+2) * 10 +a+3:200 - (height+1) * 10 +a+0] + "##"+ board[200 - (
                    height+1) * 10 +a+2:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+1
                    boardheights[a+1] = height+2
                    boardheights[a+2] = height+2
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 4 and aa == 0  and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a] + "#" + board[200 - (height+2) * 10 +a+1:200 - (height+1) * 10 +a+0] + "###"+ board[200 - (
                    height+1) * 10 +a+3:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+2
                    boardheights[a+1] = height+1
                    boardheights[a+2] = height+1
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 4 and aa == 1  and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a+1] + "#" + board[200 - (height+3) * 10 +a+2:200 - (height+2) * 10 +a+1] + "#"+ board[200 - (
                    height+2) * 10 +a+2:200 - (height+1) * 10 +a] + "##" + board[200 - (height+1) * 10 +a+2:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                    boardheights[a] = height+1
                    boardheights[a+1] = height+3
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 4 and aa == 3 and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a] + "###" + board[200 - (height+2) * 10 +a+3:200 - (height+1) * 10 +a+2] + "#"+ board[200 - (
                    height+1) * 10 +a+3:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height+2
                    boardheights[a+1] = height+2
                    boardheights[a+2] = height+2
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 4 and aa == 2  and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a] + "##" + board[200 - (height+3) * 10 +a+2:200 - (height+2) * 10 +a+0] + "#"+ board[200 - (
                    height+2) * 10 +a+1:200 - (height+1) * 10 +a] + "#" + board[200 - (height+1) * 10 +a+1:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                        numline=numline+1
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                        numline=numline+1
                    boardheights[a] = height+3
                    boardheights[a+1] = height+3
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 5 and aa == 0 and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a+2] + "#" + board[200 - (height+2) * 10 +a+3:200 - (height+1) * 10 +a+0] + "###"+ board[200 - (
                    height+1) * 10 +a+3:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height+1
                    boardheights[a+1] = height+1
                    boardheights[a+2] = height+2
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 5 and aa == 1 and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a] + "#" + board[200 - (height+3) * 10 +a+1:200 - (height+2) * 10 +a] + "#"+ board[200 - (
                    height+2) * 10 +a+1:200 - (height+1) * 10 +a] + "##" + board[200 - (height+1) * 10 +a+2:200]
                    
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 3
                    boardheights[a+1] = height + 1    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 5 and aa == 3 and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a] + "###" + board[200 - (height+2) * 10 +a+3:200 - (height+1) * 10 +a] + "#"+ board[200 - (
                    height+1) * 10 +a+1:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        numline=numline+1
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 2
                    boardheights[a+1] = height + 2    
                    boardheights[a] = height + 2
                    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 5 and aa == 2  and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a] + "##" + board[200 - (height+3) * 10 +a+2:200 - (height+2) * 10 +a+1] + "#"+ board[200 - (
                    height+2) * 10 +a+2:200 - (height+1) * 10 +a+1] + "#" + board[200 - (height+1) * 10 +a+2:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 3
                    boardheights[a+1] = height + 3    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 6 and aa == 0  and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a+1] + "#" + board[200 - (height+2) * 10 +a+2:200 - (height+1) * 10 +a] + "###"+ board[200 - (
                    height+1) * 10 +a+3:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 1
                    boardheights[a+1] = height + 2
                    boardheights[a+2] = height + 1
                    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 6 and aa == 1 and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a] + "#" + board[200 - (height+3) * 10 +a+1:200 - (height+2) * 10 +a] + "##"+ board[200 - (
                    height+2) * 10 +a+2:200 - (height+1) * 10 +a] + "#" + board[200 - (height+1) * 10 +a+1:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 3
                    boardheights[a+1] = height + 2
                    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 6 and aa == 2  and a<9:
                if height<18:
                    b= board[0:200 - (height+3) * 10 +a+1] + "#" + board[200 - (height+3) * 10 +a+2:200 - (height+2) * 10 +a] + "##"+ board[200 - (
                    height+2) * 10 +a+2:200 - (height+1) * 10 +a+1] + "#" + board[200 - (height+1) * 10 +a+2:200]
                    if b[200-(height+3)*10:200-(height+2)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+3)*10] + b[200-(height+2)*10:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    
                    boardheights[a] = height + 2
                    boardheights[a+1] = height + 3
                    
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            elif piece == 6 and aa == 3  and a<8:
                if height<19:
                    b= board[0:200 - (height+2) * 10 +a] + "###" + board[200 - (height+2) * 10 +a+3:200 - (height+1) * 10 +a+1] + "#"+ board[200 - (
                    height+1) * 10 +a+2:200]
                    if b[200-(height+2)*10:200-(height+1)*10] == "##########":
                        # #for everything in boardheights.keys():
                            ##boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+2)*10] + b[200-(height+1)*10:200]
                    if b[200-(height+1)*10:200-(height)*10] == "##########":
                        # #for everything in boardheights.keys():
                            #boardheights[everything] = boardheights[everything]-1
                        numline=numline+1
                        b="          " +b[0:200-(height+1)*10] + b[200-(height)*10:200]
                    boardheights[a] = height + 2
                    boardheights[a+1] = height + 2
                    boardheights[a+2] = height + 2
                else:
                    sadge="ff"
                    # filething.write("GAME OVER" + "\n")
            
            # print(height)
            if numline ==1:
                # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                skore=40
            elif numline ==2:
                # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                skore=100
            elif numline==3:
                skore=300
                # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            elif numline==4:
                skore=1200
                # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            # for everything in boardheights.keys():
            #     boardheights[everything] = boardheights[everything] - numline
            if not numline  == 0:
                for abcdef in range(0,10):
                    for laa in range(boardheights[abcdef],0,-1):
                        if b[200-(laa * 10) + abcdef] == "#":
                            boardheights[abcdef] = laa
                            break
            if not len(b) ==0:
                # for k in range(0,200,10):
                #     filething.write(b[k:k+10] + "\n")
                # filething.write("\n")
                # print(numline)
                # filething.write(str(boardheights)+"\n")
                boardlist.append((sadge,b,skore,boardheights))
           
    return (boardlist)
# # printboard(boardd)
# for blocks in range(0,7):
#     findavailable(boardd,blocks)
# printboard(boardd)
def heuristic(board,heights,strategy,scores):
    # print(strategy)
    # if len(strategy)>3:
    #     print(strategy)
    # print(strategy)
    waa,b,c,d,e,f,g = strategy
    # print(c)
    valuee=0
    height=0
    theight = 0
    smol =20
    # f=0
    numhole = 0
    count=0
    rough = 0
    rtrans=0
    for aaa in range(len(heights)):
        if aaa < 9:
            rough = rough + abs(heights[aaa] -heights[aaa+1])
            if heights[aaa] < heights[aaa+1]:
                rtrans+=1 
        height = max(height,heights[aaa])
        theight=theight + heights[aaa]
        smol=min(smol,heights[aaa])
        w=heights[aaa]
        while w>0:
            if board[200-10*(w)+count]==" ":
                numhole=numhole+1
            w=w-1
        count=count+1
    count=0
    # filething.write(str(valuee)+ "\n")
    valuee = valuee + waa*(rough)#rough
    # filething.write(str(valuee)+"  " +str(theight) +"\n")
    valuee=valuee+f*theight
    # filething.write(str(valuee)+ "\n")
    valuee = valuee + e*(height)
    # filething.write(str(valuee)+ "marker"+ "    " + str(c)+"\n")
    valuee=valuee + c* (numhole)*numhole
    # filething.write(str(valuee)+"   " + str(numhole) +"NUMSSS??"+"\n" )
    valuee=valuee + b* smol
    # filething.write(str(valuee)+ "\n") 

    valuee=valuee + g*rtrans
    # filething.write(str(valuee)+ "\n") 
    # valuee = valuee +scores* d
    if scores == 40: 
        valuee =valuee + 1*d
    if scores == 100: 
        valuee =valuee + 2*d
    if scores == 300: 
        valuee =valuee + 3*d
    if scores == 1200: 
        valuee =valuee + 4*d
    # filething.write(str(valuee)+ "\n")
    # filething.write("\n")

    return valuee
def printplay(strategy):
    board = " "*200
    boardheights = {}
    boardheights[0]=0
    boardheights[1]=0
    boardheights[2]=0
    boardheights[3]=0
    boardheights[4]=0
    boardheights[5]=0
    boardheights[6]=0
    boardheights[7]=0
    boardheights[8]=0
    boardheights[9]=0

    points =0
    gameover="gg"
    
    while gameover=="gg":
        gameover="ff"
        # printboard(board)
        posscore=None
        count=0
        direct = -1
        piece = random.randint(0,6)
        # print(boardheights)
        # print(piece)
        # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        avb = findavailable(board, piece,boardheights.copy())
        heu=0
        # print(avb,"\n")
        # print("hi")
        for a in avb:
            heu=0

            # print("a")
 
            # print(a[0])
            if a[0] == "gg":
                gameover = "gg"
                heu = heuristic(a[1],a[3],strategy.copy(), a[2])
                # filething.write(str(heu) + '\n')
                # filething.write(str(posscore) +"AAAAAAX" + '\n')
                if posscore == None or posscore < heu:
                    # filething.write(str(heu) +"AAAAAA" + '\n')
                    posscore  = heu
                    direct = count  
                    # print("hi")
            
            count=count+1
        # filething.write(str(heu) + '\n')

        if not direct == -1:
            # print("h")
            points=points + avb[direct][2]
            # print(avb[direct][2])
            board = avb[direct][1]
            # print(avb[direct][2])
            # print(boardheights)
            # for lin in range(0,200,10):
            #     filething.write(board[lin:lin+10]+"\n")
            # filething.write("\n")
            boardheights = avb[direct][3].copy()
        printboard(board)
        print("")
            # print(boardheights)
    # print(points)
def playgame(strategy):
    board = " "*200
    boardheights = {}
    boardheights[0]=0
    boardheights[1]=0
    boardheights[2]=0
    boardheights[3]=0
    boardheights[4]=0
    boardheights[5]=0
    boardheights[6]=0
    boardheights[7]=0
    boardheights[8]=0
    boardheights[9]=0

    points =0
    gameover="gg"
    
    while gameover=="gg":
        gameover="ff"
        # printboard(board)
        posscore=None
        count=0
        direct = -1
        piece = random.randint(0,6)
        # print(boardheights)
        # print(piece)
        # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        avb = findavailable(board, piece,boardheights.copy())
        heu=0
        # print(avb,"\n")
        # print("hi")
        for a in avb:
            heu=0

            # print("a")
 
            # print(a[0])
            if a[0] == "gg":
                gameover = "gg"
                heu = heuristic(a[1],a[3],strategy.copy(), a[2])
                # filething.write(str(heu) + '\n')
                # filething.write(str(posscore) +"AAAAAAX" + '\n')
                if posscore == None or posscore < heu:
                    # filething.write(str(heu) +"AAAAAA" + '\n')
                    posscore  = heu
                    direct = count  
                    # print("hi")
            
            count=count+1
        # filething.write(str(heu) + '\n')

        if not direct == -1:
            # print("h")
            points=points + avb[direct][2]
            # print(avb[direct][2])
            board = avb[direct][1]
            # print(avb[direct][2])
            # print(boardheights)
            # for lin in range(0,200,10):
            #     filething.write(board[lin:lin+10]+"\n")
            # filething.write("\n")
            boardheights = avb[direct][3].copy()
            # printboard(board)
            # print(boardheights)
    # print(points)
    return points
def fitness_function(strategy):
    num_trials=5
    # print("a")
    game_scores = []
    for count in range(num_trials):
        game_scores.append(playgame(strategy))
    # print(game_scores)
    return sum(game_scores)/len(game_scores)
def genvars(num):
    parents = []
    for a in range(num):
        bob= []
        bob.append(2*random.random()-1)
        bob.append(2*random.random()-1)
        bob.append(random.random()*-1)
        bob.append(abs(random.random()))
        bob.append(2*random.random()-1)
        bob.append(2*random.random()-1)
        bob.append(2*random.random()-1)
        # bob.append(2*random.random()-1)
        parents.append(bob)
    return parents
def rundathing(n,clone,tz,twin,crossover,mut):
    load = input("Load L or Play P")
    avg = []
    parentes=[]
    parents=[]
    if load == "P":
        parents=genvars(n)
    if load == "L":
        with open(input("Filename:")) as ffff:
                inputthing=  [line.strip() for line in ffff]
        for zathing in range(0,len(inputthing),2):
            prev =[]
            zzathing = inputthing[zathing+1].split(", ")
            for zzzathing in range(len(zzathing)):
                if zzzathing == 0:
                    prev.append(float(zzathing[zzzathing][1:len(zzathing[zzzathing])]))
                elif zzzathing == len(zzathing)-1:
                    prev.append(float(zzathing[zzzathing][0:len(zzathing[zzzathing])-1]))
                else:
                    prev.append(float(zzathing[zzzathing]))
            parents.append(prev)
            parentes.append((float(inputthing[zathing]),prev))
            avg.append(float(inputthing[zathing]))
            # print(avg)
    
    # print(parents)

    inputtthing = input("Watch W, Save S, or Continue C")
    while not inputtthing == "S":
    # ppparents= []
        
        if inputtthing == "C":
            if load == "P" :
                parentes=[]
                avg=[]
                cccount=0
                for a in parents:
                # print("a")
                    x=fitness_function(a)
                    avg.append(x)

                    print("strat", cccount, ">", x)
                    parentes.append((x,a))
                # print(a)
                # print(parentes)
                # filething.write(str(x) + "  " +str(a)+"\n")
                    cccount=cccount+1
            load = "P"
            rankings = []
            select=[]
            # filething.write("\n")
            
            parentes.sort(key=lambda x:x[0],reverse=True)

            parentssnext = []
            for randomthingy in range(clone):
                parentssnext.append(parentes[randomthingy][1])
                # ppparents.append(parentes[randomthingy])
            for remainingpop in range(0,n-clone):
                tournament1=[]
                tournament2=[]
                pparents = parentes.copy()
                combotourney= random.sample(pparents,2*tz)
                
                # print(combotourney)
                for thebig in range(len(combotourney)):
                    if thebig<len(combotourney)/2:
                        tournament1.append(combotourney[thebig])
                    else:
                        tournament2.append(combotourney[thebig])
                tournament1.sort(key=lambda x:x[0],reverse=True)
                # for a in tournament1:
                #     ffthing.write(str(a)+"\n")
                tournament2.sort(key=lambda x:x[0],reverse=True)
                # for a in tournament2:
                #     ffthing.write(str(a)+"\n")
                t1 = {  }
                t2 = {}
                for aaaaaaa in range(len(tournament1)-1):
                    if random.random()<twin:
                        t1 = tournament1[aaaaaaa][1]
                        break
                for aaaaaaa in range(len(tournament2)-1):
                    if random.random()<twin:
                        t2 = tournament2[aaaaaaa][1]
                        break
                # ffthing.write(str(t1) + " AAAAAAAA"+"\n")
                # ffthing.write(str(t2) + "\n")
                if len(t1) == 0:
                    t1= tournament1[len[tournament1]-1][1]
                if len(t2) == 0:
                    t2= tournament2[len[tournament2]-1][1]
                alist = [0,1,2,3,4,5,6]
                copyfromp1 = random.sample(alist,crossover)
                baby= t2.copy()
                for babya in copyfromp1:
                    baby[babya]=t1[babya]
                    
                # aalist=alist.copy()
                # for a in [0,1,2,3,4,5]:
                #     if a not in baby.keys():
                #         for aaaa in aalist:
                #             if t2[aaaa] not in baby.values():
                #                 baby[a]=t2[aaaa]
                #                 break
                if random.random()<mut:
                    blah = random.randint(0,6)
                    baby[int(alist[blah])] = baby[int(alist[blah])]  + 0.4*random.random()-0.2
                    # if not (blah==1 and baby[alist[blah]]>-0.25):
                    #     baby[alist[blah]] = baby[alist[blah]]  + 0.5*random.random()-0.25
                    # else:
                    #     baby[alist[blah]] = baby[alist[blah]]  -0.25*random.random()
                    # print(baby)
                    # print(alist[storefront])
                    # print(alist[storeffront]
                # ffthing.write(str(t2) + "\n")
                bruh=[]
                for painconvert in range(len(alist)):
                    bruh.append(baby[painconvert])
                parentssnext.append(baby)
                # ppparents.append((fitness_function(baby),baby))
                
                # ppparents.sort(key=lambda x:x[0],reverse=True)
            parents=parentssnext.copy()
            print(parentes[0][1])
            print(parentes[0][0])
            print(sum(avg)/500)

        # print(parents)
            # print(parentssnext)
        irrelevant = False
        if inputtthing == "W" and len(parentes) == 0:
            avg=[]
            cccount=0
            for a in parents:
            # print("a")
                x=fitness_function(a)
                avg.append(x)

                parentes.append((x,a))
            # print(a)
            # print(parentes)
            # filething.write(str(x) + "  " +str(a)+"\n")
                cccount=cccount+1
        while inputtthing == "W":
            
            printplay(parentes[0][1])
            irrelevant = True
            inputtthing = input("Watch W, Save S, or Continue C")
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # print(decode(l,ppparents[0][1]))
        if not irrelevant:
            inputtthing = input("Watch W, Save S, or Continue C")
        
    savething = open(input("Name of File"),"w")
     
    for everything in range(0,len(parentes),1):
        savething.write(str(parentes[everything][0])+"\n")
        savething.write(str(parentes[everything][1])+"\n")
        
populationsize = 500
numclones=50
tsize=30
tw=0.5
cl=3
multi=0.8
tempdict = {}
tempdict[0] = 0
tempdict[1] = 0
tempdict[2] = 0
tempdict[3] = 0
tempdict[4] = 0
tempdict[5] = 0
tempdict[6] = 0
tempdict[7] = 0
tempdict[8] = 0
tempdict[9] = 0
# print(findavailable(boardd, 0, tempdict))
# printboard(boardd)

# x = findavailable(boardd, 1,boarddict)
# print(x)
# for xx in x:
#     printboard(xx[1])
# print(playgame([-1.1772542361748888, 0.7795200811624339, -0.3238106629991129, 0.5966102118903188, 0.21578607313753229, 0.002476160872875388, 0.5486516587940546]))
# print("f")

rundathing(populationsize,numclones,tsize,tw,cl,multi)