# STACK

- 입력과 출력이 한 곳(방향)으로 제한

- LIFO (Last In First Out, 후입선출) : 가장 나중에 들어온 것이 가장 먼저 나옴

  

![image-20221226204038783](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226204038783.png)



*** 변수**

1. 스택 포인터(ptr)

 : 현재 스택에 데이터가 어디까지 쌓여있는지 나타내는 포인터. 

2. 크기(capacity)

 : 스택의 크기를 나타내는 변수. 스택 생성 시 지정해준다.

 

*** 함수**

1. __init__() : 변수 초기화

2. push() : 스택에 데이터를 한개 삽입한다.

3. pop() : 스택에서 데이터를 한개 꺼낸다.

4. __len__() : 현재 쌓여있는 데이터의 크기를 반환한다.

5. is_empty() : 스택의 empty 여부를 확인한다.

6. is_full() : 스택이 가득 찼는지 확인한다.

7. peek() : 가장 최근에 쌓인 데이터를 읽는다.



- push와 pop을 할 때, 해당 인덱스 위치를 알아야 하므로 '스택 포인터 SP'가 팔요함

- 1. 스택 포인터는 항상 빈 공간을 가리키고 있다.

  2. 포인터의 위치만을 수정하여 스택초기화, 데이터 제거가 가능하다.





## 구현

```python
from typing import Any

class Stack:



    class Empty(Exception):
        pass

    class Full(Exception):
        pass
    

    def __init__(self, c:int) -> None:
        ## 변수 초기화 함수.
        ## stack의 크기를 생성 시 전달받는다.
        self.ptr = 0
        self.capacity = c
        self.stk = [None] * c

    def __len__(self) -> int:
        ## Stack의 길이를 반환하는 함수
        ## ptr은 다음 빈 공간을 가리키고 있기 때문에 길이와 같다.
        return self.ptr

    def is_empty(self) -> bool:
        ## Stack이 비었는지 확인하는 함수
        return self.ptr <= 0

    def is_full(self) -> bool:
        ## Stack이 가득 찼는지 확인하는 함수
        return self.ptr >= self.capacity

    def push(self, data: int) -> None:
        if self.is_full():
            raise Stack.Full
        self.stk[self.ptr] = data
        self.ptr += 1

    def pop(self) -> any:
        ## Stack의 가장 바깥에 쌓여있는 데이터를 Stack에서 빼는 함수.
        ## 비었는지 확인하고 data를 return한다. 이 때 ptr만 하나 줄여주면 된다.
        if self.is_empty():
            raise Stack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        ## 가장 바깥에 쌓여있는 데이터를 읽어오는 함수
        ## 비어있는지 확인 후 data를 return한다.
        if self.is_empty():
            raise Stack.Empty
        return self.stk[self.ptr-1]
```





# Queue

- 입력과 출력을 한 쪽 끝(front, rear)로 제한
- FIFO (First In First Out, 선입선출) : 가장 먼저 들어온 것이 가장 먼저 나

- 큐의 가장 첫번째 원소를 front, 마지막 원소를 rear라 함

- 큐는 들어올 때 rear로 들어오고, 나갈 때는 front부터 나감

  

![image-20221226210835970](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226210835970.png)



*** 함수**

1. __init__() : 변수 초기화

2. enqueue() : 큐에 데이터를 한개 삽입한다.

3. dequeue() : 큐에서 데이터를 한개 꺼낸다.





## 구현



```python

 
#클래스 선언
class Queue:
 
    # 초기 설정, 스택으로 사용할 리스트 선언
    def __init__(self):
        self.queue = []
 
    # In 함수 / insert 함수 List의 Insert 함수 이용
    def enqueue(self, data):
        self.queue.insert(0, data)
 
    # Out 함수 / Remove 함수, List의 pop함수 이용
    def dequeue(self):
        if len(self.queue) <=0 :
            return("빈 큐입니다.")
        else :
            return self.queue.pop()
 
        
```

```python
#클래스 선언
class Queue:
    #초기화 디폴트 길이 5
    def __init__(self, size = 5):
        self.queue = []
        self.size = size
        self.front = 0
        self.reaer = 0
    
    #큐 삽입
    def enqueue(self,data):
        if self.size <= self.rear:
            print("큐가 가득 찼습니다.")
        else:
            self.queue.append(data)
            self.rear +=1 #추가했을 때, rear 크기 증가
            
    #큐 추출
    def dequeue(self):
        if self.size<=0 or self.rear == self.front:
            print("dequeue를 실행할 값이 없습니다.")
        else:
            print(self.queue[0])
        	del self.queue[0]
            self.front +=1 #추출했을 때 front 값 증가
        
            
        
```





# Stack - 설명

- 스택(stack)이란 **쌓아 올린다는 것**을 의미한다. 

- 따라서 스택 자료구조라는 것은 책을 쌓는 것처럼 **차곡차곡 쌓아 올린 형태의 자료구조**를 말한다.



![image-20221226204038783](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226204038783.png)

- ptr : 스택 포인터

- 📌 **스택의 특징**

  스택은 위의 사진처럼 **같은 구조와 크기의 자료**를 **정해진 방향으로만** 쌓을수 있고,

  **ptr으로 정한 곳을 통해서만 접근**할 수 있다.

  ptr에는 가장 위에 있는 자료는 가장 최근에 들어온 자료를 가리키고 있으며,

  삽입되는 새 자료는 ptr이 가리키는 자료의 위에 쌓이게 된다.

  스택에서 자료를 삭제할 때도 ptr을 통해서만 가능하다.

  스택에서 ptr을 통해 **삽입하는 연산**을 'push' , ptr을 통한 **삭제하는 연산**을 'pop'이라고 한다.



- 따라서 스택은 시간 순서에 따라 자료가 쌓여서 **가장 최근에 삽입된 자료가 가장 먼저 삭제된다**는

  구조적 특징을 가지게 된다.

   

  이러한 스택의 구조를 **후입선출(LIFO, Last-In-First-Out) 구조**이라고 한다.

   

  그리고 비어있는 스택에서 원소를 추출하려고 할 때 stack underflow라고 하며,

  스택이 넘치는 경우 stack overflow라고 한다.





- 📌 **스택의 활용 예시**

  스택의 특징인 후입선출(LIFO)을 활용하여 여러 분야에서 활용 가능하다.

  - 웹 브라우저 방문기록 (뒤로 가기) : 가장 나중에 열린 페이지부터 다시 보여준다.
  - 역순 문자열 만들기 : 가장 나중에 입력된 문자부터 출력한다.
  - 실행 취소 (undo) : 가장 나중에 실행된 것부터 실행을 취소한다.
  - DFS 깊이 우선 탐
  - 후위 표기법 계산
  - 수식의 괄호 검사 (연산자 우선순위 표현을 위한 괄호 검사)





# Queue - 설명

- Queue 의 사전적 의미는 1. (무엇을 기다리는 사람, 자동차 등의) **줄** , 혹은 **줄을 서서 기다리는 것**을 의미한다.

- 따라서 일상생활에서 놀이동산에서 줄을 서서 기다리는 것, 은행에서 먼저 온 사람의 업무를 창구에서 처리하는 것과 같이

- **선입선출(FIFO, First in first out) 방식**의 자료구조를 말한다. 

 

![image-20221226210835970](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226210835970.png)





- 📌 **큐의 특징**

  정해진 한 곳(top)을 통해서 삽입, 삭제가 이루어지는 스택과는 달리

  큐는 한쪽 끝에서 삽입 작업이, 다른 쪽 끝에서 삭제 작업이 양쪽으로 이루어진다.

  이때 **삭제연산만 수행되는 곳을 프론트(front)**, **삽입연산만 이루어지는 곳을 리어(rear)**로 정하여

  각각의 연산작업만 수행된다. 이때, 큐의 리어에서 이루어지는 삽입연산을 **인큐(enQueue)**

  프론트에서 이루어지는 삭제연산을 **디큐****(dnQueue)**라고 부른다.

   

  - 큐의 가장 첫 원소를 front / 가장 끝 원소를 rear
  - 큐는 들어올 때 rear로 들어오지만 나올때는 front부터 빠지는 특성
  - 접근방법은 가장 첫 원소와 끝 원소로만 가능
  - 가장 먼저 들어온 프론트 원소가 가장 먼저 삭제

  즉, 큐에서 프론트 원소는 가장 먼저 큐에 들어왔던 첫 번째 원소가 되는 것이며,

  리어 원소는 가장 늦게 큐에 들어온 마지막 원소가 되는 것이다.





- 📌 **큐의 활용 예시**

   

  큐는 주로 데이터가 입력된 시간 순서대로 처리해야 할 필요가 있는 상황에 이용한다.

  - 우선순위가 같은 작업 예약 (프린터의 인쇄 대기열)
  - 은행 업무
  - 콜센터 고객 대기시간
  - 프로세스 관리
  - 너비 우선 탐색(BFS, Breadth-First Search) 구현
  - 캐시(Cache) 구현
