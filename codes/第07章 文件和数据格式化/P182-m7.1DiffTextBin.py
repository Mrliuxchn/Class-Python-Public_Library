#在记事本文件里可以查看到该文本文件的编码方案为ANSI
textFile = open("7.1.txt","rt",encoding='gb2312') #使用eoncoding参数
print(textFile.readline())
textFile.close()
binFile = open("7.1.txt","rb")
print(binFile.readline())
binFile.close()
