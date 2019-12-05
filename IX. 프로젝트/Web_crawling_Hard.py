from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

if __name__ == '__main__' :
    url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"03", "pageUnit":"100"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text, "lxml")
    #print(soup)

    titles = soup.select("dt.tit > a")
    for title in titles :
        print(title.text)