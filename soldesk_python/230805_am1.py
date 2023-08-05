# 2023.08.05 1교시 시작
# a=10 #3전역변수
# def test_a(n):
#     global a
#     a += n
# test_a(10)
# print(a)


# class ClassTest:
#     d = 10 #  맴버변수, 멤버필드
#     def test_d(self, n): #self는 멤버필드임을 나타내주기 위해서 사용 
#         self.d += n   
#         return self.d
        

# result = 10 
# def test_result():
#     result += n
# print(result)
# test = ClassTest()
# #test.test_d(10)
# print(test.test_d(10))


# class Men:
#     name = ''
#     age = 0
#     def setVal(self, name, age):
#         self.name = name
#         self.age = age

# rhee = Men()
# rhee.setVal('이승무', 40)
# print(rhee.name)


# # 클래스는 변수와 함수를 재사용하기 위함이다.!!!
# # self.는 클래스에 사용하는 변수를 표기하기 위함이다!!
# # 메서드의 변수를 인식하기 위함.
# # 객채는 클래스를 지정하는 변수를 말한다.

# # 2023.08.05 1교시 끝


# # 2023.08.05 2교시 시작
# class FourCal:
#     first=0 # 생략이 가능 (파이썬만 가능)
#     second=0 # 생략이 가능
#     result=0 # 생략이 가능
#     def setData(self, first, second):
#         self.first=first
#         self.second=second
#     def add(self):
#         self.result = self.first + self.second
#     def div(self):
#         self.result = self.first / self.second
    
# cal = FourCal()
# cal.setData(10,20)
# cal.add() # 에러 발생
# print(cal.result)

# # self에 대한 설명
# cal1=FourCal()
# cal1.setData(10,34)

# cal2=FourCal()
# FourCal.setData(cal2, 20, 40)
# print(cal2.first)

# class FourCal():
#     def add(self,num1,num2):
#         self.result=num1+num2
#     def div(self,num1,num2):
#         self.result=num1/num2
    
# cal3=FourCal()
# #FourCal.add(cal3, 10,20)
# cal3.add(10,20)
# print(cal3.result)

# cal4=FourCal()
# FourCal.add(cal4, 10,20)
# print(cal4.result)
# result=cal4.add(10,20)
# print(result)


# #####################################################
# class FourCal:
#     #first=0 # 생략이 가능 (파이썬만 가능)
#     #second=0 # 생략이 가능
#     #result=0 # 생략이 가능
#     def setData(self, first, second):      # 맴버필드 초기화 하기 위함
#         self.first=first
#         self.second=second
#     def add(self):
#         self.result = self.first + self.second
#     def div(self):
#         self.result = self.first / self.second


# cal1 = FourCal()
# #print(cal1.first) #error
# # 변수 초기화 해줘야 함 그래야 에러 발생 안됨
# cal1.setData(10,20)
# print(cal1.first)
# print(cal2.first)
# cal1.add()
# print(cal1.result)
# # setData 하는게 싫음

# #####################################################
# print("__init__ 설명 : 객체가 실행될때 자동으로 생성되는 애 그래서 생성자!!")
# class FourCal:
#     #first=0 # 생략이 가능 (파이썬만 가능)
#     #second=0 # 생략이 가능
#     #result=0 # 생략이 가능
#     def __init__(self, first, second):      # 맴버필드 초기화 하기 위함
#         self.first=first
#         self.second=second
#     def add(self):
#         self.result = self.first + self.second
#     def div(self):
#         self.result = self.first / self.second

# cal1 = FourCal(10, 20)
# print(cal1.first)
# print(cal2.first)
# cal1.add()
# print(cal1.result)

# ####################################################################################
# class MoreFourCal(FourCal):
#     # def add(): 클래스의 상속
#     # def div():
#     def sub(self):
#         self.result=self.first - self.second
#     def mul(self):
#         self.result=self.first * self.second


# cal5=MoreFourCal(10,20)
# cal5.add()
# cal5.mul()
# print(cal5.result)

# cal6 = MoreFourCal(0,20)
# cal6.div()  # 0/20=0 : 부정
# print(cal6.result)

# cal7 = MoreFourCal(20,0)
# #cal7.div()  # 20/0= : 불능
# #print(cal7.result)

# class MoreFourCal(FourCal):
#     # def add(): 클래스의 상속
#     # def div():
#     def sub(self):
#         self.result=self.first - self.second
#     def mul(self):
#         self.result=self.first * self.second
#     def div(self): # 재정의 (override) 부모로부터 받은 함수를 재정의하고 싶다.
#         if self.second == 0:
#             self.result = 0
#         else:
#             self.result=self.first / self.second 


# cal7 = MoreFourCal(20,0)
# cal7.div()  # 20/0= : 불능
# print(cal7.result)

# # 모듈 : 변수, 객체 , 함수, 클래스, 상수등을 모아둔 파일
# import mod1
# print(mod1.PI)



# # 2023.08.05 2 교시 끝



# # 2023.08.05 3교시 시작
# # 스크래핑 : 웹문서에 있는 코드 모두를 다 가지고 오는것
# # 크롤링 : 스크래핑한 코드에서 원하는 내용만 추출하는것

# 스크래핑
# import urllib.request
# url = "http://uta.pw/shodou/img/28/214.png"
# saveName = "test.png"
# urllib.request.urlretrieve(url, saveName)


# import urllib.request
# url = "http://uta.pw/shodou/img/28/214.png"
# mem = urllib.request.urlopen(url).read()
# with open("test1.png", "wb") as f:
#     f.write(mem)


# import urllib.request
# import urllib.parse
# API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# value= {"stnId":108}
# params = urllib.parse.urlencode(value)
# url = API + "?" + params
# print("url =" + url)
# data = urllib.request.urlopen(url).read()
# text = data.decode("utf-8")

# https://www.google.com/search?q=python
# |<...............url..................>|
#                       |<----uri------->|
#                              <-------->| 쿼리 스트링
# import urllib.request
# import urllib.parse
# # API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# # data=urllib.request.urlopen(API).read()
# # print(data)
# # text = data.decode("utf-8")
# # #print(text)


# # import urllib.request
# # import urllib.parse
# # regionNumber=int(input("지역번호 입력"))
# # API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# # value ={"StnId":regionNumber}
# # parmas=urllib.parse.urlencode(value) # 딕셔녀리를 쿼리스트링으로 변경
# # url=API+"?"+parmas
# # print(url)
# # data=urllib.request.urlopen(API).read()
# # text = data.decode("utf-8")
# # print(text)

# ### 크롤링
# from bs4 import BeautifulSoup # test -> html로 파싱
# #스크래핑
# # html = """  
# # <html><body>
# #   <h1>스크레이핑이란?</h1>
# #   <p>웹 페이지를 분석하는 것</p>
# #   <p>원하는 부분을 추출하는 것</p>
# # </body></html>
# # """


# # soup=BeautifulSoup(html,'html.parser') # text를 html로 변환
# # h1 = soup.html.h1
# # print(h1.string)

# # html = """  
# # <html><body>
# #   <h1 id='title'>스크레이핑이란?</h1>
# #   <p id='body'>웹 페이지를 분석하는 것</p>
# #   <p>원하는 부분을 추출하는 것</p>
# # </body></html>
# # """
# # soup=BeautifulSoup(html,'html.parser') # text를 html로 변환
# # title = soup.find(id="title")
# # print(title)
# # print(title.string)
# # body = soup.find(id="body")
# # print(body)
# # print(body.string)

# html = """  
# <html><body>
#   <h1 id='title'>스크레이핑이란?</h1>
#   <p id='body'>웹 페이지를 분석하는 것</p>
#   <p><a href='a.html' id='link'>원하는 부분을 추출하는 것</a></p>
# </body></html>
# """
# soup=BeautifulSoup(html,'html.parser') # text를 html로 변환
# a= soup.html.a
# print(a)
# print(a.string)
# attr=a.attrs
# print(a.attrs)

import urllib.request as req # 스크래핑
from bs4 import BeautifulSoup # 크롤링
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
data = req.urlopen(url).read()
#html = data.decode("utf-8")
soup = BeautifulSoup(data, "html.parser")
#### 크롤링
title = soup.find('title').string
print(title)
wf = soup.find('wf').string
print(wf)




# 2023.08.05 3 교시 끝



# 2023.08.05 4교시 시작



# 2023.08.05 4 교시 끝