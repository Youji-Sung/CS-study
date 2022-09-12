## ARP 프로토콜

### ARP가 하는 일

IP주소로 통신하나 실제 같은 네트워크 대역에서 필요한 것은 MAC주소이다.

IP주소를 입력하더라도 컴퓨터들끼리 상대방의 MAC주소를 알아와 통신하게 되는데 MAC주소를 알아오는 프로토콜이 ARP프로토콜이다.

 **=> ARP 프로토콜은 같은 네트워크 대역에서 통신을 하기위해 필요한 MAC주소를 IP주소를 이용하여 알아오는 프로토콜이다.**

같은 네트워크 대역에서 통신을 한다고 하더라도 데이터를 보내기 위해서는 7계층부터 캡슐화를 통해 데이터를 보내기 때문에 IP주소와 MAC주소가 모두 필요하다.

이때, IP주소는 알고 MAC주소는 모르더라도 ARP를 통해 통신이 가능해진다.



**❗ ARP가 중요하게 여겨지는 이유**

보안상 중요하게 이야기되어진다.



### ARP 프로토콜의 구조

IP주소를 이용해 MAC주소를 알아오는 ARP 프로토콜

![image-20220913005313584](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913005313584.png)



✔ **Source Hardward Address**

출발지의 물리적인 주소(MAC주소) : 출발지의 MAC주소 6byte

**✔ Source Protocol Address**

IPv4 주소를 의미 4byte

✔ **Destination Hardware Address**

목적지의 MAC주소 6byte

**✔ Destination Protocol Address**

목적지의 IP주소 4byte

❗ 이더넷 프로토콜을 제외한 모든 프로토콜은 출발지가 먼저 온다.

❗ 이더넷 프로토콜은 목적지가 먼저 온다.



**✔ Hardware type**

2계층에서 사용하는 프로토콜의 타입(가장 많이 보는 것은 Ethernet Protocol : 0001)

**✔ Protocol type**

Source Protocol Address에서 사용하는 프로토콜의 타입: IPv4밖에 없다. 0800

**✔ Hardware Address Length**

MAC주소의 길이: 6byte 따라서 06

**✔ Protocol Address Length**

Protocol 주소의 길이: IPv4주소 따라서 04

**✔ Opcode**

Operation code

어떻게 동작하는지를 나타내는 코드

ARP 프로토콜로

1️⃣ 상대방의 MAC주소를 요청		 	**0001**
2️⃣ 상대방의 MAC주소 요청에 응답	**0002**

[거의 예외 없이 고정된 값이 있다.]

**0001 0800**

**0604 000**



## ARP 프로토콜의 통신 과정

IP주소만 알고 있을 때 **ARP로 MAC주소**를 알아오기

![image-20220913021712209](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913021712209.png)

**같은 LAN대역에서** A컴퓨터가 C컴퓨터의 MAC을 알고자 한다.

A컴퓨터가 ARP 요청 프로토콜을 만든다. -> 이를 캡슐화해서 보낸다.

* ARP은 3계층 프로토콜이기 때문에 2계층 Eth(이더넷) 프로토콜을 앞에 붙여서 보낸다.

![image-20220913021937161](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913021937161.png)

다음과 같이 작성된다.

0001 0800

0604 0001(요청)

출발지 MAC주소, 출발지 IP주소 자신의 것 사용한다.

(aa aa aa aa aa aa) (c0 a8 00 0a: 16진수)

도착지 MAC주소는 00 00 00 00 00 00으로 비워둔다.

도착지 IP주소는 16진수로 사용한다.

![image-20220913022254963](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913022254963.png)

Ethernet Protocol을 캡슐화한다.

목적지의 MAC주소를 모르기 때문에 FF FF FF FF FF FF로 작성한다.

MAC주소를 전부 1로 채우면 Broadcast 주소가 된다.

따라서 이 프로토콜을 작성하여 같은 대역 내의 모두에게 보낸다.



스위치: ![image-20220913022527638](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913022527638.png)

대표적인 2계층 장비로 2계층 프로토콜 까지만 확인한다. 

Ethernet Protocol만 확인하고 목적지 주소가  Broadcast이므로 모두에게 보낸다.

이를 받은 모두가 decapsulation을 한다.

2계층 decapsulation하고 Broadcast인 것 확인 후 3계층 decapsulation한다.

본인의 IP주소와 일치하지 않는 경우 패킷을 버린다.

본인의 IP주소와 일치하는 경우 그에 맞는 응답 프로토콜을 만들어서 준다.

![image-20220913022843289](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913022843289.png)

다음과 같이 작성된다.

0001 0800

0604 0002(응답)

출발지 MAC주소, 출발지 IP주소 자신의 것 사용한다.

(cc cc cc cc cc cc) (c0 a8 00 0a: 16진수)

도착지 MAC주소는 aa aa aa aa aa aa으로 작성된다. 

(이미 목적지 MAC주소를 알고 있다. Broadcast 필요하지 않다.)

도착지 IP주소는 16진수로 사용한다.



스위치가 2계층까지 decapsulation하여 컴퓨터 A에 전달한다.

A는 C의 MAC주소를 알게 되고 이를 ARP 캐시 테이블에 이 내용을 등록한다.

![image-20220913023158821](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913023158821.png)

**최초의 통신을 할 때 반드시 한번 위 과정이 실행이 된 후 통신이 된다.**



## ARP 테이블

통신했던 컴퓨터들의 주소는 **ARP 테이블**에 남는다.

`arp -a`로 확인할 수 있다.

영구적으로 저장되는 것은 아니고 일정시간이 지나면 지워진다.

![image-20220913023305947](5%EC%9E%A5_ARP_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C.assets/image-20220913023305947.png)
