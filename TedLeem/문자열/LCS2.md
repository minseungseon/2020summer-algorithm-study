# 문제
https://www.acmicpc.net/problem/9252

# 접근방법
LCS문제 dp했던 것처럼 개수 구하고 문자열도 마찬가지로 dp구하는 것처럼 합쳐가주면 된다.    

## 코드1 통과
```python
str1 = input()
str2 = input()

N= len(str1)
M= len(str2)

dp = [[0 for i in range(M+1)]for j in range(N+1)]
dpStr = [[0 for i in range(M+1)]for j in range(N+1)]
for i in range(0,M+1):
    dp[0][i] =0
    dpStr[0][i] =""
for i in range(1,N+1):
    dp[i][0] = 0
    dpStr[i][0] =""
for i in range(1,N+1) :
    for j in range(1,M+1):
        if str1[i-1] == str2[j-1] :
            dpStr[i][j] = dpStr[i-1][j-1] + str1[i-1]
            dp[i][j] = dp[i-1][j-1] +1
        else:
            if len(dpStr[i][j-1]) >= len(dpStr[i-1][j]):
                dpStr[i][j] = dpStr[i][j-1]
            else:
                dpStr[i][j] = dpStr[i-1][j]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[N][M])
print(dpStr[N][M])
```
