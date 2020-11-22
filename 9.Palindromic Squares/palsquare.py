"""
ID: vip_1001
LANG: PYTHON3
TASK: palsquare
"""
#n为待转换的十进制数，int为进制
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
inputfile = open("palsquare.in", "r").readlines()
outputfile = open("palsquare.out", "w")
int=int(inputfile[0].strip())
reslist=[]
squarelist=[]
for i in range(1,300):
   if palindromic(tranverter(i*i,int))==1:
       reslist.append(tranverter(i,int))
       squarelist.append(tranverter(i*i,int))
if reslist==[]:
    outputfile.write()
else:
    for i in range(0,len(reslist)):
        outputfile.write(str(reslist[i])+" "+str(squarelist[i])+"\n")
