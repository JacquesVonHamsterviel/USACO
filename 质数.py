def checkprime(int):
    res=1
    for i in range(2, int - 1):
        k = int % i
        if k == 0:
            res=0
            print(int)
            break
    return res
def checkprimewithdetail(int):
    res=1
    for i in range(2, int - 1):
        k = int % i
        if k == 0:
            res=0
            print("{} Can Be Divided By {}".format(int,i))
            break
    return res

def printallprimenumbers(int):
    sum=0
    for i in range(1,int):
        if checkprime(i)==1:
            sum+=1
            print(i)
    print("There Are {} Prime Numbers In Range 2 To {}".format(sum,int))
def intmain():
    welcome = int(input(
        "Wlecome,Please Choose What Your Want To Do?\n   Press 1 To Indentify If A Number Is A Prime Number.\n   Press 2 If You Want To List All Prime Number In A Range.\nChoose Number:"))
    if welcome== 1 or 2:
        if welcome == 1:
            n = int(input("Give A Number:"))
            if n <= 1:
                print("ERROR,PRIME NUMBER STARTS FROM 2 !")
            else:
                if (checkprimewithdetail(n)):  # 是返回1
                    print("{} Is A Prime Number".format(n))
                else:
                    print("{} IS Not A Prime Number".format(n))
        elif welcome == 2:
            n = int(input("Give A Number:"))
            if n <= 1:
                print("ERROR,PRIME NUMBER STARTS FROM 2 !")
            else:
                printallprimenumbers(n)
        else:
            print("ERROR, ONLY Number 1 AND 2 Are Available!!! \n")
            intmain()

intmain()