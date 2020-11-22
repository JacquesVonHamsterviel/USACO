'''
ID: vip_1001
LANG: PYTHON3
PROB: gift1
'''

inputfile = open('../gift1.in', 'r')
#outputfile = open('gift1.out', 'w')
numberofpeople = int(inputfile.readline().strip())
dict_money = {inputfile.readline().strip():0 for i in range(numberofpeople)}
print(dict_money)
print(numberofpeople)


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
		dict_money[receiver] = quotient
        dict_money[giver] = -amount + remainder


print(dict_money)