# 비연결지향형 UDP 프로토콜



## UDP가 하는 일

- 사용자 데이터그램 프로토콜 ( User Datagram Protocol )은 유니버설 데이터그램 프로토콜 ( Universal Datagram Protocel)이라고도 일컫기도 한다.
- UDP의 전송방식은 너무 단순해서 서비스의 신뢰성이 낮고, 데이터그램 도착 순서가 바뀌거나 중복되거나, 통보없이 누락되기도 한다.
- UDP는 일반적으로 오류의 검사와 수정이 필요 없는 프로그램에서 수행할 것으로 가정한다.



#### 안전한 연결을 지향하지 않는 UDP 프로토콜

![img](https://velog.velcdn.com/images%2Fcombi_areum%2Fpost%2Fe14de46f-a87c-4550-983b-2986fb831db1%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-12-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.06.17.png)

- 출발지 포트번호 ( 2바이트 ) / 목적지 포트번호 ( 2바이트 )
- Length = UDP 프로토콜 헤더 + 페이로드



## UDP 프로토콜을 사용하는 프로그램

#### 도메인을 물으면 IP를 알려주는 DNS 서버

![img](https://velog.velcdn.com/images%2Fcombi_areum%2Fpost%2F43e5cd5f-7ba1-4689-810d-820406de205c%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-12-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.09.24.png)



#### UDP로 파일을 공유하는 tftp서버

![img](https://velog.velcdn.com/images%2Fcombi_areum%2Fpost%2F21ea0fd2-da48-4d7f-8076-7d29a923f4e0%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-12-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.10.46.png)





#### 라우팅 정보를 공유하는 RIP 프로토콜

![img](https://velog.velcdn.com/images%2Fcombi_areum%2Fpost%2F9eee25f1-c099-4c9a-8a67-0414890e587b%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-12-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.11.18.png)