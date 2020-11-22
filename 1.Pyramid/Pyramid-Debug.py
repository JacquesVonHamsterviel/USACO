//num=int(input("Enter the number of rows:"))
num=5
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


rows=5
def pyramid(rows):
    for i in range(rows):
        print(''*(rpws-i-1)+'*'*(i+1))
pyramid()