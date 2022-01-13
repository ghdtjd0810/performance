

n = int(input())

a = 0

for i in range(1,n+1):
    for j in range(1, 61):
        for k in range(1, 61):
             if '3' in str(i)+ str(j) + str(k):
                 a += 1

    
    
print(a)
