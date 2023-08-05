#numpy
#pip install numpy
# python 기본 자료형:정수,실수,문자열,리스트,튜플,딕셔너리,집합,부울
# numpy : 배열자료형 : 숫자만 다루는 배열
import numpy as np
# num = np.random.randint(45)
# print(num)

# num = np.random.randint(46,size=6)
# print(num)

# l=[5,6,0,4,8,3]
# print(l)
# print(num)

# num = np.random.randint(1,45,size=(2,6))
# print(type(num))

# print(num[0,4])

# num3 = np.random.randint(1,10, size=(3,4))
# print(num3)
# '''
# [[32, 10, 20, 22]
#  [33, 19, 19, 26]
#  [28, 13, 26, 14]]
# '''
# l=[[32, 10, 20, 22],
#  [33, 19, 19, 26],
#  [28, 13, 26, 14]]
# print(l)
# print(num3)
# #배열을 만드는 방법

# i=np.random.randint(10,size=(3,4))
# print(i)

# #arrange함수사용
# print(np.arange(0,9))
# i2=np.arange(9).reshape(3,3)
# print("test",i2)
# i3=np.array([1,2,3])
# print(i3)
# # #array함쉬이용
# i9=np.array([2,5,7])
# print=print(i9)

l11 = [1,2,3]
l12 = [3,2,1]
l13 = l11 + l12
print(l13)
l14 = []
i=0
while i < len(l11):
    l14.append(l11[i]+l12[i])
    i +=1
print(l14)
