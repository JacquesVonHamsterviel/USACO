inputfile = open('gift1.in','r')
howmanypeople = int(inputfile.readline().strip())
dictOfMoney = { inputfile.readline().strip() : 0 for i in range(howmanypeople) }

while(True):
	giver = inputfile.readline().strip()
	if(giver==""):
		break
	amount, divided = map(int, inputfile.readline().strip().split())
	receivers = [inputfile.readline().strip() for i in range(divided)]

	try:
		quotient, remainder = divmod(amount,divided)
	except:
		quotient = remainder = 0

	for receiver in receivers:
		dictOfMoney[receiver] += quotient
	dictOfMoney[giver] += -amount + remainder

with open('gift1.out','w') as fout:
	for name, money in dictOfMoney.items():
		fout.write(f"{name} {money}\n")