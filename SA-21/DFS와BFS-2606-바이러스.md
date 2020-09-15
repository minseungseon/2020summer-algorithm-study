## 문제
https://www.acmicpc.net/problem/2606

**입력**: 컴퓨터의 수 n  
**입력**: 연결되어 있는 컴퓨터 쌍의 수  
**입력**: 연결되어 있는 컴퓨터의 번호 쌍  
**출력**: 1번 감염-> 감염되는 컴퓨터의 수  

#### BFS와 DFS 잘 설명되어있는 블로그
https://yunyoung1819.tistory.com/86

<br>

## 나의 답안
### 접근방법
- DFS

### 코드
```
#include <iostream>
#include <vector>
using namespace std;
int result = 0;
vector<vector<int>> network;
bool visited[101] = { false };
void dfs(int cur)
{
	visited[cur] = true;
	for (int i = 0; i < network[cur].size(); i++) {
		if (visited[network[cur][i]] == false) {
			dfs(network[cur][i]);
			result++;
		}
	}
}
int main()
{
	int comN, netN, a, b;
	cin >> comN >> netN;
	network.resize(comN + 1);
	while (netN--) {
		cin >> a >> b;
		network[a].push_back(b);
		network[b].push_back(a);
	}
	dfs(1);
	cout << result;
	return 0;
}
```

<br>

## 시도1: 틀렸습니다.
### 접근방법
- virus[]: 1은 감염,0은 비감염
- 쌍의 시작이 1이 아닐 수 있다.
- BFS로 해봐야겠다.

### 코드
```
#include <iostream>
#include <queue>
using namespace std;
int virus[101] = { 0 };
pair<int, int> network[101];

void bfs(int netN)
{
	queue<int> q;
	q.push(1);
	while (!q.empty()) {
		int n = q.front();
		q.pop();
		for (int i = 1; i <= netN; i++) {
			if (network[i].first == n && virus[network[i].second] != 1) {
				q.push(network[i].second);
				virus[q.back()] = 1;
			}
		}

	}
}

int main()
{
	int comN, netN, i, result = 0;
	cin >> comN >> netN;
	for (i = 1; i <= netN; i++)
		cin >> network[i].first >> network[i].second;
	bfs(netN);
	for (i = 2; i <= comN; i++) {
		if (virus[i] == 1)
			result++;
	}
	cout << result << endl;
	return 0;
}
```
