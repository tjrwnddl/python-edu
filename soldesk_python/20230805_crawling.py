# import urllib.request as req # 스크래핑
# from bs4 import BeautifulSoup
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# data = req.urlopen(url).read()
# #html = data.decode("utf-8")
# soup = BeautifulSoup(data, "html.parser")
# #### 크롤링
# title = soup.find('title').string
# print(title)
# wf = soup.find('wf').string
# print(wf)



# import urllib.request as req # 스크래핑
# from bs4 import BeautifulSoup # 크롤링
# # 스크래핑 
# text = """
# <html><body>
# <div id="meigen">
#   <h1>위키북스 도서</h1>
#   <ul class="items">
#     <li>유니티 게임 이펙트 입문</li>
#     <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
#     <li>모던 웹사이트 디자인의 정석</li>
#   </ul>
# </div>
# </body></html>
# """

# soup = BeautifulSoup(text, "html.parser")
# h1=soup.html.h1
# print(h1)
# h2= soup.find("h1")
# print(h2)
# print(h2.string)

# h3 = soup.find("h1").string
# print(h3)

# id1 = soup.find(id="meigen")
# print(id1)
# ### css selector (선택자)
# h12=soup.select_one("div > ul > li ")
# print(h12)

# 기상청 온도와 습도 가져오기!!
# https://www.weather.go.kr/w/obs-climate/land/city-obs.do
# 
#import urllib.request as req # 스크래핑
import requests
from bs4 import BeautifulSoup # 클롤링
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do"
source = requests.get(url)
#print(source)
soup = BeautifulSoup(source.content, "html.parser")
#print(soup)
table=soup.find("table",{'class':'table-col'})

#print(table)

data=[]
for tr in table.find_all('tr'):
    tds = list(tr.find_all("td"))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].string
            humidity = tds[9].string
            data.append([point,temp,humidity])


####################################
#시각화전 데이터 처리
####################################

with open('weather.csv','w',encoding='utf-8') as f:
    f.write('지역,온도,습도\n')
    for i in data:
        f.write("{0},{1},{2}\n".format(i[0],i[1],i[2]))

#데이터처리
df = pandas.read_csv("weather.csv", index_col = "지역", encoding="utf-8")
#df

city_df = df.loc[['서울','인천','대전','대구','광주','부산','울산']]
#city_df

font_name = mpl.font_manager.FontProperties(fname="C:\\Windows\\Fonts\\batang.ttc").get_name()
mpl.rc('font',family=font_name)

ax = city_df.plot(kind="bar", title="날씨", figsize=(12,4))
plt.show()

############## numpy ################
