# def sum(a,b):
#     return a+b

# y=sum(3,4)
# print(y)

# #함수의 4가지 유형
# #1. 입력값(parameter가 있다.) 이 있고 출력값(return)도 있는경우
# def add(x1, x2): #x1, x2입력값
#     result = x1 + x2
#     return result # result 출력값

# y=add(3,5)
# print("# 1. 입력값(parameter가 있다.) 이 있고 출력값(return)도 있는경우")
# # print(y)


# # 2. 입력값은 있고 출력값이 없는경우
# def add2():
#     x1 = int(input("첫번째 수를 입력해주세요. : "))
#     x2 = int(input("두번째 수를 입력해주세요. : "))
#     result = x1 + x2
#     return result
# print("# 2. 입력값은 있고 출력값이 없는경우")
# y=add2()
# print(y)

# # 3. 입력값은 있고 출력값이 없는경우
# def add(x1,x2):
#     result = x1 + x2
#     print(result)
# print("# 3. 입력값은 있고 출력값이 없는경우")
# add(4,3)

# # 4. 입력값이 없고 출력값도 없는경우
# def add():
#     x1 = int(input("첫번째 수를 입력해주세요. : "))
#     x2 = int(input("두번째 수를 입력해주세요. : "))
#     result = x1 + x2 
#     print(result)
# add()

# def sum():
#     sum=0
#     for num in range(1,101):
#         sum += num
#     print(sum)

# # sum()

# def sum1(start, end):
#     sum=0
#     for num in range(start,end+1):
#         sum += num
        
# #    print(sum)
#     return sum

# y=sum1(1,100)
# print(y)

# 15시 30분
# #parameter 이름을 이용해서 값을 전달 # 많이 사용하고 있음.
# y = sum1(end=100, start=1)
# print(y)

# def sum12(a,b,c,d):
#     print(a+b+c+d)

# sum12(1,2,3,4)
# sum12(a=10, b=5, c=7, d=3 )
# sum12(10, 5, c=7, d=3 )

# def sum11(* a):
#     result=0
#     for i in a:
#         result += i
#     print(result)

# sum11(1,2)
# # sum11(1,2,3)
# # sum11(1,2,3,4,5)

# t=1,2,3,4,5
# print(t[0])

# def sum13(* a):
#     print(a)
#     result = 1
#     if a[0] == "add":
#         result=0
#         for i in range(1,len(a)):
#             result+=a[i]
#     elif a[0] == "mul":
#         for i in range(1,len(a)):
#             result*=a[i]
#     elif a[0] == "sub":
#         result=0
#         for i in range(1,len(a)):
#             result-=a[i]
#     print(result)


# sum13("add",1,2)
# sum13("mul",1,2,3)
# sum13("sub",1,2,3,4,5)


# def add_mul(x,y):
#     i = x+y
#     j=x*y
#     return i,j
# #함수의 기본 : 결과값은 오직 하나이어야 한다.

# y = add_mul(2,4)
# print(y)


# def calu(opt,a,b):
#     if opt == "add":
#         return a+b
#     else:
#         print('할수없다.')

# calu = lambda opt,a,b: a+b if opt == "add" else print("덧샘만가능.")#none 올수밖에 없고 이것을 하고자 한다면 리턴값으로 받지 말아야 한다. 
# calu = lambda opt,a,b: print(a+b) if opt == "add" else print("덧샘만가능") 
# calu("sub",4,5)


# 전역변수 함수밖에 있는 변수
# 지역변수 함수 안에 있는 변수

#17시
# 파일입출력!!
# 데이터를 파일에 저장하거나 파일에 있는내용을 가지고 오는것.
# f = open("D:\for_devel\python-edu\soldesk_python\hello.py",'w',encoding="UTF-8")
# f = open("test1.py",'w',encoding="UTF-8")
# f.write("1번째 줄입니다. \n")
# f.write("2번째 줄입니다. \n")
# f.write("3번째 줄입니다. \n")
# f.write("4번째 줄입니다. \n")
# f.write("5번째 줄입니다. \n")

# f.close()

# f= open("test.py",mode="a",encoding="UTF-8")
# for i in range(11,21):
#     f.write(f"{i}번째 줄입니다.\n")
# f.close()

# f= open("test.py",mode="r",encoding="UTF-8")
# lines = f.readlines()
# print(lines)

# print("".join(lines))


# 화일 읽기
# f= open("D:\\for_devel\\python-edu\\soldesk_python\\20230715pm.py",mode="r",encoding="UTF-8")
# data=f.read()
# print(data,end="")

# with open("test1.py",mode="w",encoding="UTF-8") as f:
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")
#     f.write("1번째에요\n")


with open("test1.test",mode="w",encoding="UTF-8") as f:
    for i in range(1,11):
        f.write(f"{i}번째입니다.\n")
