allUniv = []  #存储全部表格数据，二维列表
def fillUnivList(soup):
    data = soup.find_all('tr')  #找到所有tr标签
    for tr in data:
        ltd = tr.find_all('td')  #在每个tr标签中找到所有td标签
        if len(ltd) = 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)  #提取td标签中的信息
        allUniv.append(singleUniv)
