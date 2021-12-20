from bs4 import BeautifulSoup
import requests

def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num+1
    else:
        return num+9*(num-1)

def makeUrl(search,start_pg,end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        print("생성url: ",url)
        return url
    else:
        urls= []
        for i in range(start_pg,end_pg+1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        print("생성url: ",urls)
        return urls

def news_attrs_crawler(articles,attrs):
    attrs_content=[]
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content


def news_contents_crawler(news_url):
    contents=[]
    for i in news_url:
        news = requests.get(i)
        news_html = BeautifulSoup(news.text,"html.parser") 
        contents.append(news_html.find_all('p'))
    return contents


def articles_crawler(url):
    original_html = requests.get(i)
    html = BeautifulSoup(original_html.text, "html.parser")
    articles = html.select("div.group_news > ul.list_news > li div.news_area > a")
    title = news_attrs_crawler(articles,'title')
    url = news_attrs_crawler(articles,'href')
    content = news_contents_crawler(url)
    return title, url, content


search = input("검색할 키워드를 입력해주세요:")


page = int(input("\n크롤링할 시작 페이지를 입력. ex)(숫자만입력):")) # ex)1 =1페이지,2=2페이지...
print("\n크롤링할 시작 페이지: ",page,"페이지")   

page2 = int(input("\n크롤링할 종료 페이지를 입력.ex)(숫자만입력):")) # ex)1 =1페이지,2=2페이지...
print("\n크롤링할 종료 페이지: ",page2,"페이지")   


url = makeUrl(search,page,page2)


news_titles = []
news_url =[]
news_contents =[]
for i in url:
    title, url,content = articles_crawler(url)
    news_titles.append(title)
    news_url.append(url)
    news_contents.append(content)

print("검색된 기사 갯수: 총 ",(page2+1-page)*10,'개')
print("[뉴스 제목]")
print(news_titles)
print("[뉴스 링크]")
print(news_url)
print("[뉴스 내용]")
print(news_contents)
