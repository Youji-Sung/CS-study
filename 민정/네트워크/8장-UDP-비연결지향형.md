### [UDP 프로토콜](https://youtu.be/3MkI3FBFzX8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### UDP가 하는 일

- 사용자 데이터 프로그램(User Datagram Protocol, UDP)은 유니버셜 데이터그램 프로토콜(Universal Datagram Protocol)이라고 일컫기도 한다
- UDP의 **전송방식은 너무 단순**해서 서비스의 **신뢰성이 낮고**, 데이터그램 도착 순서가 바뀌거나, 중복되거나, 심지어는 통보 없이 누락시키기도 한다.
- UDP는 일반적으로 **오류의 검사와 수정이 필요 없는** 프로그램에서 수행할 것을 가정한다.



> 안전한 연결을 지향하지 않는 UDP 프로토콜

-![image-20220918163143982](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918163143982.png)



## UDP 프로토콜을 사용하는 프로그램

### UDP 프로토콜을 사용하는 대표적인 프로그램들

> 도메인을 물으면 IP를 알려주는 `DNS 서버 `

![image-20220918164239389](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918164239389.png)



> UDP로 파일을 공유하는 tftp 서버

![image-20220918164323650](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918164323650.png)



> 라우팅 정보를 공유하는 RIP 프로토콜

![image-20220918164342847](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220918164342847.png)







### [tftpd로 파일 전송 실습](https://youtu.be/5Woau-EJChw?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

## 1. tftpd를 사용하여 데이터 공유해보기

- tftpd 프로그램을 이용해 UDP를 이용한 데이터 통신 해보기



## 2. 패킷 캡쳐 및 분석해보기

- UDP 패킷을 캡쳐해보고 분석해보기

  