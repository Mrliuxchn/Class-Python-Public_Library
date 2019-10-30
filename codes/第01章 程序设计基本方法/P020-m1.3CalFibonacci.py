a,b = 0,1   #同步赋值：同时给多个变量进行赋值
while a<1000:
    print(a,end=',')
    a,b=b,a+b
