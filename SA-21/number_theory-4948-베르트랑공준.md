## 문제
https://www.acmicpc.net/problem/4948

#### 베르트랑 공준
임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다.  
n < 적어도 소수 하나 <= 2n

**입력**: 자연수 n이 여러줄 + 0(마지막 입력)
**출력**: 베르트랑 공준 소수 개수

<br>

## 나의 답안
### 접근방법
소수 목록을 만들어서 비교 (더 효율적..?)  
- for문 돌려서 만들어놓기-> 시간초과  
- 기억안나는 기발한 방법 구글링하기-> 에라토스테네스의 체: https://wikidocs.net/21638  

와..이거 고딩때 수학책에 그림있었는데..!!!   
__'소수로 나누어 나눠지면 탈락'__ 이라는 아이디어를 소수의 배수는 지운다. 로 바꾸어 생각하면 동일하네요!!  
```
범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
1. 1은 제거 
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다. 
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다. 
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다. 
5. (반복)
```
시간복잡도: O(nloglogn)

### 코드
```
#에라토스테네스의 체
def get_prime_number(limit):
    is_prime = [True] * (limit) 
    for i in range(2, int((limit + 1)/2)): #배수 범위 넘지 않게 몫을 나눈다.
        if is_prime[i] == True: #i가 소수라면
            for j in range(2*i, limit, i): #i의 배수는 걸러낸다.
                is_prime[j] = False
    return [i for i in range(2, limit) if is_prime[i] == True]

answer=[]

limit = 2*123456
primes = get_prime_number(limit)

while True:
    n = int(input())
    if n == 0: 
        break  

    a = list(range(n+1, 2*n+1))
    count = list(set(a).intersection(primes))
    answer.append(len(count))

for e in answer:
    print(e)
```

## 코드 개선
### 접근방법
답안 코드를 보면 out of range오류를 해결하기 위해 2로 나누었다.  
나: 2로 나누면 어차피 배수니까 괜찮겠네

3. 예전에 소수문제 풀때 생각못해낼 기발한 방법있었는데... 뭐였는지 추측이 안된다..
이 3번 방법을 찾아보니 연관된 해결방법이었다.

```
N = a * b 라고 가정하자.
a 와b 모두 제곱근N보다 작거나 같다.

그러므로, a와 b의 곱인 N이 소수인지 알고 싶으면 N의 제곱근까지만 검사하면 된다!
```
위 설명보다 아래 설명이 더 빠르게 와닿았다.

```
10의 약수 : 1, 2, 5 , 10
1, 10을 제외하면
2*5, 5*2 로 10을 구성한다.

동일한 약수를 순서만 바꾸어 곱해 구한다고 볼 수 있다.
그러므로, 제곱근만 소수인지 확인하면 된다!

```


### 코드
```
def get_prime_number(limit):
    is_prime = [True] * (limit) 
    for i in range(2, int(limit ** 0.5) + 1): #개선한 코드 부분
        if is_prime[i] == True: #i가 소수라면
            for j in range(2*i, limit, i): #i의 배수는 걸러낸다.
                is_prime[j] = False
    return [i for i in range(2, limit) if is_prime[i] == True]
```

<br>

## 시도1: 시간초과
### 접근방법
소수 개수 찾기  
소수: 1과 자신만을 약수로 갖는 수  

1. 2부터 나누어 나눠지면 탈락  
2. 소수로 나누어 나눠지면 탈락  
소수가 아닌 수 = 자기 자신보다 작은 수(이 수들 중 소수가 존재)로 나누어지는 수  
But, 소수로 나누려면 소수가 필요  

n부터 소수인지 검사,  
- for문 엄청 돌리며 검사 (무조건 시간초과겠죠?)  
알면서 해보겠습니다.  

시.간.초.과~

### 코드
```
def solution(n): 
    count = 0

    for i in range(n+1, 2*n+1):
        if is_prime_number(i):
            count += 1
    return count

def is_prime_number(i):
    for divisor in range(2, i):
        if i % divisor == 0:
            return False 
    return True

```
