n,m=map(int, input().split())
li=list(i+1 for i in range(n))
for k in range(m):
    i,j=map(int, input().split())
    while j>i:
        temp=li[i-1]
        li[i-1]=li[j-1]
        li[j-1]=temp
        i=i+1
        j=j-1
for k in range(n):
    print(li[k], end=" ")
