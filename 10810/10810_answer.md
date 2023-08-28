# 10810_python
    
    n,m=map(int, input().split())
    array=[0 for i in range(n)]
    for i in range(m):
        start,end,num=map(int, input().split())
        for j in range(start-1, end):
            array[j]=num
    for i in range(n):
        print(array[i],end=" ")


## 리스트 생성

### 1. 리스트 연산
  ##### list = [0] * N
  ![image](https://github.com/marshmallowing/boj_code/assets/114673063/30a3a3ea-8d96-4ebb-8681-434bb0cdab00)

### 2. range 함수 이용
  #### ranege(start, end, stride) : start부터 end-1까지 stride 만큼씩 증가하는 수열
  
 ![image](https://github.com/marshmallowing/boj_code/assets/114673063/8a916664-cacf-4b7b-b5df-bc78079ca478)

 ![image](https://github.com/marshmallowing/boj_code/assets/114673063/015a9694-bebc-4f42-9059-c3035fe8e25d)

 ---

 ## for 반복문으로 요소 출력

 ### 1. enumerate() 이용
 
     >>> a = [38, 21, 53]
    >>> for index, value in enumerate(a):
    ...     print(index, value)
    ...
    0 38
    1 21
    2 53

for index, value in enumerate(a): enumerate에 리스트를 넣으면 for 반복문에서 인덱스와 요소를 동시에 꺼내 올 수 있음

(+) for 인덱스, 요소 in enumerate(리스트, start=숫자) => 시작점 조작 가능


### 2. 인덱스 이용

    >>> a = [38, 21, 53]
    >>> for i in range(len(a)):
    ...     print(a[i])

    
    ...
    38
    21
    53

---

    for j in array[start-1: end]:
           j=num

j에는 단순히 리스트의 값(숫자) 만이 인덱싱 될 뿐이지 리스트의 값 자체가 수정될 순 없음 
***
