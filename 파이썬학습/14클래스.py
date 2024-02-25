#%%
'''
클래스
객체지향
객체,인스턴스
다형성,캡슐화
'''

# class A:
#     pass
# a = A()

# a.x=1 

# print(a.x)

# b=A()

# print(b.x)

class A:
    def __init__(self,name,number,score) -> None:
        self.name = name
        self.number = number
        self.score = score 
        #__만 쳐도 init자동완성 나옴
a=A('욱',3,100)

print(a.name,a.number,a.score)    

b=A('승',4,0)

print(b.name,b.number,b.score)

# %%
class A:
    def __init__(self,name,number,score) -> None:
        self.name = name
        self.number = number
        self.score = score 
        #__만 쳐도 init자동완성 나옴
    def to_string(self):
        return 'name : {} , number : {}, score : {}'.format(self.name,self.number,self.score)

a=A('욱',3,100)

print(a.name,a.number,a.score)    

b=A('승',4,0)

print(b.name,b.number,b.score)
