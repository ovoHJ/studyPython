import json
from urllib.request import urlopen

if __name__ == '__main__' :
    # 다음웹툰 > 취향저격그녀 제목 가져오자
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data :
        j = json.loads(data.read())
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles :
        title = cartoon_title["title"]
        image = cartoon_title["episodeImage"]["url"]
        url = "http://webtoon.daum.net/webtoon/viewer/" + str(cartoon_title["id"])
        print(title)
        print(image)
        print(url)