# 10811_python
       
     while j>i:
        temp=li[i-1]
        li[i-1]=li[j-1]
        li[j-1]=temp
        i=i+1
        j=j-1
     #리스트 역순으로 출력하기_my code

***
### 1. 인덱스를 이용한 역순 출력

    #내가 생각한 코드
    li=li[i-1:j:-1]
 
###### 두가지 문제점 존재
##### 1) 역순 인덱스 사용 방식의 오류
[3:0:-1] : 3번 인덱스부터 1번 인덱스까지(0번 까지가 아님) 역순으로 반환
[4::-1] : 4번 인덱스부터 0번 인덱스까지 역순으로 반환
[::-1] : 리스트 전체를 역순으로 반환

=> li[i-1:j]=li[j-1:i-2:-1] 이렇게 수정

##### 2) i가 1일시 i-2<0 상황 발생
![image](https://github.com/marshmallowing/boj_code/assets/114673063/4707a61d-cc76-4630-b4fd-b1791f55f1e0)

=> 결과적으로 인덱스를 이용해 한번에 역수 변환 방식은 오류 발생

    for i in range(m):
    i,j=map(int, input().split())
    temp=li[i-1:j]
    temp.reverse() #reverse() 함수 이용
    li[i-1:j]=temp
    #이렇게 temp를 이용한 방식은 문제없이 출력

### 2. reverse(), reversed()
- list.reverse() : 리스트를 역순으로 취해주는 함수
단, 함수 자체의 반환 값은 없음

- reversed(list) : 역순으로 취한 리스트를 반환해줌
