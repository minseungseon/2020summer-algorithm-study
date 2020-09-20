#N과 M(4)
## 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
## 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

##접근방법
N과 M(1)을 풀줄 알면 풀 수 있는 문제이다. 사실 N과 M(1)이 더 생각해내기 어려운 문제인 것 같다.(내기준) 근데 풀다가 느낀건데 이런 백트래킹 문제 뭔가 트리형태로 푸는게 더 쉬운 것 같다.. 
## 코드1
```c++
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 8 + 1;


int N, M;
int arr[MAX];

void f(int cnt) {
	
	if (cnt == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i] <<" ";
		}
		cout << "\n";
		return;
	}

	for (int i = 1; i <= N; i++) {
				
		if (cnt > 0) {
			if (i >= arr[cnt - 1]) {
				arr[cnt] = i;
			}
			else continue;
			
		}
		else if (cnt == 0) {
			arr[cnt] = i;
		}
		f(cnt + 1);

	}
}

int main() {


	cin >> N >> M;
	f(0);
	return 0;

}

```

## 코드 2 (좀 더 조건을 간결하게 쓴 코드)
```c++
for (int i = (cnt ==0) ? 1 : arr[cnt-1] ; i<=N;i++) {
 arr[cnt]=i;
 f(cnt+1);
} 
```
