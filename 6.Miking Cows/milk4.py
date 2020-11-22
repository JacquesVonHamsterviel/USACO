'''
ID: vip_1001
LANG: PYTHON3
TASK:  milk2
'''

inputfile = open('milk2.in', 'r')
outputfile = open('milk2.out', 'w')


table = (inputfile.read()).split('\n')
farmers = int(table[0])
del table[0]
minvalue = 0
maxvalue = 0
for time in range(farmers):
	table[time] = table[time].split(' ')
	table[time][0] = int(table[time][0])
	table[time][1] = int(table[time][1])
	if (minvalue == 0): minvalue = table[time][0]
	if (maxvalue == 0): maxvalue = table[time][1]
	minvalue = min(table[time][0], minvalue)
	maxvalue = max(table[time][1], maxvalue)

filled_thistime = 0
filled_max = 0

empty_max = 0
empty_thistime = 0

for point in range(minvalue, maxvalue, 1):
	isfilled = False
	for check in range(farmers):
		if point >= table[check][0] and point < table[check][1]:
			filled_thistime += 1
			empty_thistime = 0
			isfilled = True
			break
	if isfilled == False:
		filled_thistime = 0
		empty_thistime += 1
	if (filled_max < filled_thistime) :
		filled_max = filled_thistime
	if (empty_max < empty_thistime) :
		empty_max = empty_thistime

if (filled_max < filled_thistime): filled_max = filled_thistime
outputfile.write(str(filled_max) + " " + str(empty_max) + "\n")
