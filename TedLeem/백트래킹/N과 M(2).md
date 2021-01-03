# 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
# 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 접근방법: 재귀
숫자들을 트리형태로 표현한다음에 알고리즘을 생각하면 조금 쉽게 재귀를 생각해낼수있다.
첫 번쨰 level에 1,2,3,4    
두 번쨰 level에 각 부모노드에 대해 트리가 1,2,3,4 형태가 쭉 있다고 생각을 하는거다.    
ex:
```
|1|                   |2|                   |3|       |4| 
|1|2|3|4|             |1|2|3|4|             |1|2|3|4| |1|2|3|4|
|1234|1234|1234|1234| |1234|1234|1234|1234| ...........
```
순서가 있는 것이므로,
다음 level(여기서는 자식 level)로로 넘어거가는 경우, 혹은 같은 level에서 옆 노드로 넘어가는 경우를 생각하면 된다.   

```java
import java.util.Scanner;

public class NandM {
    static int N,M;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N=sc.nextInt();
        M= sc.nextInt();
        int []brr = new int[M];
        recur(brr,0,0,1);
    }
    static void recur(int []brr, int length, int index, int value){

//        if(value + M > N) return;

        if ( length == M) {
            printArr(brr);
            return;
        }

        else{
            brr[index] = value;
            recur(brr,length+1,index+1,value+1);
//          트리의 다음 단계로 이동
            if(++value<=N) recur(brr,length,index,value);
            //트리의 같은 단계에서 옆 노드로 이동
        }
    }
    static void printArr(int []brr) {
        for(int i=0;i<brr.length;i++) {
            System.out.print(brr[i]);
        }
        System.out.println("\n");
    }

}

```

위의 코드인 경우 index=0 ,value=3일 경우 다음 코드를 통과한후에    
```java 
if(++value<=N) recur(brr,length,index,value);
```
다음 코드를 통과하게 되고 종료조건 length=M을 맞닥뜨려 출력하게 된다.    
```java
recur(brr,length+1,index+1,value+1);
```
