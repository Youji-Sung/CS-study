# 비연결지향형 UDP 프로토콜

## UDP 프로토콜

### UDP가 하는 일

사용자 데이터그램 프로토콜(User Datagram Protocol, UDP)은 유니버설 데이터그램 프로토콜(Universal Datagram Protocol)이라고 일컫기도 한다.

UDP의 **전송 방식은 매우 단순**하여 서비스의 **신뢰성이 낮고**, 데이터그램 도착 순서가 바뀌거나, 중복되거나, 통보 없이 누락되기도 한다.

UDP는 일반적으로 **오류의 검사와 수정이 필요 없는** 프로그램에서 스행할 것으로 가정한다.



### UDP 프로토콜의 구조

![image-20220920215516623](8%EC%9E%A5_UDP_%EB%B9%84%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220920215516623.png)

**Source Port**: 출발지 포트번호

**Destination Port**: 도착지 포트번호

✔ Port번호: 0~65535. 총 2byte

**Lenght**: UDP프로토콜 header 길이 + payload

**Checksum**: 프로토콜이 이상한 것이 있는지 체크하는 값



## UDP프로토콜을 사용하는 프로그램

### DNS 서버

도메인주소를 물으면 IP주소를 알려주는 DNS서버

![image-20220920215829727](8%EC%9E%A5_UDP_%EB%B9%84%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220920215829727.png)



### tftp 서버

UDP로 파일을 공유하는 tftp 서버

![image-20220920215951046](8%EC%9E%A5_UDP_%EB%B9%84%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220920215951046.png)



### RIP 프로토콜

라우팅 정보를 공유하는 RIP 프로토콜

![image-20220920220051958](8%EC%9E%A5_UDP_%EB%B9%84%EC%97%B0%EA%B2%B0%EC%A7%80%ED%96%A5%ED%98%95.assets/image-20220920220051958.png)