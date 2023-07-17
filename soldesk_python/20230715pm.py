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

################################################################################
# # 문자열 포메팅 2
# ### 송석중의 계좌번호는 1111이고 잔액은 100원입니다.

# name = '송석중'
# account = '1111'
# money = 100
# #행바꿈은 \에 공백이 있으면 안됨!!
# str3="%s의 계좌번호는 %s이고 잔액은 %d입니다."\
#       % (name,account,money)
# print(str3)

# name="송석중"
# age=25
# height=175.3
# str3="%s의 나이는 %s이고 키는 %.1f입니다." %(name,age,height)
# print(str3)
# #기본은 우측정렬이고 왼쪽정렬을 하고자 한다면 -주면된다. ex:%-10s(왼) %10s(우측)

################################################################################



################################################################################
# 문자열 포매팅 3
# format 함수를 이용한 포매팅
# 문자 : 'a'
# 정수 : 10
# 실수 : 0.1
# 변수 : a
# 함수 : a(), print(), len(), str(), format()
#송석중의 나이는 25이고 키는 175.3입니다.
# name="송석중"
# age=25
# height=175.3
# str3 = "{0}의 나이는 {1}이고 키는 {2}입니다."\
#     .format(name, age, height)
# # 인수        0     1     2

# # 참고
# # str3 = "{1}의 나이는 {0}이고 키는 {2}입니다."\
# #   .format(age, name, height)

# print("오늘 먹은 사과는 모두 {0}개입니다.".format(3))
# print("오늘 먹은 사과는 모두 {count}개입니다.".format(count=3))

# str3 = "{0}의 나이는 {1}이고 키는 {height}입니다."\
#     .format(name, age, height=175.3)

# print(str3)

# #중간에 변수가 들어가면 오류 발생한다.
# # str3 = "{0}의 나이는 {1}이고 키는 {height}입니다."\
# #     .format(name, height=175.3, age)
# # print(str3)

# # 이것은 정상 진행
# str3 = "{0}의 나이는 {age}이고 키는 {height}입니다."\
#     .format(name, height=175.3, age=34)
# print(str3)

# #####################################################################


# ################################################################################
# # 문자열 포매팅 4
# # f문자를 이용한 포멧팅 (주로 많이 사용)
# name = '이숭무'
# age = 26
# height = 175.3

# # 이숭무의 나이는 25살이고 이숭무의 키는 175.3입니다.
# print(f"{name}의 나이는 {age}살이고 {name}의 키는 {height}입니다.")

# # 함수란 이미 만들어져있는 기능
# # 함수는 찾아서 사용해라 (외우지 말자)
# # 파이썬 문자열 함수 찾아서 사용해라

# "life is too short"
# # 문자열 가공 : 문자여ㅑㄹ 함수
# a="hobby"
# #문자의 길이
# print(len(a))
# #특정문자의 갯수
# #문자b가 몇개?
# print(a.count('b'))
# print(a)
# print(a.count('o'))


# str1 = "Lite is too short"
# #       01234567890123456
# #                 1

# print(str1)
# print(str1[8:8+3])
# print(str1.index("t"))
# idx = str1.index('too')
# size=len('too')
# print(str1[idx:idx+3])
# # 맨뒤에 t는 rindex 함수를 사용한다 index함수는 왼쪽정렬이다.
# indexnum=len(str1)
# print("마지막이 t인가?")
# print(str1.index('t',indexnum-1))

# idx = str1.index('t')
# print(str1.index('t', idx +1))


# #문제 too부터 모든t를 가져와라
# idx = str1.index('t')
# print(str1.index('t'),idx+1)

# idx=str1.index('too')
# print(str1[idx:])


# str1 = "Lite is too short"
# #       01234567890123456
# #                 1

# print(str1.index('too'))
# print(str1.find('too'))
# print(str1.index('t',3))
# print(str1.find('t',3))
# print(str1.rindex('t'))
# print(str1.rfind('t'))

# #find와 index의 차이점
# # 문자열이 없으면 find는 -1을 리턴하고 index 는 에러를 발생시킨다.

# #############################################################################
# str1 = "Life is too short"
# #       01234567890123456
# #                 1

# #대문자 소문자로
# print(str1.lower())
# if str1.lower() == "Life is too short":
#     print('소문자네')
# else:
#     print('소문자 아닌데')
# ############################################################################

# #strip 함수는 문자열 좌우 공백만 삭제 한다. 중간에 있는 공백은 데이터이다!!
# #stripdms 왼쪽공배 오른쪽 공백을 제거 하기위해서는 lstrip() rstrip()
# str3 = "              aaaa         "
# result = str3.strip()
# if str3 == "aaaa":
#     print("같다")
# else:
#     print("다르다")

# print("sldkjf dfkjljk dfkjlj dfkljlk".lstrip("sl")) #양옆에 있는 문자만 제거하는것이다!!

######################################################################################

##################################################################################
# # 단어대체하기
# str1 = "Life is too short"
# #       01234567890123456
# #                 1

# print(str1.replace("Life","Your leg"))
# result = str1.replace("Life","Your leg")
# print(result)
# print(str1)

# #쪼개기 (스플릿하면 결과는 리스트이다.)
# result=str1.split() #스플릿은 구분자로 나눈다. 기본값은 공백이고 구분자가 있다면 split(':') 구분자로 나눈다.
# print(result)
