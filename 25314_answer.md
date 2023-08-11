# 25314_python

#### Data Type

파이썬은 변수 선언 시 자료형을 명시적으로 선언하지 않음 : '동적 타입 언어'
- 수치 자료형 : int(정수), float(실수), complex(복소수)
- 불 자료형 : bool
- 군집 자료형 : str, list, tuple, set, dictionary

(+) 파이썬의 int 자료형 범위 <https://velog.io/@toezilla/1D1Q-001.-Python%EC%9D%98-int-%EC%9E%90%EB%A3%8C%ED%98%95%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%B2%94%EC%9C%84%EA%B0%80-%EB%AC%B4%EC%A0%9C%ED%95%9C%EC%9D%BC%EA%B9%8C>

****

#### import math

- 올림 : math.ceil()
- 내림 : math.floor()
- 소수점 버림 : math.trunc()
- 반올림 : round()

    num = 12345.6789
    print(round(num, 2))
    //결과 : 12345.68
    
###### round(반올림 하려는 수, 반올림하기 원하는 자리 값)


****

#### end=''

    print("h")
    print("i")
    //결과 : h
             i

파이썬은 별도의 강제 개행 없이도 줄바꿈 발생
print("h", end='\n') 기본적으로 이러한 형태

    print("h", end='')
    print("i")

end='' 사용해 줄바꿈 방지