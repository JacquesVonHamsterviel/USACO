'''
ID: vip_1001
LANG: PYTHON3
PROB: gift1
'''
inputfile = open('../gift1.in', 'r')
outputfile = open('../gift1.out', 'w')
input=inputfile.read()

list=input.split()
print(list)
howmanypeople=int(list[0])

who=list[1:howmanypeople+1]
#who.insert(1,0)

fin = open('../gift1.in', 'r')
np = int(fin.readline().strip())
dictOfMoney = { fin.readline().strip() : 0 for i in range(np) }

while(True):
	giver = fin.readline().strip()
	if(giver==""):
		break
	amount, divided = map(int, fin.readline().strip().split())
	receivers = [fin.readline().strip() for i in range(divided)]

	try:
		quotient, remainder = divmod(amount,divided)
	except:
		quotient = remainder = 0

	for receiver in receivers:
		dictOfMoney[receiver] += quotient
	dictOfMoney[giver] += -amount + remainder

with open('../gift1.out', 'w') as fout:
	for name, money in dictOfMoney.items():
		fout.write(f"{name} {money}\n")
'''
print(input)
output = ""

input = input.split("\n")
people = []

#Counting amount of people
numberofpeople=input[0]
print(numberofpeople)

#first=word.find(" ") 
#word1=word[0:c] 
#people = []
#del input[0:2 ]
#people.append([input[gifts + 1], 0])
print(input)
#Getthenames
for gifts in range(int(input[0])):
  people.append([input[gifts + 1],0])
print(people)

del input[0:int(input[0])+1]

print(input)

#for i in range(int(len(people))):
'''