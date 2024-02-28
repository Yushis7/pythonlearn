print('a','b','c' , sep='\n')
# print('S','E','P', sep='@')

# print("I like", end=" gold and ")
# print("money")

# %%
print('hellow world')
# %%
print('hello','python','world',end='**love**')
print(0000)
print(1,2,3,4)
print(1,2,3,4, sep=',')
# %%
print(type(1)) #정수형
print(type(1.5)) #실수형
print(type(True)) #불 참거짓 판단용
print(type('문자열')) #문자열 str

print('중요한 것은 꺾이지 않는 마음')
print("중요한 것은 꺾이지 않는 마음")
print("'중요한 것은 꺾이지 않는 마음'")
print('"중요한 것은 꺾이지 않는 마음"')
print('"\'중요한 것은 꺾이지 않는 마음"') #이스케이프 문자
print('중요한 것은 \n 꺾이지 않는 마음')
print('''중요한 것은
      꺾이지 않는 마음''') #'''세개면 \n없이 띄어쓰기 가능
print('''\
중요한 것은
꺾이지 않는 마음\
''') #좀 더 깔끔하게 만들기

print('중요한 것은' + '꺾이지 않는 마음') #문자열 더하기로 표현가능
print('중요한 것은' *3 + '꺾이지 않는 마음')

print('내가 간 곳은' + str(3) + '번지다')
print( int('3'))  #정수
#print('나는' +int('3') + '도로를 탄다') 문자 안에 정수넣고 표현 어떻게하지?
print(len('abcd')) #글자갯수


# %%
#%%
print((1+2)*3)

def add(a, b):
    return a + b

print(add(1, 2))

a=(1,2,3)
print(a)
#%%
# 세트 만들기
s = {1, 2, 3}
print(s)

# 딕셔너리 만들기
d = {'a': 1, 'b': 2, 'c': 3}
print(d)

# 집합 표현식 만들기
a = {1, 2, 3}
b = {2, 4, 6}
c = a & b  # a와 b의 교집합
print(c)
#%%
def return_tuple():
    return (1, 2, 3)

x = return_tuple()
print(x)

#%%
# s = {1, 2, 3}
# print(s)  # {1, 2, 3}
# print(s[0])  # 에러: 세트에는 인덱싱이 없습니다.

# l = [1, 2, 3]
# print(l)  # [1, 2, 3]
# print(l[0])  # 1
# print(l[1])  # 2
# print(l[2])  # 3

s = "This is a \"quote\"."
print(s)

s = "This is a line with a space.\n"
print(s)

s = 'This is a \\n newline.'
print(s)

s = "This is a line \n with a space. "
print(s)