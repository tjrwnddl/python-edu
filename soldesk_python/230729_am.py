# 1~100의 홀수의 값만 출력
# i = 0
# sum = 0
# while True:
#     i += 1
#     if i > 100:
#         print("반복종료")
#         break
#     if i % 2 == 0:
#         continue
#     sum += i

# print(i)
# print(sum)


# # 리스트에 있는 합을 구하시오!
# idx=0
# total=0
# ftotal=0
# l=[34,76,99,45,78,89]
# cnt=len(l)-1 #인덱스 최종번호 5
# #cnti=len(l)-1
# print(cnt) 
# #while 문이용  
# while True:
#     # print(idx)
#     total += l[idx]
#     idx += 1
#     if idx > cnt:
#         # print("종료")
#         break
# print(total)

# # for문이용
# for i in l:
#     ftotal += i
#     # print(ftotal)

# print(ftotal)


# t = (111,333,45,666,535)
# sum = 0

# # for문은 바로 가져오기때문에 간결!
# for num in t:
#     sum += num
# print(sum)

# idx=0
# sum=0
# #while은 인덱스를 이용해야한다. 복잡!
# while idx < len(t):
#     sum += t[idx]
#     idx += 1
# print(sum)

# # 1~100까지의 합을 구하세요
# i=1
# sum=0
# while i < 101:
#     sum += i
#     i += 1

# print(sum)

# sum=0
# for i in range(1,101,1): #1부터 101미만까지 1씩 증가 시켜 반복 시키겠다.!
#     sum += i
# print(sum)

# 1~100까지의 합중 홀수 합만 구해요
# i=0
# sum=0
# while i < 100:
#     if i % 2 == 0:
#        pass
#     else:
#         sum += i
#     i += 1

# print(sum)

# import random
# lotto=[]
# for i in range(1,46):
#     lotto.append(i)

# size=len(lotto)
# print(size)

import random
qty = int(input("수량을 입력해주세요. : ")) # 1입력
lotto = []
for cnt in range(qty): #cnt=1 로또 수량 체크
    for num in range(1, 45+ 1): #숫자는 1이상 46미만
        lotto.append(num)  # 45개의 리스트를 생성
    size = len(lotto)      # size는 리스트의 길이를 나타내며 여기서는 45를 이야기함
    #print(lotto,size)      # 로또 리스트와 그 리스트의 길이를 확인
    for i in range(6):      
        size -= 1            # 인덱스 0~5까지 생성
        idx = random.randint(0,size) #인덱스는 
        lottoNum = lotto.pop(idx)
        print(lottoNum, end=", ")
    print()
    lotto.clear()