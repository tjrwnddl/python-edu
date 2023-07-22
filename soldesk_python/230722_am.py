# 리터럴 : 자연어 : 문자, 문자열 : " " or ''
        #    자연수 : 정수 : 10,20,3
        #             실수 : 10.5, 0.5
        #    논리형 : 참, 거짓

# 리스트 자료형 부터 시작!!!
# 리스는 여러가지의 값을 가진 자료형이 필요함!! 
# list=[1,2,3,4,5,6,12,"hello"]
# print(list[3:])

# list2=list[5:7]
# a=list2
# print(a)
# print(type(a))

def list_test():
    str1="Life is to short"
    l1 = str1.split()
    print(l1)
# 한개는 자료형이 될수가 없다.

#list_test()

# 리스트의 종류
# l2=[] #빈리스트
# l3=[1,2,3,4,5] # 정수형리스트
# l4=["이숭무", "이상범"]  # 문자형 리스트
# l5=[1,2,3,4,5,6] #혼합형리스트
# l6=[[1,2,3,4,5], [3,4,5,6,7]] #리스트 포함 리스트
# l7=[1,2,"gd",[1,2,3,4,"ekjf"],1,4,3] #혼합형 리스트
def variable():
    global str1
    global c
    str1 = "Life is too short"
#       01234567890123456
#                 1
#      -76543210987654321
#              1
    c=['Life','is','too','short']

#variable()

def list_indexing():
    global str1
    str1 = "Life is too short"
#       01234567890123456
#                 1
#      -76543210987654321
#              1
    print(str1[3])
    print(str1[-14])
    l=[1,2,3,4,5,6,7,8] #리스트에 있는 각각의 값을 요소라 함
#  0 1 2 3 4 5 6 7 
# -8 7 6 5 4 3 2 1
    print(l[3])
    print(l[-6]) # indexing을 하면 요소가 가지고 있는 자료형으로 출력
    print(l[3] + l[7])
    l1=str1.split()
    print(l1)
    print(l1[1])
    print(l1[0][3])
    
#list_indexing()


def index_slicing():
    #e i
    print(str1[3:3+3])

    #print(str[1] + str[2])
#index_slicing()


def modify_list():
    c=['Life','is','too','short']
    str1 = "Life is too short"
    print("1test",c[0])
    c[0] = "your log"
    print("2ts",c)
    str2=str1.replace("Life", c[0])
    print(c[0])
    print(c)
    print("test"+str2)
    #replace 함수에 대해서 다시 한번 확인!!
    #바뀔문자열에 대문자 소문자 구분 안했더니 인식을 못해서 안바뀜

#modify_list()

def list_append():
    ### 리스트에 요소 추가 
    # append()
    l1 = ['Life','is'] #문자열을 가진 리스트
    # 요소 'is' 뒤에 'too'를 추가  ['Life','is','too']
    l1.append("too")
    
    l1.append(3)
    print(l1)
    l1=['life','short']
    l1.insert(1,"is")
    print(l1)
    l1.insert(2,"too")
    print(l1)
    a=[1,2,3]
    l1.append(a)
    print(l1)
#list_append()

def list_component_del():
    #요소 삭제
    l1 = ['Life', 'is', 'too', 'short', 1, 2, 3]
    #        0       1      2      3     4  5  6
    # indexing을 이용해서 요소 삭제
    del l1[4]
    print(l1)
    print(l1[2:2+2])
    del l1[1:]
    print("te",l1)
    # 요소를 이용해서 삭제
    l1 = ['Life', 'is', 'too', 'short', 1, 2, 3]
    #        0       1      2      3     4  5  6
    l1.remove("short")
    l1.remove(1)
    l1.remove("is")
    print(l1)
    
    l1 = ['Life', 'is', 'too', 'short', 1, 2, 3]
    #        0       1      2      3     4  5  6
    result=l1.pop(3) # pop함수는 맨 마지막 값을 삭제가 기본이고 원하면 인덱스 번호를 주면된다.
    print(result)
    print(l1)

#list_component_del()

def sort_list():
    l = [4,2,5,1,3]
    #오름차순
    l.sort()
    print(l)
    l.sort(reverse=True)
    print(l)
    l = [4,2,5,1,3]
    l.reverse() #리버스 함수는 리스트를 뒤집어준다.
    print(l)
    l=['b','a','c']
    l.sort()
    print(l)
#sort_list()

def tuple_test():
    l=[1,2,3,4,3]
    t=(1,2,3,4,3)
    print(l[1:1+2]+[10])
    #튜플은 변경 불가하다!!

#tuple_test()


def changel():
    # 질문
    str1 = "hello"
    print(str1)
    l=list(str1)
    print(l)
    t = tuple(str1)
    print(t)
    a = "1"
    print(str(10) + a)
    print(10 + int(a))
    print(10 + float(a))

changel()

dic={}
dic1={'name':'이승무', 'age':35, 'height':175.5}
print(dic1['name'])
#print(dic1[0]) #KeyError: 0
#딕셔너리는 index를 사용하지 않는다 키와 index는 중복될수 있다.
# 딕셔너리는 키의 중복을 허용하지 않느다.
# 키가 없으면 딕셔너로 요소를 만들고 있으면 키에 대한 값을 변경한다.
dic={}
dic1={'name':'이승무', 'age':35, 'height':175.5}
l=[1,2,3,4]
del l[1]
print(l)
del dic1['age']
print(dic1)
#키만 가져오기
print(dic1.keys())
#밸류만 갑져오기
print(dic1.values())
#키와 값을 쌍으로
print(dic1.items())
print(l)
l.clear() # 리스트 비우기
print(l)
dic1.clear() # 딕셔너리 비우기
print(dic1)