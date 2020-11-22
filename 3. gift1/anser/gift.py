
f = open('gift1.in', 'r')
w = open('gift1.out', 'w')
input = f.read()

output = ""
# 总人数计算
input = input.split("\n")
people = []
for gifts in range(int(input[0])):
    people.append([input[gifts + 1], 0])

# 删掉已读数据
del input[0:int(input[0]) + 1]

# 计算实际花费
for peeps in range(int(len(people))):
    # 失去的钱
    giver = input[0]
    paid = input[1].split(" ")
    money = int(paid[0])
    shared = int(paid[1])
    # 别人得到的钱
    receipients = input[2:2 + shared]
    # 删掉已读数据
    del input[0:2 + shared]
    # 计算花费
    if money > 0:
        kept = money % shared
        given = money // shared
    else:
        kept = 0
        given = 0
    # 分配钱
    for gifts in range(int(len(people))):
        if people[gifts][0] == giver:
            people[gifts][1] -= (money - kept)
        if people[gifts][0] in receipients:
            people[gifts][1] += given

    print(people)






# 输出数据
for data in range(int(len(people))):
    output += people[data][0] + " " + str(people[data][1]) + "\n"

w.write(output)




