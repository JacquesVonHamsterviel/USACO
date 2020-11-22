"""
ID: vip_1001
LANG: PYTHON3
TASK: beads
"""

'''
inputfile = open("beads.in", "r").readlines()
outputfile = open("beads.out", "w")
#colourdict = {"r":1,"b":2,"w":3}

n=inputfile[0]
n=n.replace("\n","")
n=int(n)
tn=n*3
necklace=inputfile[1]
necklace=str.lower(necklace)+str.lower(necklace)+str.lower(necklace)
k=0
suml=0
sumr=0
maxsum=0

print(necklace)
start=n

for i in range(1,n+1):
    for i in range(1,n+1):
        goal_l=necklace[start-1]
        print("goal_l:",goal_l)
        goal_lc=necklace[start-i]
        if goal_l=="r":
            if goal_l==goal_lc:
                suml=suml+1
            elif goal_lc=="w":
                suml=suml+1
            else:
                break
        if goal_l=="b":
            if goal_l==goal_lc:
                suml=suml+1
            elif goal_lc=="w":
                suml=suml+1
            else:
                break
        if goal_l == "w":
            if goal_l == goal_lc:
                suml = suml + 1
            else:
                break
    goal_r = necklace[start]
    print("goal_r:", goal_r)
    goal_rc = necklace[start + i]
    if goal_r == "r":
        if goal_r == goal_rc:
            sumr = sumr + 1
        elif goal_rc == "w":
            sumr = sumr + 1
        else:
            break
    if goal_r == "b":
        if goal_r == goal_rc:
            sumr = sumr + 1
        elif goal_rc == "w":
            sumr = sumr + 1
        else:
            break
    if goal_r == "w":
        if goal_r == goal_rc:
            sumr = sumr + 1
        else:
            break
    start = start + 1




print(suml)
print(sumr)


    for i in range(k,n-k):
        c1= necklace2[0:i]
        c2 = necklace2[i+1:i+2]
        c3= necklace2[i+1:len(necklace2)]
        print(c2)



'''


# input
inputFile = open("beads.in", "r").readlines()
outputFile = open("beads.out", "w")
necklaceStr = inputFile[1].strip()
necklaceList = list(necklaceStr)
actualNumBeads = inputFile[0].strip()
doubledNumBeads = len(necklaceList)
maxSum = 0
# check if necklace is same throughout
if len(set(necklaceList)) == 1:
    maxSum = len(necklaceList)
    outputFile.write(str(maxSum) + "\n")
else:
    necklaceList = list(necklaceStr + necklaceStr)
    numBeads = len(necklaceList)
 
    # what color will white beads be?
    def setWhiteColor(whichList):
        if whichList == "rList":
            for eachColor in rightList:
                if eachColor == "r":
                    chosenColor = "r"
                    return chosenColor
                elif eachColor == "b":
                    chosenColor = "b"
                    return chosenColor
        elif whichList == "lList":
            for eachColor in leftList:
                if eachColor == "r":
                    chosenColor = "r"
                    return chosenColor
                elif eachColor == "b":
                    chosenColor = "b"
                    return chosenColor
                
    # methods
    def getColorCount(color, whichList):
        rCount = 0
        lCount = 0
        
        # rightList colors
        if whichList == "rList":
            for eachColor in rightList:
                if eachColor == color or eachColor == "w":
                    rCount += 1
                else:
                    return rCount
        
        # leftList colors 
        if whichList == "lList":
            for eachColor in leftList:
                if eachColor == color or eachColor == "w":
                    lCount += 1
                else:
                    return lCount
                    
    # main loop
    rightIndex = 1
    leftIndex = 1
    
    for eachBead in necklaceList:
        # rightList handler
        rightList = necklaceList[rightIndex:] 
        if rightList == []:
            rightList.append(0)
        print("right:", rightList)
        
        # right color handler 
        if rightList[0] == "r":
            rMax = getColorCount("r", "rList")
        elif len(rightList) == 1:
            rMax = 1
        elif rightList[0] == "b":
            rMax = getColorCount("b", "rList")
        elif rightList[0] == "w":
            rCurrentColor = None
            rCurrentColor = setWhiteColor("rList")
            rMax = getColorCount(rCurrentColor, "rList")
        elif rightList[0] == 0:
            rMax = 0
            
            
        if rMax == None:
            rMax = 0
        rightIndex += 1
        print("rMax:", rMax)
        
        # leftList handler 
        tempLeftList = necklaceList[:leftIndex]
        leftList = tempLeftList[::-1]
        print("left:", leftList)
        
        # left color handler
        if leftList[0] == "r":
            lMax = getColorCount("r", "lList")
        elif leftList[0] == "b":
            lMax = getColorCount("b", "lList")
        elif leftList[0] == "w":
            lCurrentColor = None
            lCurrentColor = setWhiteColor("lList")
            lMax = getColorCount(lCurrentColor, "lList")
            
            
        if lMax == None:
            lMax = 0
        leftIndex += 1
        print("lMax:", lMax)
        
        
        
        
        
        # handle max
        maxSum = max(rMax + lMax, maxSum)
        print("MAX:", maxSum)
        rMax = 0
        lMax = 0
        if int(maxSum) > int(actualNumBeads):
            maxSum = int(actualNumBeads)
    
    # output
    outputFile.write(str(maxsum) + "\n")
    outputFile.close()
