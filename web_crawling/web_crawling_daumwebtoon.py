from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

if __name__ == '__main__' :
    # 다음웹툰 > 취향저격그녀 제목 가져오자
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data :
        j = json.loads(data.read())

    html = "<html><head><meta charset='utf-8'></head><body>"

    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles :
        title = cartoon_title["title"]
        image = cartoon_title["episodeImage"]["url"]
        url = "http://webtoon.daum.net/webtoon/viewer/" + str(cartoon_title["id"])

        html += "<a href = '{}'><img src='{}' />{}</a>".format(url, image, title)
    html += "</body>"

    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())

    with open("취향저격그녀.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)