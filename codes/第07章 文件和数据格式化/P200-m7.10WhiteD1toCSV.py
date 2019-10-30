fo = open("price2016bj.csv", "w")
ls = ['北京', '101.5', '120.7', '121.4']
fo.write(",".join(ls)+ "\n")
fo.close()
