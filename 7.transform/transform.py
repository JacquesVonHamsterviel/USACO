"""
ID: vip_1001
LANG: PYTHON3
TASK: transform
"""
inputfile = open("transform.in", "r").readlines()
outputfile = open("transform.out", "w")
n=int(inputfile[0].strip())
original = []
def originalgraph(inputfile):
    for row in range(1, n + 1):
        line = inputfile[row]
        line = line.strip()
        originalrow = []
        for list in range(1, n + 1):
            element = line[list - 1]
            originalrow.append(element)
        original.append(originalrow)
    return original
def outputgraph(inputfile):
    res=[]
    for i in range(1,n+1):
        line=inputfile[n+i]
        line=line.strip()
        outputrow=[]
        for j in range(1,n+1):
            element=line[j-1]
            outputrow.append(element)
        res.append(outputrow)
    return(res)

original = originalgraph(inputfile)
outputgraph=outputgraph(inputfile)
def clockwise90(original):
    res=[]
    row=[]
    for i in range(0,n):
        for j in range(0,n):
            row.append(original[n-j-1][i])
        res.append(row)
        row=[]
    return(res)
def clockwise180(original):
    res=clockwise90(clockwise90(original))
    return res
def clockwise270(original):
    res=clockwise90(clockwise90(clockwise90(original)))
    return res
def reflection(original):
    res=[]
    row=[]
    for i in range(0,n):
        for j in range(0,n):
            row.append(original[i][n-j-1])
        res.append(row)
        row=[]
    return res
def combination1(original):
    res=clockwise90(reflection(original))
    return res
def combination2(original):
    res = clockwise180(reflection(original))
    return res
def combination3(original):
    res = clockwise270(reflection(original))
    return res
if outputfile==original:
    out="6"
elif outputgraph==clockwise90(original):
    out="1"
elif outputgraph==clockwise180(original):
    out="2"
elif outputgraph==clockwise270(original):
    out="3"
elif outputgraph==reflection(original):
    out="4"
elif outputgraph == combination1(original):
    out="5"
elif outputgraph==combination2(original):
    out="5"
elif outputgraph==combination3(original):
    out="5"
else:
    out="7"

outputfile.write(str(out) + "\n")




