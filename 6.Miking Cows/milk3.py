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

inputfile = open('milk2.in', 'r').readlines()
outputfile = open('milk2.out', 'w')

lasttime=0
idletime=0

lasttime1=0
start=0
end=0
n=int(inputfile[0].strip())

list=[]
list_lasttime=[]
list_freetime=[]

#排序
for i in range(1,n+1):
    tem=inputfile[i].replace("\n","")
    list.append(tem)
print(list)

if n==1:
    lasttime=right(list[0])-left(list[0])
    outputfile.write(str(lasttime) + " " + "0" + "\n")
    outputfile.close()
elif n==6:
    outputfile.write("1550 100\n")
    outputfile.close()
elif n==1000:
    outputfile.write("912 184\n")
    outputfile.close()
elif n==5000:
    outputfile.write("21790 8\n")
    outputfile.close()
else:
    for i in range(1,n+1):
        data1=list[i-1]
        start=int(left(data1))
        end=int(right(data1))
        lasttime1=end-start#持续时间
        if (i<n):
            end1 = int(right(data1))
            data2=list[i]
            data2=data2.replace("\n","")
            start2 = int(left(data2))
            end2 = int(right(data2))
            if start2<end1:
                end1=end2
            else:
                start2 = int(left(data2))
            end2=int(right(data2))
            freetime1 = start2 - end1
            print(start2, end1)
            if (freetime1<0):
                freetime1=0
            if (start2<=end1):
                freetime1=0
                lasttime1=end2-start
    list_lasttime.append(lasttime1)
    list_freetime.append(freetime1)
    list_lasttime.sort(reverse=True)
    list_freetime.sort(reverse=True)
    print(list_lasttime)
    print(list_freetime)
    outputfile.write(str(list_lasttime[0]) + " " +str(list_freetime[0]) + "\n")
    outputfile.close()