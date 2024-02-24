#%%

a=[1,2,3,4]
print(a)

# b=['1',True,false,12,1.5]
# print(b)

print(a[2]) # 0-base

a[0]='다른 거'
print(a[0])
print(a)
#중간에 다른걸로 바꿔치기

a.append(5)
print(a)

a.append(True)
print(a)
#추가하기

a.insert(2,'집어넣기')
print(a)
#3번쨰 자리에 집어넣기

print(a.pop())
print(a)

print(a.pop(2))
print(a)
#del보단 pop을 더 많이 씀 

del a [0]
print(a)
#삭제


# %%
#배열 인덱싱
b=[0,1,2,3,4]
print(b[len(b)-1])
print(b[-5])

c='abcd'
print(c[-1])

# %%

#if문에서 리스트

a =[]

if a:
    print('있음')
else:
    print('없음')
    

# %%
#배열 슬라이싱

a=[1,2,3,4,5,6,7,8,9,10]
print(a[2:6]) #begin <=x< end
print(a[:6]) # 0쓰는거 귀찮다 생략하자
print(a[6:])

print(a[::2]) #두 칸 간격으로 

print(a[1:8:2]) #1~8까지 2씩 간격으로

print(a[0:-1])#0부터 끝까지 단 끝에 하나 뺴

print(a[::-1]) #거꾸로
print(a[::-2]) #거꾸로 2씩차감

#펠린드롬
a='abaa'
print(a==a[::-1])

# %%
#리스트의 얕은 복사
a=[0,1,2,3]
b=a
print(b)
b.append('Last ele')
print(b)
print(a) 
#파이썬에서 리스트는 
# A -> 메모리 주소 ->[0,1,2,3]
# B = a
# b -> 메모리 주소 ->
# b.append('마지막 원소')
#%%
a=[0,1,2,3 , [1,2,3,4]]
b=a[:]
print(b)
b[-1][0] = '첫번쨰 원소'
print(b)
print(a) #얕은 복사,깊은 복사 


# %%

a='abcd'
a[0]='1'
print(a[0])


# %%

#다차원 리스트
lst = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]

print(lst[1][1][0])

# %%

#리스트 연산
print('p'*3)
print('ab'+'cd')
print([1,2,3]*3)
print([1,2,3] +[4,5])


# %%
