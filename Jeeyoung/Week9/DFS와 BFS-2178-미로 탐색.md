미로 탐색
=======================================================
DFS
-------------------------------------------------------
> 

> 

BFS
-------------------------------------------------------
>


### 문제
https://www.acmicpc.net/problem/2178

### 코드

``` python
#DFS와 BFS-미로 탐색

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, str(input()))))

visited = [[0]*M for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

queue = [[0,0]]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if maze[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx, ny])

print(visited[N-1][M-1])
```
