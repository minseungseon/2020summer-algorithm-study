## 문제
https://www.acmicpc.net/problem/2947

**입력**:  
첫째 줄에 조각에 쓰여 있는 수가 순서대로 주어진다.  숫자는 1보다 크거나 같고, 5보다 작거나 같으며, 중복되지 않는다.  
처음 순서는 1, 2, 3, 4, 5가 아니다.  
**출력**: 두 조각의 순서가 바뀔때 마다 조각의 순서

<br>

## 나의 답안
### 접근방법
버블정렬  
시간복잡도: O(n^2)  
### 코드
```
def sort(wood):
    for i in range(len(wood)):
        for j in range(len(wood)-1):
            if wood[j] > wood[j+1]:
                wood[j], wood[j+1] = wood[j+1], wood[j]
                print(* wood)
```

<br>

## 시도1: zip함수
### 접근방법
파이썬 내장함수로 믓지게 짜보고 싶다..  
-> zip()으로 원소 둘씩 묶어서 해보자

for문을 돌면서 wood의 원소위치가 함께 변경되어야 한다...
### 코드
```
def sort(wood):
    for a, b in zip(wood, wood[1:]):
        if a > b:
            wood.index(b)= a
            wood.index(a)= b
```
