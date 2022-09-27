# TCP 연결지향형

## TCP 프로토콜

✔ 연결을 지향하기 때문에 UDP보다 안정적인 통신을 제공한다.

✔ 통신을 한다할 때 대부분 TCP, IPv4, Ethernet protocol을 사용한다.

✔ payload에 따라 어떤 데이터를 전달해주는 지가 달라진다.



### TCP가 하는 일

전송 제어 프로토콜(Transmission Control Protocol, TCP)은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 **안정적**으로, **순서대로**, **에러 없이** 교환할 수 있게 한다.

TCP의 안정성을 필요로 하지 않는 애플리케이션의 경우 일반적으로 TCP대신 비접속형 사용자 데이터그램 프로토콜(User Datagram Protocol)을 사용한다.

TCP는 UDP보다 안전하지만 느리다.

* 체감할 수 있는 정도로 느리지 않다.



### TCP 프로토콜의 구조

UDP와 비교하여 구조가 복잡하다.

![image-20220927124655536](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927124655536.png)

**Source Port**: 출발지 포트 2byte

**Destination Port**: 도착지 포트 2byte

**Sequence Number**: 4byte

**Acknowledgment Number**: 4byte

**Offset**: Header의 길이를 의미한다.

**Reserved**: 예약된 필드로 사용하지 않는 필드를 의미한다.

**Window**: 

TCP는 연결을 지향한다. 

상대방과 연결이 된 상태에서 데이터를 주고 받는다.

TCP는 보내는 것, 잘 받았는지 확인하는 것을 하는 데 그 때 얼마나 더 보내는지 확인할 때 사용한다.

내 사용공간이 얼마나 남았는지 상대방에게 알려주는 것이다.

**Checksum**

**Urgent Pointer**

✔ TCP 플래그에서 학습

* TCP Flags의 긴급 데이터가 어디서부터가 긴급데이터인지 알려주는 위치값

**TCP Options(variable length, optional)** 

* IP프로토콜과 마찬가지로 일반적으로 붙지 않는다.
* 4byte씩 최대 10개까지 붙는 Option
* 가장 일반적인 길이는 20byte이나 최대 60byte까지 늘어날 수 있다.



## TCP 플래그

![image-20220927202514811](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927202514811.png)

이 중에서 **U A P R S F**를 중점적으로 보면 된다.

**👉 URG(Urgent)**

**👉 ACK(Acknowledgement)**

**👉PSH(Push)**

**👉RST(Reset)**

**👉SYN(Synchronize)**

**👉FIN(Finish)**



TCP는 계속해서 통신하면서 상대방과 연결상태를 물어본다.

여러 정보를 나타내는 것이 이 Flag값이다.

Flag의 setting에 따라 

* 연결하려고 물어보는 것인지
* 데이터를 보내도 된다고 대답을 하는 것인지
* 연결을 종료하려는 것인지
* 연결을 초기화하려는 것인지
* 데이터를 보내는 것인지
* 데이터가 급한 데이터인지 아닌지 등

✔ TCP의 주된 기능이 Flag로 나눠진다.



**A**: 승인을 할 때 보내주는 Flag

**P**: TCP버퍼가 일정크기 만큼 쌓여야 패킷을 추가로 전송하는데 그것과 상관없이 데이터를 push하겠다는 것

**R**: 초기화 비트, 상대방과 연결이 되어있는 상태에서 추가적으로 데이터를 주고받으려고 하는데 문제가 발생되어 Reset을 하자고 하는 것

**S**: **중요** 동기화 비트, 상대방과 연결을 시작할 때 무조건 실행하는 플래그, S플래그 보내진 후부터 상대방과 동기화

**F**: 종료비트, 연결을 끊을 때 사용하는 Flag



✔ Flag의 모습

![image-20220927203421343](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927203421343.png)

## TCP를 이용한 통신과정

### 연결 수립 과정

TCP를 이용한 데이터 통신을 할 때 프로세스와 프로세스를 연결하기 위해 **가장 먼저 수행되는 과정**

1. 클라이언트가 서버에 요청 패킷을 보내고
   * 서버가 먼저 요청을 보내는 경우 없다.
2. 서버가 클라이언트의 요청을 받아들이는 패킷을 보내고
3. 클라이언트는 이를 최종적으로 수락하는 패킷을 보낸다.

**위의 3개의 과정을 3Way Handshake라고 부른다.**

✔ 이 과정이 지나고 난 뒤에 데이터 전달이 시작된다.



### TCP 3Way Handshake

연결 수립을 하기 위한 통신

![image-20220927204311328](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927204311328.png)



**Client**

* Chrome 프로그램



**Web Server**

* Apache (daum, nate)
* Tomcat
* Nginx (naver)

![image-20220927204532382](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927204532382.png)

**02**: SYN Flag

✔ **IPv4 프로토콜과 Eth 프로토콜을 세팅해서 웹서버로 보낸다.**

❗ Flag는 SYN, S(SEQ 번호, 시퀀스 번호), A(ACK번호)는 0으로 세팅된다.

![image-20220927204904366](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927204904366.png)

✔ 서버가 decapsulation해서 내용확인 Flag를 확인하고 답장 작성

❗ Flag는 SEQ번호와 ACK번호가 같이 세팅된다.

![image-20220927204948606](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927204948606.png)



✔ encapsulation하여 다시 클라이언트로 보낸다.

❗ Flag는 A(ACK번호)만 세팅된다.

![image-20220927205026174](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927205026174.png)

![image-20220927205100057](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927205100057.png)

🎇 네트워크 보안까지 가면

**S:100 A:0**

**S:2000 A:101**

**S:101 A:2001**

까지 도 알아야한다.



처음에 Client가 SEQ번호를 100으로 세팅, ACK번호를 0으로 세팅 (SEQ번호는 랜덤으로 Client에서 세팅된다.)

받는 쪽에서 SEQ번호값과 동기화한다. 동기화를 컴퓨터는 이 번호를 가지고 한다.

받는 쪽에서 답장을 보내는 쪽으로 줄때 ACK번호는 **SEQ번호 + 1**, SEQ번호는 처음 보내는 것이므로 랜덤한 번호로 세팅한다.

SEQ번호와 ACK번호를 받은 Client입장에서 ACK번호는 **받은 SEQ번호 + 1**, SEQ번호는 이전과 동일한 100로 보낸다. (서로 동기화 되었기 때문이다.)



### 데이터 송수신 과정

TCP를 이용한 데이터 통신을 할 때 단순히 TCP 패킷만을 캡슐화해서 통신하는 것이 아닌 페이로드를 포함한 패킷을 주고 받을 때의 일정한 규칙

1. 보낸 쪽에서 또 보낼 때는 SEQ번호와 ACK번호가 그대로다.
2. 받는 쪽에서 SEQ번호는 받은 ACK번호가 된다.
3. 받는 쪽에서 ACK번호는 받은 SEQ번호 + 데이터의 크기

✔ 이전에는 Payload가 없었고 보낸 쪽의 SEQ번호 + 1이 ACK번호가 되었었다.

✔ 데이터가 있으면 Payload가 있으므로 받은 SEQ번호 + 데이터의 크기가 된다.



**데이터를 포함한 통신**

HTTP나 FTP와 같은 데이터를 포함한 통신

![image-20220927210739601](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927210739601.png)

![image-20220927210759538](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927210759538.png)

✔ 이전 연결하던 때에서 이어서 SEQ번호: 101, ACK번호: 2001

![image-20220927210846739](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927210846739.png)



![image-20220927210859362](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927210859362.png)

✔ 보낸 SEQ번호:101 + Data(100) => ACK번호: 201

![image-20220927211127492](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927211127492.png)

✔ ACK번호이었던 201이 SEQ번호. SEQ번호: 2001 + Data(500) => 2501이 ACK번호

![image-20220927211449067](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927211449067.png)



## TCP 상태전이도

### TCP 연결 상태의 변화

![image-20220927211536642](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927211536642.png)

**실선: Client의 상태변화**

**점선: Server의 상태변화**



여러 상태 중 중요한 두 상태

**✔ LISTEN**

* 4계층은 포트번호를 사용한다.
* 포트번호를 서버쪽에서 사용하고 있어서 클라이언트 쪽을 듣고 있는 상태

**✔ ESTABLISHED**

* 연결이 서로 수립되어 있는 상태
* 3way handshake과정이 끝나면 ESATBLISHED상태가 된다.



Client는 포트를 사용할 때 **active open**하면서 **SYN를 전달** => SYN_SENT

SYN를 받은 서버는 **<u>SYN_RCVD</u>상태**되면서 **SYN, ACK**을 보내게 된다.

![image-20220927212119538](9%EC%9E%A5_TCP_%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220927212119538.png)
