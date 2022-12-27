# Linked List

[참고링크](https://visualgo.net/en)

Array List와 함께, List를 만드는 방법 중 하나.

![image-20221227202908813](C:/Users/SSAFY_youji/AppData/Roaming/Typora/typora-user-images/image-20221227202908813.png)

CPU는 생각하고 계산하는 일을 합니다.

STORAGE는 컴퓨터 안의 하드디스크, SSD 등을 얘기합니다. 저장 장치죠. 데이터를 담아둡니다.
STORAGE는 가격이 저렴합니다. 용량이 크고 전원이 꺼져도 데이터가 저장되어 있습니다.

하지만 MEMORY는 STORAGE에 비해 가격이 비싸고 용량이 적고 전원이 꺼지면 데이터가 사라집니다.
그렇지만, MEMORY가 훨씬 더 빨리 데이터를 저장하고 가져옵니다.

CPU는 이 중에서 가장 처리 속도가 빠릅니다. STORAGE안에 있는 데이터를 CPU가 바로 가져와서 쓰게되면 STORAGE가 너무 느리게 대답하는 것으로 느껴집니다. 따라서 MEMORY안에 데이터를 옮겨 놓고 CPU가 처리하게 되는 것이죠. (이전 캐시 개념과 이어짐)

여기서 Data Structure의 미션이 등장합니다.

**데이터 스트럭쳐의 미션은 메모리의 효율적 사용**

-----

![img](Linked%20List.assets/2903.png)

메모리를 건물에 비유하자면,

각각의 사무실에 데이터가 들어가고, 모든 사무실에 접근하는 시간과 비용은 같다.

따라서 찾고자 하는 데이터의 주소를 알고 있다면, 굉장히 빠르게 데이터를 가져올 수 있다는 것이

RAM의 특징이다. 이걸 잘 활용했을 때 우리의 어플은 빠르게 동작한다.

---



## 구조

![img](Linked%20List.assets/2939.png)



## 첫 번째 위치에 추가

![img](Linked%20List.assets/2943.png)

```
Vertex temp = new Vertex(input)
```

![img](Linked%20List.assets/2944.png)

```
temp.next = head
```

![img](Linked%20List.assets/2945.png)

```
head = temp
```



## 중간에 추가

![img](Linked%20List.assets/2919.png)

```
Vertex temp1 = head
```

![img](Linked%20List.assets/2920.png)

```
//현재 k의 값은 2
while (--k!=0)
  temp1 = temp1.next
```

![img](Linked%20List.assets/2921.png)

```
Vertex temp2 = temp1.next
```

![img](Linked%20List.assets/2922.png)

```
Vertex newVertex = new Vertex(input)
```

![img](Linked%20List.assets/2923.png)

```
temp1.next = newVertex
```

![img](Linked%20List.assets/2924.png)

```
newVertex.next = temp2
```

![img](Linked%20List.assets/2926.png)



## 제거

![img](Linked%20List.assets/2932.png)

```
Vertex cur = head
```

![img](Linked%20List.assets/2933.png)

````
//k = 2
while (--k!=0)
  cur = cur.next
````

![img](Linked%20List.assets/2934.png)

```
Vertex tobedeleted = cur.next
```

![img](Linked%20List.assets/2935.png)

```
cur.next = cur.next.next
```

![img](Linked%20List.assets/2936.png)

```
delete tobedeleted
```