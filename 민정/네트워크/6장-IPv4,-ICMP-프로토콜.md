### [IPv4 프로토콜](https://youtu.be/_i8O_o2ozlE?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### IPv4가 하는 일

> 네트워크 상에서 데이터를 교환하기 위한 프로토콜
>
> 데이터가 **정확하게 전달될 것을 보장하지 않는다**
>
> 중복된 패킷을 전달하거나 패킷의 순서를 잘못 전달할 가능성도 있다
>
> --> 악의적으로 이용되면 DoS 공격이 됨
>
> 데이터의 정확하고 순차적인 전달은 그보다 상위 프로토콜인 TCP에서 보장한다

### IPv4 프로토콜의 구조

![image-20220911131405172](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911131405172.png)

### IHL (Header Length)

- 헤더의 길이는 20~60

- IHL에 4로 나눈 값을 저장한다 --> 일반적으로 5가 됨

  

### TOS

- 비워둠 --> 0

  

### Total Length

- 전체의 길이

  

### Identification, IP Flags, Fragment Offset

#### Identification

- 하나의 데이터가 쪼개졌을 때, 원래 하나의 데이터였다는 것을 알려주기 위해 id를 부여함

#### IP Flags

- 3비트로 이루어짐
- D(Don't fragment): 데이터를 안쪽에서 보내겠다
- M: (More fragments)

#### Fragment OFfset

- 쪼개진 데이터를 원래대로 복구할 때, 순서를 알아볼 수 있게 Offset을 지정한다
- Offset: ~로부터 얼마만큼 떨어져있다



### Tiem To Live (TTL)

- 패키지가 살아있는 시간
- 주소를 잘못 설정했을 경우 계속 반복되는 걸 방지
- 컴퓨터의 운영체제를 알 수 있다
  - Window: 128, Linux: 64



### Protocol

- 상위 프로토콜이 무엇인지 알려준다



### Header Checksum

- 헤더에 오류가 있는지 확인한다 (값 비교)





### [ICMP 프로토콜](https://youtu.be/JaBCIUsFE74?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### ICMP가 하는 일

> ICMP(Internet Control Message Protocol, 인터넷 제어 메시지 프로토콜)
>
> 네트워크 컴퓨터 위에서 돌아가는 운영체제에서 오류 메시지를 전송 받는데 주로 쓰인다
>
> 프로토콜 구조의 Type과 Code를 통해 오류 메시지를 전송 받는다



### ICMP 프로토콜의 구조

> 특정 대상과 내가 통신이 잘 되는지 확인하는 ICMP 프로토콜

![image-20220911133731405](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911133731405.png)

### Type: 카테고리 (대분류)

- 기본: 0, 8
- 잘못됐을 때: 3(Destination Unreachable)-내 문제, 11(요청시간 만료)-상대방 문제(보통 방화벽)
- 보안상: 5

### Code: 카테고리 (소분류)





### [IPv4, ICMP프로토콜 실습](https://youtu.be/8ZwTvTuZlVw?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### Wireshark

```bash
ping 192.168.0.51
```

필터에 `icmp` 적용

![image-20220911134659961](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911134659961.png)

- Type: 8 === 요청

- Code(응답): 0





### [라우팅 테이블](https://youtu.be/CjnKNIyREHA?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### 내가 보낸 패킷은 어디로 가는가

> 어디로 보내야 하는지 설정되어 있는 라우팅 테이블

![image-20220911135257104](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911135257104.png)





## 다른 네트워크와 통신 과정

### 다른 네트워크까지 내 패킷의 이동 과정

> 내 컴퓨터에서 보낸 패킷이 다른 네트워크의 컴퓨터까지 어떻게 이동하는가

![image-20220911135727698](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911135727698.png)

- A의 라우팅 테이블
  - 192.168.0.0/24 --> 192.168.10.1
  - 192.168.20.0/24 --> 192.168.10.1

![image-20220911135948435](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911135948435.png)

 - 요청 프로토콜 작성
   - Type : 08
   - Code: 00
   - Checksum: 4d 56
   - 뒤에는 추가적으로 쓰고 싶은 거



![image-20220911140030183](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911140030183.png)

- IP 프로토콜 작성
  - 4: 버전
  - 5: 헤더 길이
  - 00: TOS
  - 00 3c: 전체 데이터 길이
  - 12 ab: 아이디 길이
  - 0: Flag
  - 0 00: Offset
  - 80: TTL
  - 01: 상위 프로토콜 타입
  - 00 00: 헤더 Checksum
  - c0 a8 0a 0a: 출발지 IP
  - c0 a8 14 14: 목적지 IP





### [라우팅 테이블 확인 실습](https://youtu.be/tVntagSJctc?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

```bash
// cmd 창에서 라우팅 테이블 확인
netstat -r
```

--> IPv4 경로 테이블 확인 가능





### [IPv4 조각화 이론](https://youtu.be/_AONcID7Sc8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### 조각화란?

> 큰 IP 패킷들이 적은 **MTU**(Maximum Transmission Unit)를 갖는 링크를 통하여 전송되려면 **여러 개의 작은 패킷으로 쪼개어/조각화 되어 전송**돼야 한다.
>
> 즉, 목적지까지 패킷을 전달하는 과정에 통과하는 각 라우터마다 전송에 적합한 프레임으로 변환이 필요하다
>
> 일단 조각화되면, 최종 목적지에 도달할 때까지 재조립되지 않는 것이 일반적이다.
>
> IPv4에서는 발신지 뿐만이 아니라 중간 라우터에서도 IP 조각화가 가능
>
> IPv6에서는 IP 단편화가 발신지에서만 가능
>
> 재조립은 항상 최종 수신지에서만 가능함

![image-20220911143141413](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911143141413.png)

> 여러 개의 패킷으로 조각화 된 패킷



### 큰 데이터를 전송하는 패킷이 조각화되는 과정

![image-20220911143657933](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911143657933.png)



![image-20220911143743439](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911143743439.png)

![image-20220911144025551](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911144025551.png)





### [IPv4 조각화 실습](https://youtu.be/QKEL9aBgHtg?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### 보내려는 데이터 크기: 2379

### MTU: 980

![image-20220911144301492](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220911144301492.png)

ab13: id



