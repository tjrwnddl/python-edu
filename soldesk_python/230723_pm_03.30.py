# bool type
a=True

a=1
b=2
print(b<a)

mat=40
eng=80
result=mat>=40 and eng>=40 and (mat+eng)/2 >=60
print(result)    

# 비교(관계)연산자 : < , > ,>=, <= , == , != : 결과는 부울타입
mat = 40
eng = 80
#각 과목이 40점이상이고 평균이 60점 이상이면 True
result = mat >= 40 and eng >= 40 and (mat+eng) / 2 >= 60
print(result)
result = mat >= 40 #비교연산
print(result)
### 2200년은 윤년일까요(True)? 평년일까요(False)? 
### 4년마다 윤년이지만 100년마다는 윤년이 아니다 그렇지만 400년마다는 윤년이다.
#논리연산과 비교연산
result = 2200 % 4 == 0 and 2200 % 100 != 0  or  2200 % 400 == 0
print(result) # False(평년)

print(bool('마이클'))
print(bool('')) #blank , False
print(bool(-1))
print(bool(1))
print(bool(0)) #False
print(bool([1,2,3,4]))
print(bool([])) #False
print(bool((1,23)))
print(bool(())) #False
print(bool({1:'a'}))
print(bool({}))#False
print(bool(None)) #False



#파이썬의 변수 선언법

t=1,2,3,4
print(t)
a, b = 1, 2
print(a)
[a,b]=[1,2]
a,b,c=1,2,"lee"
print(c)


###################################################
a, b = 10, 20
a,b=b,a
print(a,b)