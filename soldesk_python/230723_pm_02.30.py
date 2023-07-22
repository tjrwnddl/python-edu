# dic= {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# dic['birth'] = '19981118'
# #               87654321 - 

# #print(dic)
# a=dic['birth']
# print(type(a))
# year=dic['birth'][0:4]
# month=dic['birth'][4:6]
# day=dic['birth'][6:]
# print(year)
# print(month)
# print(day)
# print(type(dic.keys()))

# #print(dic['addr']) # 키가 없으면 에러를 리턴
# print(dic.get('addr')) # 키가 없으면 None를 출력
# print(dic.get('addr','서울')) # 서울
# print(dic) # {'name': 'pey', 'phone': '0119993323', 'birth': '19981118'}

# dic1 = {'classic' : 500 ,  "pop" : 600 }
# dic2 = {'classic' : 500 ,  "pop" : 600, 'money': 100 }
# #dic1'time':100] 딕셔너리 추가하기
# print(dic1)
# print(dic1['pop']) #정수
# print(dic2['pop']) #정수

# print(dic1['pop'] + dic2['pop'])
# print(dic1.get('money',0) + dic2.get('money', 0))
# print(dic1.get('money',0) + dic2.get('money'))

# ################################################################

# l=list((1,2,3,4,5))
# print(type(l))
# s="".join(str(l))

# print(type(s))

# # 집합
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# # 교집합
# print(s1&s2)
# print(s1.intersection(s2))
# # 합집합
# print(s1|s2)
# print(s1.union(s2))
# # 차집합
# print("#차집합")
# print(s1-s2)
# print(s2-s1)
# print(s2.difference(s1))

#########################################################################
# 집합함수
#요소 추가
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.add(7)
print(s1)
s1.add(9)
s1.add('a')
#s1.add(10,11,12) # 에러 발생 여러개 값을 너을수 없다.
s1.add((10,11,12)) #튜플 추가됨
#s1.add([10,11,12]) #리스트 추가안됨
s1.update((10,11,12)) #튜플로 추가하면됨 update함수 쓸때
s1.update([10,11,12]) #리스트도 추가하면됨 update함수 쓸때
print(s1)

#삭제
s1.remove((10,11,12))
print(s1)
