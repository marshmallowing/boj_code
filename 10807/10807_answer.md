# 10807_python

### li=list(map(int, input().split()))
map : 리스트의 요소를 지정된 함수로 처리해주는 함수
    
    x=input().split()
    print(x)
    #입력: 1 2 3
    #결과: ['1', '2', '3']


    a = [1.2, 2.4, 3.6, 4.5]
    a = list(map(int, a))
    #a=> [1, 2, 3, 4]

---

### count()
count() : python 리스트 내장 메소드 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환

    cnt=0
    for i in li:
      if(i==v) : cnt+=1
    print(cnt)

count() 사용 시 이렇게 축약 가능

    print(li.count(v))
