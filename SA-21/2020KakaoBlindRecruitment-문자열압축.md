## 문제

https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

<br>

## 나의 답안1:

```python
def solution(s):
    answer = len(s)
    result = ""

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):  # 반으로 나눠질 때 까지만
        substr = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if s[j : j + i] == substr:  # 반복
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + substr  # 숫자 + 문자열
                substr = s[j : j + i]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + substr
        if len(result) < answer:
            answer = len(result)
        result = ""
    return answer

```

## 접근 방법:

i : 문자열 묶음 단위  
```for j in range(i, len(s), i):```

- 처음 부분문자열부터 시작, count = 1
- 묶음 단위만큼 건너뛰며 반복

j : 포인터

- 묶음단위보다 마지막 남은 부분문자열이 짧은 경우도 처리
