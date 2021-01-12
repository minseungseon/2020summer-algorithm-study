## 문제
https://www.acmicpc.net/problem/1013

**목표**: (100+1+|01)+ 정규식 match  
**출력** : 'YES' or 'NO'  

<br>

## 나의 답안1: 내장함수 없이

# 시간초과
```python
def isVega(case):
    if len(case) < 2:
        return False

    idx = 0
    while idx < len(case): # 모두 거친 후 같다면 True 
        #(1)
        if case[idx] == '1':
            #(100+1)
            if case[idx:idx+3] == '100':
                idx += 3
                while idx < len(case) and case[idx] == '0':
                    idx += 1
                if idx < len(case) and case[idx] == '1':
                    idx += 1
                else:
                    return False
            #(1001)(1+)
            elif idx > 3 and case[idx-4:idx] == '1001':
                while idx < len(case) and case[idx] == '1':
                    idx += 1   
                if idx < len(case) and case[idx] == '0':
                    idx -= 1
            else:
                return False
        #(01)
        elif case[idx:idx+2] == '01':
            idx += 2
            while case[idx:idx+2] == '01':
                idx += 2
        else:
            return False  
    return True
```

<br>

## 답안 접근 방법
2 번 선택
1. match 된 문자열 pop
2. idx 이동 (윈도우슬라이드가 이런건가요??)

<br>

## 시도1: 틀렸습니다
```python
def isVega(case):
    if len(case) < 2:
        return False

    idx = 0
    while idx < len(case): # 모두 거친 후 같다면 True 
        #(100+1+)
        if case[idx:idx+3] == '100':
            idx += 3
            while idx < len(case) and case[idx] == '0':
                idx += 1
                #(1+)
            if idx < len(case) and case[idx] == '1':
                idx += 1
            else:
                return False
        
        #(01)
        elif case[idx:idx+2] == '01':
            idx += 2
            while case[idx:idx+2] == '01':
                idx += 2
        else:
            return False  
    return True
```

#### 내 코드 문제분석(반례찾기)
100
01
1001
01
YES
YES
YES
YES

<br>

## 시도2: 틀렸습니다

```python
def isVega(case):
    if len(case) < 2:
        return False

    idx = 0
    while idx < len(case): # 모두 거친 후 같다면 True 
        #(1)
        if case[idx] == '1':
            #(100+1)
            if case[idx:idx+3] == '100':
                idx += 3
                while idx < len(case) and case[idx] == '0':
                    idx += 1
                if idx < len(case) and case[idx] == '1':
                    idx += 1
                else:
                    return False
            #(1001)(1+)
            elif idx > 3 and case[idx-4:idx] == '1001':
                while idx < len(case) and case[idx] == '1':
                    idx += 1
            else:
                return False
        #(01)
        elif case[idx:idx+2] == '01':
            idx += 2
            while case[idx:idx+2] == '01':
                idx += 2
        else:
            return False  
    return True
```

#### 내 코드 문제분석(반례찾기)
10011001

10011 001 이아니라
1001 1001 로 봐야함

#### 해결
1001 매치 이후 1이 나왔을 때 case분리
1. 1+ 뒤에 0이 두번 이상나온 후 1이 나오는 1001 패턴인가
2. 아닌가

<br/><br/>

## 나의 답안2: fullmatch()와 정규식
```python
def isVega(case):
    if len(case) < 2:
        return False

    p = re.compile('(100+1+|01)+')
    result = p.fullmatch(case)
    return True if result else False
```

<br/><br/>

### 시도1 : 런타임에러
```python
def isVega(case):
    p = re.compile('(100+1+|01)+')

    result = p.match(case)
    return False if result.end() != len(case) else True
```

#### 런타임에러 발생이유
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때

#### 내 코드 문제 분석: 
- '' 값이 들어왔을 때 .end() 참조
- 길이가 2보다 작으면 거르기 + fullmatch() 
