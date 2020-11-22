"""
ID: vip_1001
LANG: PYTHON3
TASK: namenum
"""
inputfile = open("namenum.in", "r").readlines()
outputfile = open("namenum.out", "w")

dictxt=open("dict.txt", "r").readlines()
dic_1=[]
dic_2=[]
originalnum=[]
for i in dictxt:
    dic_1.append(i.strip())
def wordtonum(str):
    p=[]
    res=""
    dic = {"A":"2","B":"2","C":"2","D":"3","E":"3","F":"3","G":"4","H":"4","I":"4","J":"5","K":"5","L":"5","M":"6","N":"6","O":"6","P":"7","R":"7","S":"7","T":"8","U":"8","V":"8","W":"9","X":"9","Y":"9","Z":"0","Q":"0"}
    for i in str:
        p.append(dic[i])
    return(p)

for i in range(0,len(dic_1)):
    dic_2.append(wordtonum(dic_1[i]))

for i in inputfile[0].strip():
    originalnum.append(i)
times=dic_2.count(originalnum)

if times==0:
    ans = "NONE"
elif times==1:
    p = int(dic_2.index(originalnum))
    ans = dic_1[p]
elif times==2:
    p = int(dic_2.index(originalnum))
    ans = dic_1[p]
    p2=int(dic_2.index(originalnum,p+1,len(dic_2)))
    ans=ans+"\n"+dic_1[p2]
elif times==3:
    p = int(dic_2.index(originalnum))
    ans = dic_1[p]
    p2 = int(dic_2.index(originalnum, p + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p2]
    p3 = int(dic_2.index(originalnum, p2+ 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p3]
elif times==4:
    p = int(dic_2.index(originalnum))
    ans = dic_1[p]
    p2 = int(dic_2.index(originalnum, p + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p2]
    p3 = int(dic_2.index(originalnum, p2+ 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p3]
    p4 = int(dic_2.index(originalnum, p3 + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p4]
elif times==5:
    p = int(dic_2.index(originalnum))
    ans = dic_1[p]
    p2 = int(dic_2.index(originalnum, p + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p2]
    p3 = int(dic_2.index(originalnum, p2+ 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p3]
    p4 = int(dic_2.index(originalnum, p3 + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p4]
    p5 = int(dic_2.index(originalnum, p4 + 1, len(dic_2)))
    ans = ans + "\n" + dic_1[p5]
else:
    ans="ERROR"


outputfile.write(str(ans) + "\n")
