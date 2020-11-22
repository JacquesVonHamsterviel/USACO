"""
ID: vip_1001
LANG: PYTHON3
TASK: transform
"""
inputfile = open("transform.in", "r").readlines()
outputfile = open("transform.out", "w")




def clockwise90(list):
    n=len(list)
    res=[]
    for i in range(1,n+1):
        rowcontent=[]
        for j in range(1,n+1):
            element=str(list[n-i+1][j])
            rowcontent.append(element)
        res.append(rowcontent)
    return res
def clockwise180(list):
    res=clockwise90(clockwise90(list))
    return res
def clockwise270(list):
    res = clockwise90(clockwise90(clockwise90(list)))
    return res

