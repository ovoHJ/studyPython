from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
    data = urlopen("https://www.youtube.com/user/BANGTANTV/videos?view=0&sort=dd&shelf_id=0")
    soup = BeautifulSoup(data, "lxml")
    data.close()

    html = "<html><head><meta charset='UTF-8'><title> 방탄소년단의 모든 것 </title></head><body>"

    all_title = soup.find_all('a', attrs={"id":"video-title"})
    print(all_title)

    html += "</body></html>"
    outputSoup = BeautifulSoup(html, "lxml")
    cleanHtml = str(outputSoup.prettify())

    # with open("All_About_BTS.html", "w", encoding="utf-8") as f:
    #     f.write(cleanHtml)