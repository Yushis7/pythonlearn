#%%
'''
list comprehension
'''
a=[1,4,5,6,7,10]
b=[]
for x in a:
    b.append(x*2)
print(b)

a=[1,4,5,6,7,10]
b=[x*2 for x in a]
print(b)
#같은 방법 더 짧거나 맘에 드는걸로

a=[1,4,5,6,7,10]
pivot = 5
for x in a:
    if x> pivot:
        b.append(x)
print(b)

a=[1,4,5,6,7,10]
pivot = 5
b = [x for x in a if x > pivot]
print(b)

#이렇게 코드도 짧아지기도 하는데 많이 쓰기도 함
#%%
#%%
'''unpacking'''

a=1,2,3

def f(x,y,z):
    return x+y+z

print(f(a[0],a[1],a[2]))
#복잡하니 짧게만드려면

a=1,2,3

def f(x,y,z):
    return x+y+z

print(f(*a))

#만약 추가한다면?

a=1,2,3

def f(x,y,z,w):
    return x+y+z+w

print(f(*a,1))
# *a 앞뒤에 아무것도 안붙이면 오류가 나지만
#*a에 아무 숫자 붙여놓으면 알아서 계산 됨

a=1,2,3

def f(x,y,z,w):
    return x+y+z+w

print(f(*a,1))

x = '1','2','3','4'
y = [*map(int,x)] # = [1,2,3,4] 와 동일
print(y)

#%%


a=1,2,3

def f(x,y,z,w):
    return x+y+z+w

print(f(*a,1))

x = '1','2','3','4'
y = [*map(int,x)] 
z = {1:'손',2:'흥',3:'민',1999:'최고'} #이게 딕셔너리
w = z
z[1] = '갓'
print(z[1])

#%%
'''lambda'''
def a(x):
    return x*x + x + 1
def b(key,x):
    return key(x)

print(b(a,1))
#가 너무 길으니

def b(key,x):
    return key(x)

print(b(lambda x :x*x + x + 1,1))
lambda x: x*x+x+1

#%%
'''global'''
# glo = 0 #전역변수?

# def function(a,b,c,d):
#     local = 0 #지역변수

glo = 0 
def function(a,b,c,d):
    print(a,b,c,d)
    print(glo) #전역변수는 보통 읽기전용으로 쓰임

function(1,2,3,4)
# %%
