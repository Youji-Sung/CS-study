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


# 클래스 선언
class Queue:

    # 초기 설정, 스택으로 사용할 리스트 선언
    def __init__(self):
        self.queue = []

    # In 함수 / insert 함수 List의 Insert 함수 이용
    def insert(self, data):
        self.queue.insert(0, data)

    # Out 함수 / Remove 함수, List의 pop함수 이용
    def remove(self):
        if len(self.queue) <= 0:
            return ("빈 큐입니다.")
        else:
            return self.queue.pop()




class HangQ:
    size = 0
    rear = -1
    front = -1
    q=[]

    def __init__(self, size):
        self.size = size
        self.q = [None] * size

    def enqueue(self, O:int):
        if self.isFull():
            return

        self.rear+=1
        self.q[self.rear]  = O

    def dequeue(self):
        if self.isEmpty():
            return None
        self.front +=1
        self.q[self.front] = None



    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear == self.size-1)


qq = HangQ(5)
print(qq.q)
qq.enqueue(1)
print(qq.q)
qq.enqueue(2)
print(qq.q)
qq.dequeue()
print(qq.q)
qq.enqueue(1)
print(qq.q)