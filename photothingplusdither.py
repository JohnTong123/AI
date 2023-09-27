from distutils.ccompiler import gen_lib_options
from sys import argv
import urllib.request
import io
import random
from PIL import Image
import math
k = int(argv[2]) #this is the k value
from datetime import datetime

# URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg' #url
URL = argv[1]
# f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
# f="IMG_1089-min (1) (1).jpg"
#f="c:\\temp\\ad.jpg"
f="image.jpg"
img = Image.open(f) # You can also use this on a local file; just put the local filename in quotes in place of f.
img.show() # Send the image to your OS to be displayed as a temporary file
print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
w,h = img.size

speed = {}
for alx in range (w):
    for aly in range (h):
        if pix[alx,aly] not in speed:
            speed[pix[alx,aly]]=[(alx,aly)]
        else:
            speed[pix[alx,aly]].append((alx,aly))

back = Image.new(mode = "RGB", size = (w, h+w//k),
                           color = (255, 0, 255))

def eight():
    for a in range(w):
        for aa in range(h):
            colores1 = 0
            colores2= 0
            colores3=0 
            if pix[a,aa][0]>127:
                colores1=255
            if pix[a,aa][1]>127:
                colores2=255
            if pix[a,aa][2]>127:
                colores3=255
            pix[a,aa] =(colores1,colores2,colores3) 
def twentyseven():
    for a in range(w):
        for aa in range(h):
            colores1 = 0
            colores2= 0
            colores3=0 
            if pix[a,aa][0]>170:
                colores1=255
            elif pix[a,aa][0]>84:
                colores1=127
            if pix[a,aa][1]>170:
                colores2=255
            elif pix[a,aa][1]>84:
                colores2=127
            if pix[a,aa][2]>170:
                colores3=255
            elif pix[a,aa][2]>84:
                colores3=127
            pix[a,aa] =(colores1,colores2,colores3) 
def dithernaive8():
    storage=[]
    for aly in range(h):
        for alx in range(w):
            storage.append(list(pix[alx,aly]))
    count=0
    for aly in range(h):
        for alx in range(w):
            coloress=[]
            colores1 = 0
            colores2= 0
            colores3=0 
            
            if storage[count][0]>127:
                colores1=255
                    
            if storage[count][1]>127:
                colores2=255
            if storage[count][2]>127:
                colores3=255
            coloress.append(colores1)  
            coloress.append(colores2)      
            coloress.append(colores3)      

            for idk in range(3):
                if not alx==w-1:
                    # print(coloress[idk])
                    storage[count+1][idk] = 7/16 *(storage[count][idk] - coloress[idk]) +storage[count+1][idk]
                if not alx ==0 and not aly == h-1 :
                    storage[count-1+w][idk] = 3/16 * (storage[count][idk] - coloress[idk])+storage[(count-1+w)][idk] 
                if not aly == h-1:
                    storage[(count+w)][idk] = 5/16 * (storage[count][idk] - coloress[idk]) +storage[(count+w)][idk]
                if not aly == h-1 and not alx ==w-1:
                    storage[(count+w+1)][idk] = 1/16 * (storage[count][idk] - coloress[idk]) +storage[(count+1+w)][idk]
            pix[alx,aly] =(colores1,colores2,colores3) 
            count=count+1
    back.paste(img)
    colors =[(0,0,0),(0,0,255),(0,255,0),(255,0,0),(255,255,0),(255,0,255),(0,255,255),(255,255,255)]
    k=8
    count=0
    for aaaa in colors:
        im = Image.new(mode = "RGB", size = (w//k , 200),
                color = aaaa)

        back.paste(im,(count *w//k,h ))
        count = count + 1
def dithernaive27():
    storage=[]
    for aly in range(h):
        for alx in range(w):
            storage.append(list(pix[alx,aly]))
    count=0
    for aly in range(h):
        for alx in range(w):
            coloress=[]
            colores1 = 0
            colores2= 0
            colores3=0 
            if storage[count][0]>170:
                colores1=255
            elif storage[count][0]>84:
                colores1=127
            if storage[count][1]>170:
                colores2=255
            elif storage[count][1]>84:
                colores2=127
            if storage[count][2]>170:
                colores3=255
            elif storage[count][2]>84:
                colores3=127
            coloress.append(colores1)  
            coloress.append(colores2)      
            coloress.append(colores3)      

            for idk in range(3):
                if not alx==w-1:
                    # print(coloress[idk])
                    storage[count+1][idk] = 7/16 *(storage[count][idk] - coloress[idk]) +storage[count+1][idk]
                if not alx ==0 and not aly == h-1 :
                    storage[count-1+w][idk] = 3/16 * (storage[count][idk] - coloress[idk])+storage[(count-1+w)][idk] 
                if not aly == h-1:
                    storage[(count+w)][idk] = 5/16 * (storage[count][idk] - coloress[idk]) +storage[(count+w)][idk]
                if not aly == h-1 and not alx ==w-1:
                    storage[(count+w+1)][idk] = 1/16 * (storage[count][idk] - coloress[idk]) +storage[(count+1+w)][idk]
            pix[alx,aly] =(colores1,colores2,colores3) 
            count=count+1
    back.paste(img)
    colors=[]
    for randomthingy in range(3):
        for randomthing in range(3):
            for randomt in range(3):
                colors.append((randomthingy *127,randomthing*127,randomt*127))
    # colors =[(0,0,0),(0,0,255),(0,255,0),(255,0,0),(255,255,0),(255,0,255),(0,255,255),(255,255,255)]
    k=27
    count=0
    for aaaa in colors:
        im = Image.new(mode = "RGB", size = (w//k , 200),
                color = aaaa)

        back.paste(im,(count *w//k,h ))
        count = count + 1
def spedkmeanplusdit():
    kount=1
    colors={}
    start = True
    past = {}
    xval = random.randint(0, w - 1)
    yval = random.randint(0, h - 1)
    #kount = 1
    #colors = {}
    colors[pix[xval, yval]] = []
    start = True
    past = {}
    while len(colors) < k:
        beeg = 0
        # close=math.inf
        far = -math.inf
        trackerr = None
        for everything in speed.keys():
            # sizee =0
            close = math.inf
            for everythingg in colors.keys():
                newdistance = (everything[0] - everythingg[0]) ** 2 + (everything[1] - everythingg[1]) ** 2 + (
                            everything[2] - everythingg[2]) ** 2
                if newdistance < close:
                    close = newdistance
                    # sizee=0
                    sizee = newdistance

            if sizee > beeg:
                beeg = sizee
                trackerr = everything
                # print(trackerr)
        if not trackerr in colors and not trackerr == None:
            colors[trackerr] = []
    past=colors.copy()
    now=datetime.now()
    while not past.keys() == colors.keys() or start == True:
        start=False

        for each in speed:
            smol = 10000
            track = None
            for aaa in colors:
                dist = 0
                # print(each[0])
                dist = dist + abs(aaa[0]-each[0])
                dist = dist + abs(aaa[1]-each[1])
                dist = dist + abs(aaa[2]-each[2])
                if smol > dist:
                    smol=dist
                    track = aaa
            for i in range(0,len(speed[each])):
                colors[track].append(each)
        past=colors.copy()
        newcolor={}
        for all in colors.values():
            r=0
            g=0
            b=0
            for everything in all:
                r=r+everything[0]
                g=g+everything[1]
                b=b+everything[2]
            newcolor[(r//len(all),g//len(all),b//len(all))] =[]
        colors = newcolor.copy()
        kount=kount+1
        print("Generation number:", kount)
    print("Time: ",datetime.now()-now)
    #for a in range(w):
            #for aa in range(h):
                #smol = 10000
                #track = None
                #for aaa in colors:
                    #dist = 0
                    #dist = dist + abs(aaa[0]-pix[a,aa][0])
                    #dist = dist + abs(aaa[1]-pix[a,aa][1])
                    #dist = dist + abs(aaa[2]-pix[a,aa][2])
                    #if smol > dist:
                        #smol=dist
                        #track = aaa
                #pix[a,aa] = track
    #for a in range(1,w-1):
    for aa in range(0, h):
        for a in range(0, w):
        #for aa in range(1,h-1):
            smol = 10000
            track = None
            for aaa in colors:
                dist = 0
                dist = dist + abs(aaa[0]-pix[a,aa][0])
                dist = dist + abs(aaa[1]-pix[a,aa][1])
                dist = dist + abs(aaa[2]-pix[a,aa][2])
                if smol > dist:
                    smol=dist
                    track = aaa
            redError=pix[a,aa][0]-track[0]
            greenError=pix[a,aa][1]-track[1]
            blurError=pix[a,aa][2]-track[2]

            pix[a,aa] = track
            if not a == w - 1:
                pix[a+1, aa] = (pix[a+1, aa][0]+int(7/16*redError+0.5),pix[a + 1, aa][1] + int(7 / 16 * greenError+0.5),pix[a + 1, aa][2] + int(7 / 16 * blurError+0.5))
            if not a== 0 and not aa == h - 1:
                pix[a - 1, aa+1]= (pix[a - 1, aa+1][0] + int(3 / 16 * redError+0.5),pix[a - 1, aa+1][1] + int(3 / 16 * greenError+0.5),pix[a - 1, aa+1][2] + int(3 / 16 * blurError+0.5))
            if not aa == h - 1:
                pix[a, aa + 1] = (pix[a, aa + 1][0] + int(5 / 16 * redError+0.5),pix[a, aa + 1][1] + int(5 / 16 * greenError+0.5),pix[a, aa + 1][2] + int(5 / 16 * blurError+0.5))
            if not aa == h - 1 and not a == w - 1:
                pix[a + 1, aa + 1] = (pix[a + 1, aa + 1][0] + int(1 / 16 * redError+0.5),pix[a + 1, aa + 1][1] + int(1 / 16 * greenError+0.5),pix[a + 1, aa + 1][2] + int(1 / 16 * blurError+0.5))

               
    count=0
    print((colors))
    
    for aaaa in colors:
        print(aaaa)
        im = Image.new(mode = "RGB", size = (w//k , 200),
                color = aaaa)

        back.paste(im,(count *w//k,h ))
        count = count + 1
                # colors[track].append(pix[a,aa])
def kmean():
    kount=1
    colors={}
    start = True
    past = {}
    while len(colors) < k:
        xval=random.randint(0,w)
        yval=random.randint(0,h)
        if not pix[xval,yval] in colors:
            colors[pix[xval,yval]] = []
    past=colors.copy()
    while not past.keys() == colors.keys() or start == True:
        start=False

        for a in range(w):
            for aa in range(h):
                smol = 10000
                track = None
                for aaa in colors:
                    dist = 0
                    dist = dist + abs(aaa[0]-pix[a,aa][0])
                    dist = dist + abs(aaa[1]-pix[a,aa][1])
                    dist = dist + abs(aaa[2]-pix[a,aa][2])
                    if smol > dist:
                        smol=dist
                        track = aaa
                colors[track].append(pix[a,aa])
        past=colors.copy()
        newcolor={}
        for all in colors.values():
            r=0
            g=0
            b=0
            for everything in all:
                r=r+everything[0]
                g=g+everything[1]
                b=b+everything[2]
            newcolor[(r//len(all),g//len(all),b//len(all))] =[]
        colors = newcolor.copy()
        kount=kount+1
        print("Generation number:", kount)
    for a in range(w):
            for aa in range(h):
                smol = 10000
                track = None
                for aaa in colors:
                    dist = 0
                    dist = dist + abs(aaa[0]-pix[a,aa][0])
                    dist = dist + abs(aaa[1]-pix[a,aa][1])
                    dist = dist + abs(aaa[2]-pix[a,aa][2])
                    if smol > dist:
                        smol=dist
                        track = aaa
                pix[a,aa] = track
               
                count=0
    for aaaa in colors:
        im = Image.new(mode = "RGB", size = (w//k , 200),
                color = aaaa)
        count=count+1
        back.paste(im,(count *w//k,h ))
                # colors[track].append(pix[a,aa])

# print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
# pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
# kmean()
spedkmeanplusdit()
back.paste(img)

back.show()


# kmean()
# img.show() # Now, you should see a single white pixel near the upper left corner
img.save("kmeansout.png")
