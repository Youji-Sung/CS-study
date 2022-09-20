### [TCP 프로토콜](https://youtu.be/cOK_f9_k_O0?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### TCP가 하는 일

- 전송 제어 프로토콜(Transmission Control Protocol, TCP)은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 `안정적으로`, `순서대로`, `에러 없이` 교환할 수 있게 한다.
- TCP의 안전성을 필요로 하지 않는 애플리케이션의 경우 일반적으로 TCP 대신 비접속형 사용자 데이터그램 프로토콜(User Datagram Protocol)을 사용한다.
- TCP는 UDP보다 안전하지만 느리다.



### TCP 프로토콜의 구조

> 안전한 연결을 지향하는 TCP 프로토콜

![image-20220918170013547](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918170013547.png)



### TCP 플래그

### UAPRSF

- U: Urgent Pointer과 관련 / 긴급 bit
- A: 애크 플래그 == 승인 bit
- P: Push _ 일정 데이터가 쌓이기 전에 밀어넣기
- R: 초기화 비트 (Reset)
- S: (Sync) 상대와 동기화 할때 (==시작할 때)
- F: 연결 끊을 때

![image-20220918170734223](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918170734223.png)



### [TCP 3Way Handshake](https://youtu.be/Ah4-MWISel8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

## TCP를 이용한 통신과정

### 연결 수립 과정

> TCP를 이용한 데이터 통신을 할 때 프로세스와 프로세스를 연결하기 위해 `가장 먼저 수행되는 과정`
>
> 1. 클라이언트가 서버에게 요청 패킷을 보내고
> 2. 서버가 클라이언트의 요청을 받아들이는 패킷을 보내고
> 3. 클라이언트는 이를 최종적으로 수락하는 패킷을 보낸다
>
> `위의 3개의 과정을 3Way Handshake라고 부른다.`

![image-20220918171609461](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918171609461.png)





### [TCP를 이용한 데이터 전송 과정](https://youtu.be/0vBR666GZ5o?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

## TCP를 이용한 통신과정

### 데이터 송수신 과정

> TCP를 이용한 데이터 통신을 할 때 단순히 TCP 패킷만을 캡슐화해서 통신화하는 것이 아닌 페이로드를 포함한 패킷을 주고 받을 때의 일정한 규칙
>
> 1. 보낸 쪽에서 또 보낼 때는 SEQ 번호와 ACK 번호가 그대로다
> 2. 받는 쪽에서 SEQ 번호는 받은 ACK 번호가 된다
> 3. 받는 쪽에서 ACK 번호는 받은 SEQ 번호 + 데이터의 크기



#### HTTP나 FTP와 같은 각종 데이터를 포함한 통신

![image-20220919200701376](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220919200701376.png)





### [TCP의 연결 상태 변화](https://youtu.be/yY0uQf0BTH8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

## TCP 상태전이도

### TCP 연결 상태의 변화

![image-20220919200956449](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220919200956449.png)

실선 - client

- LISTEN: 포트 번호를 열어놓고 있는 상태(서버쪽에서 사용하는 상태)
- ESTABLISHED: 연결이 수립됨



### 3Way-Handshake와 함께보기

> 연결을 수립하는 3Way-Handshake 과정에서의 상태 변화

![image-20220919201342566](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220919201342566.png)





### [TCP 프로토콜 분석 실습](https://youtu.be/WseqBDo-j3Y?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

-