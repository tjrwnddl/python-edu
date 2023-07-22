#제어문 
# bool타입을 이용해서 원하는 결과를 가져오는 것
## 조건식은  비교연산식 또는 논리연산식
## 조건식의 결과에 따라 실행되거나 안된다.
## 조건식이 True이면 if문 안에 있는 명령어가 실행이 된다.
## if문 안에 있는 명령어는 Tab이나 공백문자를 이용해서 들여쓰기가 되어야한다.
## 하지만 두개 혼용할 수 없다. tab을 많이 사용한다.
### 조건식 뒤에는 :이 와야 한다.
'''
if  조건문:  # True 
    명령어1
    명령어2
    ...
    명령어n
'''


if '':
    print("참")
else:
    print("거짓")

###############################################################

#  단일 if
a = 10
if a < 20: #True
    print("a는 20보다 작다.")#if문 안에 있는 명령문
    
    print("안녕")#if문 안에 있는 명령문
print("if문 끝") # if문 밖에 있는 명령문

if a > 20 : #Fasle
    print("a는 20보다 크다.") #if문 안에 있는 명령문
    
print("if문의 끝") # if문 밖에 있는 명령문



######################################################
#in연산자 사용하기
l = [1,2,3,4,5,6]
if 4 in l:
    print("포함되어있네")
print( 4 in l) # 포함되어 있으면 참/ 아니면 거짓
print(10 in l)
print(10 in [1,2,3,4,5,6])
print(7 not in l)

print( "y" in "python")
print( "yt" in "python")
print( "이" in "python")
print( "이" not in "python")

print(6 in (1,2,3,4,5,6))
print(6 in {1,2,3,4,5,6})

print(1 in {1:'이', 2:'숭'}) #키가 있는지


### 영어가 40이상이고 국어가 40이상이고 수학이 40이상일때,
#평균이 60 이상이면 합격 아니면 불합격
mat = 100
eng =70
kor= 40
result=(mat+eng+kor)/3

#if mat >= 40 & eng >=40 & kor >= 40 | result >=60:
if result >=60 and mat >= 40 and eng >=40 and kor >= 40:
    print('합격')
else:
    print("당신의 성적평균은",result,'이므로 불합격')


#score가 60이상이면 message 변수에 success를 아니면 message 에 failure를 저장한 후 출력

score = 78

# if score >= 60:
#     message="success"
# else:
#     message="failure"

message = "success" if score >= 60 else "failure"


print(message)


# 사직연산
a = 10; b = 20; opt = "add"
if opt == 'add':
    result = a + b
elif opt == 'sub':
    result = a - b
elif opt == 'mul':
    result = a * b
else:
    result = a / b
print(result)


if opt == 'add':
    result=a+b
else:
    if opt=='sub':
        result = a-b
    else:
        if opt=='mul':
            result=a*b
        else:
            result=a/b

print(result)

#python style
result = a+b if opt == "add" else(a-b if opt == 'sub' 
                                  else( a*b if opt == 'mul' 
                                       else a/b))
print(result)

for i in range(1,11):
    print(f"나무가 {i}번 찍으니 넘어간다!!" )