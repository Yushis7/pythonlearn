#%%

if True:
    pass

a=None #아무것도 없다

a.split()
b=[1,2,3,4]

print(b[4])

'''try except'''
#%%
x = None
try:
    x.ok() #에러
    print(1234)
except:
    print('예외발생')
else:
    print('정상실행')
finally: #실행되든 안되든 무조건 finally 실행
    print('무조건 실행되는 것')

#%%
x = None
try:
    raise IndexError()
    print('실행구문')
except:
    print('예외발생')
else:
    print('정상실행')
finally: #실행되든 안되든 무조건 finally 실행
    print('무조건 실행되는 것')
    #%%
    '''raise 응용'''
try:
    for i in range(10):
        for j in range(10):
            if j == 5:
                raise
            print(i,j)
except:
    pass
#맞는데 왜 안되지?
#%%
'''함수 내에서 finally'''
def f():
    try:
        return
    except:
        pass
    else:
        print('else')
    finally:
        print('finally')
f()

