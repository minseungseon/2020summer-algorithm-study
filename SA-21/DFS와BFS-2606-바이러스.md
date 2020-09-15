## 문제
https://www.acmicpc.net/problem/2606

### 입력: 컴퓨터의 수 n
### 입력: 연결되어 있는 컴퓨터 쌍의 수
### 입력: 연결되어 있는 컴퓨터의 번호 쌍
### 출력: 1번 감염-> 감염되는 컴퓨터의 수

### 접근방법1: 틀렸습니다.
- virus[]: 1은 감염,0은 비감염
- 쌍의 시작이 1이 아닐 수 있다.
#### BFS와 DFS 설명한 블로그
https://yunyoung1819.tistory.com/86
- DFS로 해봐야겠다.

<br>

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
