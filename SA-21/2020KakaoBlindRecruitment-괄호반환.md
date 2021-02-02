## 문제

https://programmers.co.kr/learn/courses/30/lessons/60058

### 문제 정보

p는 균형잡힌 괄호 문자열

<br>

## 나의 답안1:

```python

def solution(p):
    answer = ""

    if not p or is_correct(p):
        return p

    u, v = divide(p)

    if is_correct(u):
        return u + solution(v)
    else:
        s = "(" + solution(v) + ")"
        u_list = list(u[1:-1])
        for i in range(len(u_list)):
            if u_list[i] == "(":
                u_list[i] = ")"
            elif u_list[i] == ")":
                u_list[i] = "("
        u = "".join(u_list)
        return s + u


def divide(w):
    valance = 0
    u = ""
    v = ""
    for i in range(len(w)):
        if w[i] == "(":
            valance += 1
        if w[i] == ")":
            valance -= 1

        if valance == 0:
            u = w[: i + 1]
            v = w[i + 1 :]
            break
    return u, v


def is_correct(s):
    lc = 0
    rc = 0
    for i in s:
        if i == "(":
            lc += 1
        else:
            rc += 1
            if lc < rc:
                return False
    if lc != rc:
        return False
    return True
```

## 접근 방법:
**divide()**  
u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 한다.  
=왼쪽부터 오른쪽까지 괄호를 세는 경우 마지막 괄호를 세면 갯수가 동일해진다.

<br>
<br>

## 시도1

```python
    lc = 0
    rc = 0
    for i in s:
        if i == "(":
            lc += 1
        else: # 수정해야하는 block
            if lc == 0:
                return False
            else:
                rc += 1
                if lc != rc:
                    return False
    if lc != rc:
        return False
    return True
```

#### 문제 해결

- (의 수가 0이 아님
- )의 수가 더 적어야함
- (, ) 의 수가 동일
