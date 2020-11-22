"""
ID: vip_1001
LANG: PYTHON3
TASK: milk
"""
def left(string):
    rs = int(string[0:string.find(" ")])
    return rs
def right(string):
    rs = int(string[string.find(" ")+1:len(string)])
    return rs
def takeFirst(elem):
    return elem[0]
inputfile = open("milk.in", "r").readlines()
outputfile = open("milk.out", "w")

target=int(inputfile[0].strip()[0:inputfile[0].strip().find(" ")])
numoffarmers=int(inputfile[0].strip()[inputfile[0].strip().find(" ")+1:len(inputfile[0].strip())])
if target==0:
    outputfile.write("0\n")
    quit()
elif numoffarmers==0:
    outputfile.write("0\n")
    quit()
list=[]
temp=0
moneyused=0
for i in range (1,numoffarmers+1):
    l=[]
    l.append(left(inputfile[i]))
    l.append(right(inputfile[i]))
    list.append(l)
list.sort(key=takeFirst)
i=0
while temp<target:
    moneyused+=list[i][0]*list[i][1]
    temp+=list[i][1]
    i+=1
remainder=0
for j in range(0,i):
    remainder+=list[j][1]
remainder=remainder-target
moneyused=moneyused-remainder*list[i-1][0]

print(list)
print("Stop at farmer {} ".format(i))
print("moneyused: {} cents".format(moneyused))
print("remainder: {} unit".format(remainder))
print("moneyused: {} cents".format(moneyused))

outputfile.write(str(moneyused) + "\n")