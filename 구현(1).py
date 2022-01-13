##구현 답 맞긴 맞았음 ㅋㅋ 근데 푼 시간 1시간 ;;;;;;
'''
n = int(input())
input_button =list(map(str, input().split()))
x, y = 1,1
# 여기서 n을 이용해서 갈수 있는곳과 갈 수 없는 곳을 정해보자. 각 RULD 상황에 맞게.
#R은 좌표리스트의 원소[1] 이 n을 넘어가면 안됨.
#L은 1보다 작으면 안댐[1]
#U는 원소 n1보다 작으면 안댐[0]
#D는 n이 5 넘어가면 안댐. [0]
# 현재의 주소도 필요하겠어.
the_map = []
for i in range(n):
    for j in range(n):
        print([i+1,j+1] , end= ' ')

#내가 푼답인데, 여기 과정의 반복을 효율적으로 바꿔주는 뇌 근육이 부족함.

for i in input_button:
    if i == 'R':
        if n <= y:
            continue
        else:
            y = y+1
    elif i == 'L':
        if 1 >= y:
            continue
        else:
            y = y - 1
    elif i == 'U':
         if 1>= x:
             continue
         else:
             x = x -1
    elif i == 'D':
         if n <= x:
             continue
         else:
             x = x + 1


print(x,y)
'''

#L =(0,1), R = (0,1),  U= (1,0), D=(-1,0)
n = int(input())

x, y = 1 ,1
plans=input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

'''
for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx<1 or ny <1 or nx >n or ny > n:
        continue
    x,y = nx, ny
'''

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        
