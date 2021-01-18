## 문제
https://programmers.co.kr/learn/courses/30/lessons/42888

### 문제 정보

**목표**: result에서 보여지는 닉네임은 해당 유저의 최종 닉네임

<br>

## 나의 답안1: 

```python
def solution(record):
    answer = []

    id_record = []
    user = {}

    for r in record:
        s = r.split()
        if s[0].startswith('L'):
            id_record.append(s[1]+'님이 나갔습니다.') #id로 구성
        else:
            user[s[1]] = s[2] #중복되어도 덮어씌워짐
            if s[0].startswith('E'):
                id_record.append(s[1]+'님이 들어왔습니다.')

    for i in id_record:
        user_id = i[0:i.find('님')]
        answer.append(user[user_id]+i[i.find('님'):])

    return answer
```

## 접근 방법:
1. id로 result문장 생성  
딕셔너리를 이용하고 key, value는 아래와 같이!  
{'id':'nickname'}
2. id를 최종 nickname으로 변경

<br>
<br>
