import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 20)
        r.raise_for_status()
        r.encoding = 'uft-8'
        return r.text
    except:
        return ""
url = "http://www.baidu.com"
print(getHTMLText(url))
