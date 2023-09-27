import sys
final = []
dfa = {}
letters = []
file = sys.argv[1]
# file ="1"
if file[len(file)-4:] == ".txt":
# if not file == "1":
    with open(file) as f:
        vals=[line.strip() for line in f]
    for a in vals[0]:
        letters.append(a)
    c=3
    final = vals[2].split(" ")
    # print(final)
    empty = True
    # print(vals)
    sections = []
    s = []
    for a in range(4,len(vals)):
        if vals[a]=="":
            sections.append(s)
            s=[]
            empty=True
        elif empty == True:
            empty=False
            s.append(vals[a])
        else:
            s.append(vals[a])
    # print(sections)
    for a in sections:
        first = True
        randomthing={}

        for aa in range(1,len(a)):
            
            lesgo = a[aa].split(" ")
            # print(lesgo)
            
            if first:
                randomthing[lesgo[0]]=lesgo[1]
                first=False
            else:
                randomthing[lesgo[0]]=lesgo[1]
            empty = False
        dfa[a[0]]= randomthing
        # print(vals)
    # print(dfa)
else:
    theotherpartthtatididntread =[]
    theotherpartthtatididntread.append(({"0":{"a":"1"},"1":{"a":"2"}, "2":{"b":"3"},"3":{}},["3"], #1
    ["ab", "4", "23", "", "0", "a 1", "", "1", "a 2", "", "2", "b 3", "", "3"]))
    theotherpartthtatididntread.append(({"0":{"1":"0","2":"1","0":"1"},"1":{"1":"0","0":"1","2":"1"}},["0"], #2
    ["012", "2", "0", "", "0", "1 0", "2 1", "0 1", "", "1", "1 0", "0 1", "2 1"]))
    theotherpartthtatididntread.append(({"0":{"a":"0","c":"0","b":"1"},"1":{"a":"1","b":"1","c":"1"}},["1"],#3
    ["abc", "2", "1", "", "0", "a 0", "c 0", "b 1","","1", "a 1", "b 1", "c 1"]))
    theotherpartthtatididntread.append(({"0":{"1":"0","0":"1"},"1":{"1":"1","0":"0"}},["0"],#4
    ["01", "2", "0", "", "0", "1 0", "0 1", "","1", "1 1", "0 0"]))
    theotherpartthtatididntread.append(({"0":{"0":"1","1":"2"},"1":{"0":"0","1":"3"},"2":{"0":"3","1":"0"},"3":{"0":"2","1":"1"}},["0"],#5
    ["01", "4", "0","", "0", "0 1", "1 2", "", "1", "0 0", "1 3","", "2", "0 3", "1 0", "", "3", "0 2", "1 1"]))
    theotherpartthtatididntread.append(({"0":{"a":"1","b":"0","c":"0"},"1":{"a":"1","b":"2","c":"0"},"2":{"a":"0","b":"0","c":"3"},"3":{"a":"3","b":"3","c":"3"}},["0","2","1"], #6
    ["abc", "4", "0 1 2", "", "0", "a 1", "b 0", "c 0","","1", "a 1", "b 2", "c 0","","2", "a 0", "b 0", "c 3", "", "3", "a 3", "b 3", "c 3"]))
    theotherpartthtatididntread.append(({"0":{"0":"0","1":"1"},"1":{"0":"2","1":"0"},"2":{"0":"2","1":"3"},"3":{"0":"2","1":"4"},"4":{"0":"4","1":"4"}},["4"],#7
    ["01", "5", "4", "", "0", "0 0", "1 1","", "1", "0 2", "1 0","","2", "0 2", "1 3","","3", "0 2", "1 4","","4", "0 4", "1 4"]))
    dfa = theotherpartthtatididntread[int(file)-1][0]
    final = theotherpartthtatididntread[int(file)-1][1]
    vals = theotherpartthtatididntread[int(file)-1][2]
    # print(dfa)
def next(letter, node):
    if node not in dfa.keys():
        return False
    if letter not in dfa[node].keys():
        return False
    return dfa[node][letter]

def rundfa(word):
    j="0"
    for a in word:
        if next(a,j) == False:
            return False
        j=next(a,j)
    if j in final:
        return True
    return False
def display():
    row = "*     "
    for a in vals[0]:
        row=row + a + "     "
    print(row)
    for a in range(0,int(vals[1])):
        row = str(a)+ "     "
        for aa in vals[0]:
            # print(a)
            # print(aa)
            if str(a) not in dfa.keys():
                row=row + "_" + "     "
                print(str(a))
            elif str(aa) not in dfa[str(a)].keys():
                row=row + "_" + "     "
            else:
                row=row + dfa[str(a)][aa] + "     "
        print(row)

    


with open(sys.argv[2]) as ff:
# with open("dfathing.txt") as ff:
    wordlist = [line.strip() for line in ff]
display()
print("Final nodes:", final)
for a in wordlist:
    print(rundfa(a),a)

