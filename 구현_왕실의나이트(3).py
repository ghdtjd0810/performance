
# 3. 위치를 정해야지(어디가 어디인지를 알아야 할 위치)
# 행렬? 리스트? 아님 그냥 포문?? 일단 8X8행렬임

# 풀었다 ㅋㅋㅋㅋ 와웅 ~ 잘한다 홍혜쪙
# 문자로 볼 필요도없다. 여기는 내가 푼거
'''
x, y = map(int,input())
count = 8
step = [(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]
                 
for i,j in step:
    nx = x + i
    ny = y + j
    if nx > 8 or nx <1:
        count -=1
    elif ny >8 or ny <1:
        count -=1
    else:
        continue
    nx,ny = x,y


print(count)
'''


# 여기는 교과서

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result +=1

print(result)
