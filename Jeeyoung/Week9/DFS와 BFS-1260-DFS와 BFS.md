DFS와 BFS
=======================================================
DFS
-------------------------------------------------------
> 

> 

BFS
-------------------------------------------------------
>


### 문제
https://www.acmicpc.net/problem/1260

### 코드

``` python
#DFS와 BFS-DFS와 BFS

N, M, V = map(int, input().split())

matrix = [[0]*(N+1) for _ in range (N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

def dfs(start, visited):
    visited += [start]
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for i in range(len(matrix[start])):
            if matrix[n][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return visited

print(*dfs(V, []))
print(*bfs(V))
```

### 풀이
1. 


### 추가
