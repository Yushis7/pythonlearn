#%%
#stack 뒤에 넣고 뒤에서 뺴는 자료구조

from collections import deque
a=[]
a.append(0)
a.pop()

#queue 뒤에 넣고 앞에서 뺴는 구조

b= []
b.append(0)
b.pop(0)

#stack queue

c=deque()
c.append(1)
print(c)
c.appendleft(2)
print(c)
c.pop()
print(c)
c.popleft()
print(c)

