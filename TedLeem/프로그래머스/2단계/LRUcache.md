# 문제
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

# 입력 형식
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
# 출력 형식
입력된 도시이름 배열을 순서대로 처리할 때, “총 실행시간”을 출력한다.
# 조건
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다.
# 입출력 예제
캐시크기(cacheSize)	도시이름(cities)	실행시간
3	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	50
3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]	21
2	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	60
5	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	52
2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]	16
0	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	25
hit = 1time, miss = 5time 실행시간이 걸린다.
# 접근방법
내가 고민했던 부분은 캐시의 자료구조를 연결리스트를 이용한 큐를 이용할 것인가 아니면 단순히 배열을 이용한 리스트를 이용할 것인가 였다.    
전자는 삽입 삭제의 시간복잡도가 O(1), 검색 시간복잡도가 O(n)이고    
후자는 O(n), O(1)이다.   
처음에는 그냥 연결리스트를 사용하는 것이 맞을 것 같다 생각했는데 캐시 사이즈가 무진장하게 커질 수록 캐시내 hit비율이 높아질 것이고 
그때는 검색시간이 더 중요할 거라 생각해 배열을 사용하는 것도 좋다 생각했다. 이런거 어떻게 결정해야 할지 모르겠다..    
일단 큐로 구현한다고 가정을 하고 생각한 알고리즘은 다음과 같다.   
``` python3
 # 입력받은 문자열 cities를 파싱하기
        # 크기가 cacheSize인 큐 생성 , 반환값인 time 선언
        # 입력받은 문자열이 없을 떄까지            
            # 입력받은 문자열들을 순서대로 확인한다. ( 큐에 해당 문자열이 있는지 검색)
            
              # 큐에 해당 문자열이 있는 경우(hit)
                  # time = time +1
                  # 해당 문자열을 큐에서 찾은후 삭제한다
                  # 다시 해당 문자열을 큐에 인큐(삽입)
              # 큐에 해당 문자열이 없는 경우(miss)
                  # time = time +5
                  # 디큐(큐의 맨 앞에 원소 삭제)
                  # 해당 문자열을 인큐(삽입)
            # time 반환

```
문제 풀때 파이썬을 선택했는데 문법을 몰라서 일단 그땐 이런식으로 작성했었다.. 함수 매개변수가 자료형이 없으니 어떻게 처리해야할지도 몰라서 난감했다. 

# LRU 알고리즘
보통 LRU 알고림즈의 구현은 LinkedList의 큐를 이용한다. 이때 검색효율을 증가하기 위해 그 해쉬함수(?)를 이용한 맵 기능을 추가한다.    
큐가 (key, value)의 형태로 있고 입력값이 x일때 다음식을 만족하는 "f(x) = key" 함수가 해쉬함수이다. 이때 해쉬함수를 결정해주는게 중요한데..    
이번문제의 입력값은 문자열이고 문자열의 맨 앞에 문자를 숫자로 변환하여 key값을 찾는 함수를 해쉬함수로 하면 좋을 것 같다 생각했다.. (a=0,b=1, apple => 0 이런식으로..    )    
문제는 apple absolute의 단어가 캐쉬에 존재하면 어쩔 수 없이 key가 0인 것들중에서 검색을 해야헤서 __"모든 키는 중복된다"__ 해쉬테이블의 법칙을 위반한다..   
그래서 문자열 해쉬함수만드는 방법들을 소개하는 링크를 걸어보겠다.     
https://twpower.github.io/116-hash-table-string-key-hash-function    
https://stackoverflow.com/questions/8317508/hash-function-for-a-string    
해쉬 정말 중요한 것같다.. 나중에 공부해봐야겠따.    
``` python3 
from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
```
참고 https://www.geeksforgeeks.org/lru-cache-implementation/
