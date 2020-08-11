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

### 같은 접근방법으로 구현한 다른 방법
1. 입력 받은 수열은 num_list, 함수 셋은 p라고 부르겠습니다.

2. 먼저 p 안의 R과 D의 개수를 세야 합니다. R의 개수는 최종적으로 출력할 수열이 정방향인지, 역방향인지 결정합니다. 홀수 일경우 아래 과정을 모두 거치고 수열을 뒤집어서 출력하면 됩니다. D의 개수는 AC가 오류를 내는지 확인하는데 사용됩니다. D의 개수가 num_list의 길이보다 크다면 함수를 실행하다가 반드시 오류를 낼겁니다. 빼내야 하는 수의 개수가 존재하는 수보다 많으니까요. 이 경우에는 함수를 중단하고 error를 출력하면 됩니다.

3. 방향을 가리키는 direction이라는 변수를 만들고 처음엔 앞쪽을 의미하게 합니다. 저는 0으로 초기화했어요. 리스트에서 맨 앞 요소의 index는 0이니까요.

4. 입력 받은 함수 셋 p를 차례로 순회합니다.

5. R을 만났을 때, direction이 0이면 -1로 바꾸고, -1이면 0으로 바꿉니다. 리스트에서 맨 뒤 요소의 index는 -1이니까 삭제할 요소의 위치를 변경한다고 볼 수 있습니다.

6. D를 만나면 num_list[direction] 위치의 요소를 삭제합니다.

7. R의 개수가 홀수면 최종적으로 만들어진 수열을 뒤집어서 반환합니다. 그렇지 않으면 그냥 반환합니다.
https://nerogarret.tistory.com/43
