fname = input("请输入要打开的文件: ")
fo = open(fname, "r")
a = fo.readlines()
print(type(a))
for line in a:
    print(line)
fo.close()
