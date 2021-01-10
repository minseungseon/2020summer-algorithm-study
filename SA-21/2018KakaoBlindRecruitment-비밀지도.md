## 문제
https://programmers.co.kr/learn/courses/30/lessons/17681
<br>

# 최종 답안
### 접근방법
- bin() 내장함수 사용
- python 2진수 표현 '0b....' -> 2개 슬라이싱
- 부족한 0 concatenation
- replace()로 0->' '/ 1->'#'

### 코드
```
def solution(n, arr1, arr2):
    overlap = map(lambda x, y : bin(x | y)[2:], arr1, arr2)
    answer = [("0" *(n - len(e)) + e).replace("0", " ").replace("1", "#") for e in overlap]
    return answer
```

<br>
<br>
<br>
<br>

# bin(), | 구현하기
### 접근방법
집념의 삽질...ㅎ


1. 십진수를 바로 논리합 연산할 수 없다고 생각했다.  
  -> bin() 구현  

2. 구현한 bin() 반환형은 string  
  -> 논리합 연산 불가  
    -> union() 구현  
    
    
파이썬 내장함수 공부,, 빡시게 했네요

### 코드
```
def dec_to_bin(arr):
    result=[]
    for dec in arr:
        binary = ''
        while dec > 0: 
            dec, mod = divmod(dec, 2)
            binary += str(mod)
        binary += '0'*(len(arr)-len(binary))
        result.append(binary[::-1])
    return result

def union(x, y):
    result = ''

    for i in range(len(x)):
        if x[i]=='1' or y[i]=='1':
            result += '1'
        else:
            result += '0'
    return result

def solution(n, arr1, arr2):
    answer = []
    arr1, arr2 = dec_to_bin(arr1), dec_to_bin(arr2)
    overlap = list(map(union, arr1, arr2))
    
    for e in overlap:
        answer.append(e.replace("0", " ").replace("1", "#"))
    return answer
```
