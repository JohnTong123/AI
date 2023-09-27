from sys import argv
import ast
import numpy as np
import matplotlib.pyplot as plt
import random
import math
def truth_table(bits, n):
    truth = {}
    first = [1]*bits
    count=2**(2**bits-1)
    nnn = n 
    for everything in range(2**bits):
        if nnn >= count:
            truth[tuple(first)]  = 1
            nnn=nnn-count
        else:
            truth[tuple(first)]  = 0
        if not first == [0]*bits:
            track = 0
            for x in range(bits-1,-1,-1):
                if first[x] == 1:
                    track =x
                    break
            for y in range(track+1,bits):
                first[y] = 1
            first[track]=0
        count=count/2
    return(truth)
def pretty_print(table):
    
    for a in table:
        vals = ""
        for aa in a:
            vals=vals + str(aa) + " "
        vals=vals+ "| "
        vals = vals + str(table[a])
        print(vals)
def step(num):
    if num>0:
        return 1
    else:
        return 0
# write code to correctly model a step function (make sure to return an int)
def sigmoid(num):
    return 1/(1+math.exp(-num))
def perceptron(A, w, b, x):
    total = 0
    for aa in range(len(w)):
        total = total + w[aa] * x[aa]
    total=total+b
    return A(total)
# write code to correctly model a perceptron
# import ast
# x = "(1, 2, 3, 4, 5)"
# t = ast.literal_eval(x)
# print(t, type(t))
def check(n, w, b):
    c=0
    # print("a")
    x=truth_table(len(w),n)
    # print(x)
    for all in x.keys():
        # print(all)
        # print(perceptron(step, w, b, all) )
        if perceptron(step, w, b, all) == x[all]:
            c=c+1
    return c/(2**len(w))
def themath(weight,bias,x,y):
    learning = 1
    f= perceptron(step,tuple(weight),bias,x)
    ww=[]
    for everything in range(len(weight)):
        # print(weight)
        ww.append(weight[everything] + (y[x] - f)  * learning * x[everything])
    bb = bias + (y[x] - f) * learning 
    return((ww,bb))

def epochbits(x):
    
    matches = 0
    for pain in range(2**(2**x)):
        startw = [0]*x
        runs = 0
        startb=0
        copyw = []
        copyb = 0
        thetruth = truth_table(x,pain)
        # print(thetruth)
        while runs < 100 and not(startw==copyw and startb==copyb):
            copyw=startw.copy()
            copyb=startb
            for everyrow in thetruth.keys():
                d = themath(startw, startb, everyrow,thetruth.copy())
                startw=d[0]
                startb=d[1]
            runs=runs+1
        if check(pain,tuple(startw),startb)==1.0:
            matches = matches+1
    return  matches 
def epoch(bits,canonical):
    startw = [0]*bits
    runs = 0
    startb=0
    copyw = []
    copyb = 0
    thetruth = truth_table(bits,canonical)
    # print(thetruth)
    while runs < 100 and not(startw==copyw and startb==copyb):
        copyw=startw.copy()
        copyb=startb
        for everyrow in thetruth.keys():
            d = themath(startw, startb, everyrow,thetruth.copy())
            startw=d[0]
            startb=d[1]
        runs=runs+1
    return(startw,startb, check(canonical,tuple(startw),startb))

# print(epochbits(4))
#104
# print(epoch(int(argv[1]),int(argv[2])))

# print(epochbits(4))
# pretty_print(truth_table(2,9))

# print(check(int(argv[1]),ast.literal_eval(argv[2]),float(argv[3])))

# print(perceptron(step, (1,1), -1.5, (1,1)))
def p3(x):
    l=perceptron(step, (-1,-1),1,x) 
    ll = perceptron(step, (1,1),-1,x)
    lll = perceptron(step,(-1,-1),1,(l,ll))
    return(lll)
def graph(x,b,end):
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    for xvals in range(-20,21,1):
        for yvals in range(-20,21,1):
            if not (( xvals  ==10 or xvals==0) and (yvals==0 or yvals==10)):
                l=perceptron(sigmoid,x,b,((xvals/10),(yvals/10)))
                if l >0.5:
                    plt.plot((xvals/10), (yvals/10), marker="o", markersize=5,c="green")
                else:
                    plt.plot((xvals/10), (yvals/10), marker="o", markersize=5, c="red")
    for every in end:
        if end[every] ==1:
            plt.plot(every[0], every[1], marker="o", markersize=10, c="green")
        else:
            plt.plot(every[0], every[1], marker="o", markersize=10, c="red")
    plt.show()
def p_net(A,x,w,b):
    new_f = np.vectorize(A)
    azero = x
    for each in range(1,len(w)):
        # print(w[each])
        # print(azero@w[each])
        # print(b[each])
        azero = new_f(azero@w[each]+b[each])
    return azero
# print(p3(ast.literal_eval(argv[1])))
# aaa= np.array([[1,1],[1,0],[0,1],[0,0]])  
# aaaa= [None, np.array([[1, -1], [1, -1]]),np.array([[-1],[ -1]])]
# aaaaa = [None,np.array([[-1,1]]),np.array([[1]])]

# print(p3(ast.literal_eval(argv[1])))
# aaa= np.array([[0.5,0.49]])

# print(p_net(step,aaa,aaaa,aaaaa))
# print(p_net(sigmoid,aaa,aaaa,aaaaa))
# graph((-0.5,-0.5),1.3,truth_table(2,1))
# graph((0.5,-0.5),0.5,truth_table(2,1))
# graph((-0.5,0.5),0.5,truth_table(2,1))
# graph((0.5,0.5),0.5,truth_table(2,1))
big = 0
track = 0
# for idk in range (-100,100,1):
    # dep=idk/10
# aaaaa = [None,np.array([[0.9,0.9]]),np.array([[-1.75]])]
avg=0
 
if len(argv) == 2: #XOR HAPPENS HERE
    aaa= np.array([[ast.literal_eval(argv[1])]])
    aaaa= [None, np.array([[1, -1], [1, -1]]),np.array([[-1],[ -1]])]
    aaaaa = [None,np.array([[-1,1]]),np.array([[1]])]
    print(p_net(step,aaa,aaaa,aaaaa))
elif len(argv)==3:
    
    aaa= np.array([[float(argv[1]),float(argv[2])]])
    aaaa= [None, np.array([[-1, 1,-1,1], [-1, 1,1,-1]]),np.array([[1],[1],[1],[1]])]
    aaaaa = [None,np.array([[1,1,1,1]]),np.array([[-3]])]
    print(p_net(step,aaa,aaaa,aaaaa))
else:
    wrong = []
    correct=0
    aaaa= [None, np.array([[-1, 1,-1,1], [-1, 1,1,-1]]),np.array([[1],[1],[1],[1]])]
    aaaaa = [None,np.array([[0.9,0.9,0.9,0.9]]),np.array([[-2.7]])]
    for b in range(0,500):
        xvals = random.random() *2 - 1
        yvals = random.random() *2 -1
        idk = p_net(sigmoid,np.array([[xvals,yvals]]),aaaa,aaaaa)
        # print(idk)
        # print((xvals,yvals))
        if xvals**2 + yvals**2 <1 and idk >0.5:
            correct=correct+1
        elif  xvals**2 + yvals**2 >1 and idk <0.5:
            correct=correct+1 
        else:
            wrong.append((xvals,yvals))
    print(100*correct/500)
    print(wrong)
# print(len(argv))