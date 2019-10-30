fo = open("price2016.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()
