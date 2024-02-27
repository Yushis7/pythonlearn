#%%
# print(map(int,input().split()))

a=[1,2,3,4,5]
b=[1,4,9,16,25]
c=list(map(lambda x:x*x, a))
print(c)

#%%
#min max sum

print(max(range(11)))
print(min([1,5,7,1,45,7,2,3,5]))
print(max([1,5,7,1,45,7,2,3,5]))
print(sum([1,5,7,1,45,7,2,3,5]))

#%%
#random
import random

print(random.randint(0,10)) 
#0~10사이 랜덤 정수 만들기

#%%
#sort함수

a=[1,3,7,2,1,3,3,5]
a.sort()
print(a)


a=[1,3,7,2,1,3,3,5]
b=a[:] #a복사본
b.sort()
print(a,b)

a=[1,6,3,3,5,111,7]
b=sorted(a)
print(a,b)


#%%
import bisect
import random
#이분탐색
#정렬된 배열 X,logN

# a= [ random.randint(0,100) for_in range(10) ]
a = [random.randint(0, 100) for i in range(10)]

#랜덤으로 0~100 10개 만들기
print(a)
print(bisect.bisect_left)

#%%
import itertools
a = [1,3,5]

print(*itertools.combinations(a,2))
#1,3,5의 경우의수 만들기
print([*itertools.combinations_with_replacement(a,2)])
#중복 조합만들기
print([*itertools.permutations(a,2)])
#순열만들기
print([*itertools.product(a,a)])
#a,a로 가능한 모든 순서쌍 만들기
print([*itertools.product(a,repeat=3)])
