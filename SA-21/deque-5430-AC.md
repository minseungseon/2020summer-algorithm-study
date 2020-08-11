## 문제
https://www.acmicpc.net/problem/5430

**첫 번째 입력** : 테스트 케이스 개수 t  
**두 번째 입력** : 수행할 함수 p  
**세 번째 입력** : 배열 크기 n  
**나머지 입력, n번** : 배열에 들어있는 수  

**출력** : 각 테스트 케이스에 대한 함수 수행 결과 or error

## 접근 방법
stack : LIFO (Last In First Out) 구조  
queue : FIFO(First-In-First-Out) 구조  
deque : Deque(Double Ended Queue), front와 end에서 모두 삽입, 삭제가 가능

R(뒤집기) : front와 end 중 point되어있는 위치가 바뀐다.  
D(버리기) : 현재 point 되어있는 위치에서 버린다.

역시 STL duque가 존재!!

입력, 출력 형식(ex. [1,2,3,4]) 때문에 string을 정수로 변환하는 과정 필요

## 나의 답안
```c++

```

## 시도 1 = 논리오류
```c++
#include <iostream>
#include <deque>
#include <string>
using namespace std;

void print(deque<int> d, int error)
{
	if (error == 1) {
		cout << "error" << endl;
		return;
	}
	cout << "[";
	for (int i = 0; i < d.size(); i++)
	{
		cout << d.front();
		d.pop_front();
		if (i != d.size() - 1)
			cout << ",";
	}
	cout << "]";
}

int main()
{
	int t, n, front = 1, error = 0;	//1 -> front, 0->rear
	string p, arr;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> p;
		cin >> n;
		deque<int> d(n);
		for (int j = 0; j < n; j++)
			cin >> d[j];	//배열 입력 완료
		
		for (int k = 0; k < p.size(); k++) {
			if (p[k] == 'R') {
				if (front == 0)
					front == 1;
				else
					front == 0;
			}

			else if (p[k] == 'D') {
				if (d.empty()) {
					error = 1;
					break;
				}
				else {
					if (front == 0)
						d.pop_back();
					else
						d.pop_front();
				}
			}
		}
		print(d, error);
	}
	return 0;
}
```

### 시도 1에 따른 해결방안 모색
string 정수변환에서 문제가 있다.
