"""
ID: vip_1001
LANG: PYTHON3
TASK: ride
"""
output=open("ride.out","w")
TXT=open("ride.in","r")
wordA,wordB=TXT.readlines()
newdict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"\n":1}
SumA=1
SumB=1
for character in wordA:
    number=newdict[character]
    SumA=SumA*number
for character in wordB:
    number=newdict[character]
    SumB=SumB*number
DvidedA=SumA%47
DvidedB=SumB%47
if DvidedA==DvidedB:
    result="GO"
else:
    result="STAY"
output.write(result+"\n")
output.close()