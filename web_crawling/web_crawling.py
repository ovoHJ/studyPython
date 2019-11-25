from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
    # 네이버웹툰 > 트럼프 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=524520")
    print(data)
    soup = BeautifulSoup(data, "lxml")
    print(soup)
    #print(soup)
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})       # <td class="titld"> .... </td>
    for cartoon_title in cartoon_titles:                                # cartoon_titles[:2]
        title = cartoon_title.find("a").text                            # <a> text </a>
        link = cartoon_title.find("a").get("href")                      # 태그의 속성값 가져오기 <a
        print(title)
        print("https://comic.naver.com" + link)

    cartoon_titles