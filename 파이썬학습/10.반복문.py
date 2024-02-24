# %%
'''반복문 for'''

'''
학생1
학생2
학생3
'''
'''
학생100
'''
a=[1,2,3,4]

# for x in a:
#     print(x)

합 = 1
for x in a:
    합 *= x #1x2x3x4를 만든다
print(합)

''' 최솟값을 구하라'''
최솟값 = 10
for x in a:
    if x < 최솟값:
        최솟값 = x #a가 최솟값보다 작으면 갱신한다
print(최솟값)

최댓값=0
for x in a:
    if x < 최댓값:
        최대값 = x
print(최댓값)

# %%
'''
range
'''

# for x in range(10):
#     print(x)
#     #0~10이전까지 출력
# #range(10): = (1,2,3,4,5,6,7,8,9)

# for x in range(100):
#     print("천번찔러")

# for _ in range(100):
#     print("천번찔러") 
# # x가 아니라 _는 아무의미가 없단 뜻

# for x in range(1,10):
#     print(x)
#range(1,10): = (1,2,3...9)

# for x in range(1,10,2):
#     print(x)

for x in range(10,-1,-2):
    print(x)
# %%
'''
리스트 내부에 어떤 원소가 있는지 확인'''

# arr=[0,3,6,8,10]
# check= False
# for x in arr:
#     if x == 3:
#         check = True
# print(check)
#arr안에 3이 있으니 True가 뜨고 4를 넣음 없으니 False가 뜸

# arr=[0,3,6,8,10]
# check= False
# for x in arr:
#     if x == 3:
#         check = True
#         break

# for i in range(10):
#     for j in range(10):
#         if j == 5:
#             break
#         print(i,j)

'''위 방식이 너무 길기게 파이썬은 짧게 간다'''
arr=[0,3,6,8,10]
print(3 in arr)
print(0,1,2,3,4 in arr)
print([0,1,2,3,4] in arr) #무작위로 넣는건 안되네
print(range(10) in arr) #이것도 안되고

# %%

'''while 반복문
잘못쓰면 무한 반복할 수 있다'''

# i=0
# while i < 10:
#     print(i)
#     i += 1 #무한반복

# i=0
# cnt = 100
# while i < 10:
#     print(i)
#     cnt -= 1
#     if (cnt == 0):
#         break #이렇게하면 100번 반복 후 끝

# while True:
#     menu = input('좋아하는 메뉴는')
#     if menu =='고기':
#         print("good")
#     elif menu == '나가자':
#         break
#     else : 
#         print('bad')
#         break
    


# %%

lst = list(range(100))

while lst:
    a= lst.pop()
    print(a)

'''반복문 else'''
for i in range(10):
    print(i)
    if i == 9:
        break
else:
    print("완료")

i = 0
while i<10:
    print(i)
    if i == 9:
        break
else:
    print("완료")  


