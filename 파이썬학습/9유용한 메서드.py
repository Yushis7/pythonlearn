# # %%
# # '{}'.format(1)
# #'{},{}'.format(1) 이건 안되네
# # '1,2,3,4,5,6,7,8'.split(',') #,를 다 없애고 리스트 문자열로 바꿈
# # 
# '1,2,3'.split(',')
# # map(int,a)'{}'.format(1,2) #굴러'1,2,3,4,5,6,7,8'.split(',') #,를 다 없애고 리스트 문자열로 바꿈
# a=# 
# b=list('1,2,3'.split(','))
# # map(int,a)는 가는데 1만 뜨네
# a=# 'ormat(1,2) #인덱스 순서 바꾸기
# b=blist(= list())

# import math
# '{:2F}'.format(math.pi)  #소수 2쨰자리
# '{:3F}'.format(math.pi)

# %%

#SPLIT

# '1 2 3 4 5 6 7 8'.split() # 리스트 문자열로 만들어줌
# '1,2,3,4,5,6,7,8'.split(',') #,를 다 없애고 리스트 문자열로 바꿈

a = '1,2,3'.split(',')
# b=list(map(int,a))
b = list(map(float,a))
# %%
