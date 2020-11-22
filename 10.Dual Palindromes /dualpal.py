"""
ID: vip_1001
LANG: PYTHON3
TASK: dualpal
"""
def tranverter(n,int):
    a=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    b=[]
    res=0
    while True:
        s=n//int  # 整数-商
        y=n%int  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    c=""
    for i in b:
        c=c+str(a[i])
    return c
def palindromic(num):
    b = num[::-1]  # 倒序
    if num==b:
        res=1
    else:
        res=0
    return res
inputfile = open("dualpal.in", "r").readlines()
outputfile = open("dualpal.out", "w")
outnum=int(inputfile[0].strip()[0:inputfile[0].strip().find(" ")])
startfrom=int(inputfile[0].strip()[inputfile[0].strip().find(" ")+1:len(inputfile[0].strip())])
reslist=[]
i=startfrom+1
while i>startfrom:
    k=0
    for j in range(2,11):
        if palindromic(tranverter(i,j))==1:
            k+=1
        if k>=2:
            reslist.append(i)
            break
    i+=1
    if len(reslist)==outnum:
        break
if len(reslist)<outnum:
    for i in range(0, len(reslist)):
        outputfile.write(str(reslist[i]) + "\n")
else:
    for i in range(0, outnum):
        outputfile.write(str(reslist[i]) + "\n")