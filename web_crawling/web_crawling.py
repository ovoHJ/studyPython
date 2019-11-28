from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
    # 네이버웹툰 > 트럼프 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=524520")
    print(data)
    soup = BeautifulSoup(data, "lxml")
    print(soup)
    data.close()
    #print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})       # <td class="titld"> .... </td>
    for cartoon_title in cartoon_titles:                                # cartoon_titles[:2]
        title = cartoon_title.find("a").text                            # <a> text </a>
        link = cartoon_title.find("a").get("href")                      # 태그의 속성값 가져오기 <a
        print(title)
        print("https://comic.naver.com" + link)
        html += "<a href='https://comic.naver.com{}'>{}</a>".format(link, title)

    html += "</body></html>"
    #print(html)

    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())

    with open("트럼프.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)