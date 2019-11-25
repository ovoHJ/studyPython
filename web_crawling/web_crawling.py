from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
    # 네이버웹툰 > 트럼프 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=524520")
    print(data)
    soup = BeautifulSoup(data, "lxml")
    print(soup)
    #print(soup)
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        print(title)

    cartoon_titles