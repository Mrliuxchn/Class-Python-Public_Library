#e10.3CalThreeKingdoms.py
import jieba
excludes = {}#{"将军","却说","丞相"}
txt = open("三国演义.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
