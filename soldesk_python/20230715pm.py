# a="Life is too short, You need Python"
# print(a[-4:])

# # print("""hihidkfjldjf
# # kldjfljskdfjsl
# # skldjfklsjfdklsj
# # skdfjslkfj
# # """)
# str="sd"
# del str
# print(''' "10" + "10"
#       ''')
# print("Life is too short, You need Python"[12:14])
# print("Life is too short, You need Python"[8:8+2])

# #슬라이싱도 변수 취급해준다.
# idx = 2
# cnt = 5
# print(a[idx:idx+cnt])

# #날짜와 이름을 분리하여 출력
# a = "20010331Rainy"
# ###  0123456789012
# ##             1
# year=a[:4]
# month=a[4:4+2]
# day=a[6:6+2]
# year_day=a[:8]
# weahter=a[8:]
# print("날짜 :",year_day) #인덱스 8전까지
# print("날씨 :",weahter) #인덱스 8부터
# print(year+"년", month+"월", day+"일") # , 구분하면 공백이 삽입된다.

# #  
# a = "Life is too short"
# ###  01234567890123456
# ##             1 
# #한글자씩 건너 띄어서 프린트하기
# print(a)
# print(a[:])
# print(a[::2])
# #두글자씩 띄워서
# print(a[::3])
# #뒤에서부터 앞으로
# print(a[::-1])
# print(a[2:14])


# #문자열 포메팅
# "나의 이름은 송석중이고 나이는 30입니다."
# name="송석중"
# age=30
# print("나의 이름은 %s이고 나이는 %d 입니다." %(name,age))

# 문자열 포메팅 2
### 송석중의 계좌번호는 1111이고 잔액은 100원입니다.

name = '송석중'
account = '1111'
money = 100
#행바꿈은 \에 공백이 있으면 안됨!!
str3="%s의 계좌번호는 %s이고 잔액은 %d입니다."\
      % (name,account,money)
print(str3)

name="송석중"
age=25
height=175.3
str3="%s의 나이는 %s이고 키는 %.1f입니다." %(name,age,height)
print(str3)
#기본은 우측정렬이고 왼쪽정렬을 하고자 한다면 -주면된다. ex:%-10s(왼) %10s(우측)
