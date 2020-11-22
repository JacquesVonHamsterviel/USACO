"""
ID: vip_1001
LANG: PYTHON3
TASK: barn1
"""

inputfile = open("barn1.in", "r").readlines()
outputfile = open("barn1.out", "w")

M = int(inputfile[0].strip()[0:inputfile[0].strip().find(" ")])
SC = inputfile[0].strip()[inputfile[0].strip().find(" ")+1:len(inputfile[0].strip())]
S = int(SC[0:SC.find(" ")])
C = int(SC[SC.find(" ")+1:len(SC)])
list = []
list2 = []
p = []
length = 0
number = 0
end = 0
for i in range(1, C+1):
   list.append(int(inputfile[i].strip()))
   list.sort()
print(list)
begin = list[0]
for i in range(1, len(list)):
    if list[i]-1 == list[i-1]:
        end = list[i]
    else:
        end = list[i-1]
        length = length+end-begin+1
        begin = list[i]
        list2.append(begin-end-1)
        number += 1

end=list[len(list)-1]
length = length+end-begin+1
number += 1
list2.sort()

#print("length:{}".format(length))
#print("number:{}".format(number))
#print(list2)

k=0
while number>M:
    length=length+list2[k]
    k+=1
    number-=1
#print("length:{}".format(length))

outputfile.write(str(length) + "\n")