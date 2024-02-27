d={}

d['1'] = 3
d['3'] = 5
d['555'] = 1243

print(d)

#숫자 범위는 큰데 자료 갯수는 많지 않을 때
#문자열에 이것저것 대응이 될 떄

#%%
d={1:'a',2:'b',3:'c'}
print(d)
for x in d:
    print(x)
#숫자만
for x in d:
    print(x,d[x])
#숫자랑 문자 같이
for x in d.items():
    print(x)
#소괄호로 감싼채로
for k,v in d.items():
    print(k,v)
print('a'in d.values())
#어떤 숫자가 dictionary 안에 key로써 존재한느가?
if 3 in d:
    print(d[3])
#d안에 3이 있는가?

#set
S =set([1,1,3,3,5,5,6,7,7,7])
print(S)
#set은 중복을 허용치 않음 
#set은 list와 비슷하지만 list에 비해 탐색속도가 빠르다
#아마 sort방법이 set이 더 효율적인걸 쓰는듯?


