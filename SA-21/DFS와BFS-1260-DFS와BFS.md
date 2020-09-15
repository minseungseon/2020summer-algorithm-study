# 문제
https://www.acmicpc.net/problem/1260

😙 2606번 바이러스문제에서 삽질하면서 공부하고 푸니까 아주아주 수월했다.

**입력**: 정점개수N 간선개수M 시작정점V  
**입력**: 간선이 연결하는 두 정점  
*두 정점 사이에 여러 개의 간선 존재*  

**출력**: DFS수행  
**출력**: BFS수행  
*V부터 방문된 점을 순서대로 출력*  

<br>

# 나의 답안
### 접근방법: 
- 방문할 수 있는 정점이 여러 개인 경우는 정점 번호가 작은 것을 먼저 방문 -> sort
- DFS: 순환 알고리즘, 재귀
- BFS: queue

### 코드
```
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, S, V;
vector<vector<int>> tree;
bool visited[1001] = { false };
queue<int> q;

void dfs(int cur)
{
	visited[cur] = true;
	cout << cur << " ";
	for (int i = 0; i < tree[cur].size(); i++) {
		if (visited[tree[cur][i]] != 1) {
			dfs(tree[cur][i]);
		}
	}
	return;
}

void bfs(int cur)
{
	q.push(cur);
	visited[q.back()] = 1;
	cout << q.back() << " ";

	while (!q.empty()) {
		int n = q.front();	
		q.pop();
		for (int i = 0; i < tree[n].size(); i++) {
			if (visited[tree[n][i]] != 1) {
				q.push(tree[n][i]);
				visited[q.back()] = 1;
				cout << q.back() << " ";
			}
		}
	}
	return;
}

int main()
{
	cin >> N >> S >> V;
	tree.resize(N+1);
	int a, b;
	while (S--) {
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a); //양방향
	}
	while (N--) { //작은 순서부터 탐색을 위한 정렬
		sort(tree[N].begin(), tree[N].end());
	}
	dfs(V);
	puts("");
	fill_n(visited, 1001, false); //false로 배열 전체 초기화
	bfs(V);
	return 0;
}
```
