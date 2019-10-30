#e10.2CalHamlet.py 进一步排除无意义的虚词
excludes = {"the","and","of","you","a","i","my","in",\
            "to","it","that","is","not","his","this",\
            "but","with","for","your","me","be","as",\
            "he","what","him","so","have","will","do",\
            "no","we","are","on","all","our","by","or",\
            "shall","if","o","good","come","they","now",\
            "more","let","from","her","how","at"}
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
for word in excludes:
    del counts[word] 
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(12):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
