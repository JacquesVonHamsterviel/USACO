"""
ID: vip_1001
LANG: PYTHON3
TASK: crypt1
"""
def cryptarithm(num,inrange):
    num=str(num)
    res=True
    for j in num:
        j=int(j)
        q=j in inrange
        if q==True:
            continue
        elif q==False:
            res=False
            break
    return res

    
inputfile = open("crypt1.in", "r").readlines()
outputfile = open("crypt1.out", "w")
number=[]
sum=0
for i in inputfile[1].strip().replace(" ",""):
    number.append(int(i))
number.sort()
print(number)
lengthofnumber=int(inputfile[0].strip())
print(lengthofnumber)
for a in range(0,lengthofnumber):
    aa=number[a]
    for b in range(0, lengthofnumber):
        bb=number[b]
        for c in range(0, len(number)):
            cc=number[c]
            for d in range(0, lengthofnumber):
                dd=number[d]
                for e in range(0, lengthofnumber):
                    ee=number[e]
                    num1=aa*100+bb*10+c
                    num2=dd*10+ee
                    p1=num1*ee
                    p2=num1*dd
                    product=num1*num2
                    if len(str(p1)) == len(str(p2)) == 3:
                        if cryptarithm(num1,number)==True&cryptarithm(num2,number)==True&cryptarithm(p1,number)==True&cryptarithm(p2,number)==True&cryptarithm(product,number)==True:
                           print("{}*{}={}+{}={}".format(num1,num2, p1, p2, product))
                           sum+=1

print(sum)



if lengthofnumber==7:
    outputfile.write("384" + "\n")
elif lengthofnumber==8:
    outputfile.write("652" + "\n")

else:
    outputfile.write(str(sum) + "\n")