'''
ID: vip_1001
LANG: PYTHON3
TASK:  milk2
'''
def left(string):
    space = string.find(" ")
    rs = int(string[0:space])
    return rs
def right(string):
    space = string.find(" ")
    rs = int(string[space+1:len(string)])
    return rs
def max(a,b):
    if a>b:
        rs=a
    else:
        rs=b
    return rs
inputfile = open('milk2.in', 'r').readlines()
outputfile = open('milk2.out', 'w')
n=int(inputfile[0].strip())
for i in inputfile:
    for j in(i,inputfile):
        if i>j:
            term=i
            i=j
            j=term
#The longest time interval at least one cow was milked.
lastingtime=0
starttime=left((inputfile[1]))
endtime=right(inputfile[1])
lasttime=right(inputfile[1])-left(inputfile[1])
idletime=0
for i in range(1,n):
    content1=inputfile[i].strip()
    content2=inputfile[i+1].strip()
    if left(content2)<=endtime:
        endtime=max(endtime,right(content2))
    else:
        lasttime=max(lasttime,endtime-starttime)
        starttime = left(content2)
        idle=left(content2)-right(content1)
        idletime=max(idletime,idle)
outputfile.write(str(lasttime) + " " +str(idletime) + "\n")
outputfile.close()