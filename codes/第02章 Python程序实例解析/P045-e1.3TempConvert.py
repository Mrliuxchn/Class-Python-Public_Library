#e1.3TempConvert.py
def tempConvert(ValueStr):  #ValueStr：形参
    if ValueStr[-1] in ['F','f']:
        C = (eval(ValueStr[0:-1]) - 32)/1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif ValueStr[-1] in ['C','c']:
        F = 1.8*eval(ValueStr[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")
TempStr = input("请输入带有符号的温度值: ") #"82F"
tempConvert(TempStr) #TempStr：实参
