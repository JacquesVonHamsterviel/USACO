"""
ID: vip_1001
LANG: PYTHON3
TASK: namenum
"""
inputfile = open("namenum.in", "r").readlines()
outputfile = open("namenum.out", "w")

dictxt=open("dict.txt", "r").readlines()
names=[]
for i in range(0,len(dictxt)):
    names.append(dictxt[i].strip())

num=[]
inputfile=inputfile[0].strip()
result=[]
for i in range(len(inputfile)):
    n=int(inputfile[i])
    num.append(int(inputfile[i])-2)
dic=[["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","R","S"],["T","U","V"],["W","X","Y"]]
newdic=[]
for j in range(1,len(inputfile)+1):
    newdic.append(dic[num[j - 1]])
from itertools import product
B=product(*newdic)
resname=""
for i in B:
    name=""
    for j in i:
        name=name+j
    result.append(name)
for i in range(0,len(result)):
        if result[i-1] in names:
            resname=result[i-1]
            break
if resname=="":
    resname="NONE"
print(resname)
outputfile.write(resname + "\n")
