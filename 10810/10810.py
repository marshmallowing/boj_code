n,m=map(int, input().split())
array=[0 for i in range(n)]
for i in range(m):
    start,end,num=map(int, input().split())
    for j in range(start-1, end):
        array[j]=num
for i in range(n):
    print(array[i],end=" ")
