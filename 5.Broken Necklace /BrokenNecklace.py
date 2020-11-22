"""
ID: vip_1001
LANG: PYTHON3
TASK: beads
"""

inputfile = open("beads.in", "r").readlines()
outputfile = open("beads.out", "w")

n=inputfile[0]
n=int(n.replace("\n",""))

necklace=inputfile[1]
necklace=necklace.replace("\n","")
necklace=necklace.replace(" ","")
necklace=str.lower(necklace)+str.lower(necklace)+str.lower(necklace)

print(necklace)

currentposition=n
sum=0

for i in range(1,n+1): #循环项链的长度次
    #清空当次计算数据
    frontcalc = 1
    backcalc = 1
    #项链断点前的比较
    if (necklace[currentposition] != "w"):
        for fi in range(1, n):
            if (necklace[currentposition] == necklace[currentposition - fi]):  # 当当前字幕与前一个字母相同时
                frontcalc += 1
            elif (necklace[currentposition - fi] == "w"):  # 当前一个字母是w时
                frontcalc += 1

            else:
                break

    else:
        for fi in range(1, n):
            if (necklace[currentposition - fi] == "w"):
                frontcalc += 1
            else:
                colour = necklace[currentposition - fi]
                frontcalc += 1
                for fj in range(1, n+1 - fi):
                    if (colour == necklace[currentposition - fi - fj]):  # 当当前字幕与前一个字母相同时
                        frontcalc += 1
                    elif (necklace[currentposition - fi - fj] == "w"):  # 当前一个字母是w时
                        frontcalc += 1
                    else:
                        break
                break



    # 项链断点后的比较
    if (necklace[currentposition+1] != "w"):
            for bi in range(1, n):
                if (necklace[currentposition + 1] == necklace[currentposition + bi + 1]):
                    backcalc += 1
                elif (necklace[currentposition + bi + 1] == "w"):
                    backcalc += 1
                else:
                    break

    else:
            for bi in range(1, n):
                if (necklace[currentposition +1+ bi] == "w"):
                    backcalc += 1
                else:
                    colour = necklace[currentposition + bi +1]
                    backcalc+=1
                    for bj in range(1, n+1 - bi):
                            if (colour == necklace[currentposition + bi + bj + 1]):
                                backcalc += 1
                            elif (necklace[currentposition + bi + bj + 1] == "w"):
                                backcalc += 1
                            else:
                                break
                    break











    sumcalc=frontcalc+backcalc
    if(sumcalc>sum):
        sum=sumcalc
    currentposition += 1
if(sum>n):
    sum=n

print(sum)
outputfile.write(str(sum) + "\n")
outputfile.close()





