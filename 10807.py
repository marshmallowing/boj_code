n=int(input())
li=list(map(int, input().split()))
v=int(input())

cnt=0
for i in li:
    if(i==v) : cnt+=1
print(cnt)

#print(li.count(v)) 이렇게 축약 가능