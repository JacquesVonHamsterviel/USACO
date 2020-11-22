'''
ID: vip_1001
LANG: PYTHON3
PROB: gift1
'''

inputfile = open('gift1.in', 'r')
outputfile = open('gift1.out', 'w')
a=inputfile.read()
print(a)
numberofpeople = int(inputfile.readline().strip()) #读取总人数
dict_money = {inputfile.readline().strip():0 #新建字典
for i in range(numberofpeople)}
currentline = numberofpeople + 2 #现在行加1到
while numberofpeople>0:

    givername = inputfile.readline(currentline) #姓名行
    givername = givername.replace("\n", "") #删除空格
    #print(givername)
    currentline = currentline + 1 #总金额和给的人数行
    moneyandpeople = inputfile.readline(currentline) #读取总金额和给的人数行
    print(moneyandpeople)
    #print(moneyandpeople)
    space=moneyandpeople.find(" ") #寻找总金额和给的人数中间的空格
    #print(moneyandpeople[0:space])
    money=int(moneyandpeople[0:space]) #读取前一半的钱数
    #print(money)

    people=int(moneyandpeople[space+1:len(moneyandpeople)]) #读取后一半的人数
    dict_money[givername]=dict_money[givername]-money #给钱者金额减少
    giveout = money // people  # 计算给出的钱


    contect = inputfile.readline(currentline) #读给钱的人
    contect = contect.replace("\n", "")#去除空格
    dict_money[contect] = dict_money[contect] + giveout

    while people>0:
        currentlineline = currentline + 1 #收到钱的人名
        contect = inputfile.readline(currentline) #收到钱的人名
        contect = contect.replace("\n", "") #去除空格
        people=people-1
        dict_money[contect] = dict_money[contect]+giveout#放入值
    print(dict_money)
    numberofpeople=numberofpeople-1
