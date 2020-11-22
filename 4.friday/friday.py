'''
ID: vip_1001
LANG: PYTHON3
TASK: friday
'''

f = open('friday.in', 'r')
w = open('friday.out', 'w')



start=1
sum=[0,0,0,0,0,0,0]
years=int(f.read())
months = [31,28,31,30,31,30,31,31,30,31,30,31]
week = 0

year=years
numberofnormol=0
numberofleap=0


for year in range(1900, 1900+years, 1):
    if year%100==0 and year%400!=0:
        months[1] = 28
    elif year%400==0:
        months[1] = 29
    else:
        if year%4 == 0:
            months[1] = 29
        else:
            months[1] = 28
    for i in range(12):
        week = (week + 13) % 7
        sum[week] =sum[week]+1
        week = (week + (months[i]-13)) % 7

print(sum)

#for i in range(12):
   # week=(week+sum[i]-1)%7
#print(week)

'''
            #numberofnormol = numberofnormol + 1
totoldays=365*years+numberofleap
print(numberofleap)
print(numberofnormol)
print(months)
print(sum)
print(totolday)

k = 3
for i in range(1,totoldays):
'''

answer=str(sum[6])+" "+str(sum[0])+" "+str(sum[1])+" "+str(sum[2])+" "+str(sum[3])+" "+str(sum[4])+" "+str(sum[5])+"\n"
w.write(answer)












