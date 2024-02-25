#%%
'''
함수
'''

a=1
b=2
c=3
print(a*a+1,b*b+1,c*c+1)
#이렇게 하나하나 해놓으면 귀찮으니

def f(x):
    print('f함수:',x*x+1)
    

a=1
b=2
c=3

f(a)
f(b)
f(c)
#이것도 길다면?


def f(x):
    return x*x+1

a=1
b=2
c=3
print(f(a),f(b),f(c))

#함수를 늘려서 한다면

def f(x,y=0,z=0):
    return x*x + y +1
a=1
b=2
c=3
f(1,2)

# %%
