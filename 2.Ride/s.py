word="USACO PYTHON"
a=str.upper(word) #变成大写
b=str.lower(word) #变为小写
c=word.find(" ") #找到空格的位置，返回结果为字符串的第几位
word1=word[0:c] #截第一段
word2=word[c+1:len(word)] #截第二段
print(word1)
print(word2)
print(c)
print(a,b)

word="USACO PYTHON"
a=str.upper(word) 
b=str.lower(word)
c=word.find(" ") 
word1=word[0:c] 
word2=word[c+1:len(word)] 
print(word1)
print(word2)
print(c)
print(a,b)