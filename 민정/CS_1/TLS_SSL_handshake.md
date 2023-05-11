# TLS/SSL handshake

> TLS(Transport Layer Security)는 SSL(Secure Sockets Layer)의 향상된 버전
>
> SSL이 더 일반적인 용어

> handshake는 웹 클라이언트와 서버 간에 신뢰성을 수립하는 과정

HTTPS에서 `SSL 인증서`로 서버가 신뢰할 수 있는지 판단하기 위해 사용하는 `공개키 서명 방식`



## 1. ClientHello

![image-20230216192136626](https://user-images.githubusercontent.com/97648258/219338166-e40fd480-9c66-4961-b02a-8502b8819275.png)

`client hello` 메시지를 보냄

- SSL/TLS 버전
- 암호 알고리즘 목록
- 사용 가능한 압축 방식



## 2. ServerHello

![image](https://user-images.githubusercontent.com/97648258/219340487-71a2ad29-df72-46ef-bbee-600c3bb19e71.png)

`server hello` 메시지에 담아 응답

- 서버가 선택한 암호 알고리즘, 압축 방식
- 세션 ID
- CA가 사인한 서버의 공개 인증서
  - 대칭키가 생성되기 전까지 클라이언트가 나머지 handshake 과정을 암호화하는 데에 쓸 공개키를 담고 있음

- *클라이언트의 인증서 요청*



## 3. 클라이언트가 CA 목록 확인 --> 웹 서버 신뢰성 수립

![image](https://user-images.githubusercontent.com/97648258/219342436-8c19d44e-e7c9-4157-8496-5552c44309b4.png)

서버의 디지털 인증서가 유효한지 CA 목록을 확인한다

--> 신뢰성 수립



## 4. 클라이언트 키 익스체인지

![image](https://user-images.githubusercontent.com/97648258/219343263-020eb639-ad98-4cdf-b984-12450558bec2.png)

난수(pseudo-random) 바이트 생성해 `서버의 공개키`로 암호화

- `대칭키`를 정하는데 사용됨
  - 메시지 데이터를 암호화하는데 사용됨

*서버가 인증서를 요구한 경우*

- 클라이언트의 인증서 or "디지털 인증서 없음 경고"
  - 일부 구현에서 인증이 필수일 때 handshake 실패
- 클라이언트의 개인키로 암호화된 임의의 바이트 문자열



## 5. 클라이언트의 'Finished'

![image](https://user-images.githubusercontent.com/97648258/219343496-f09921b9-aa84-4d91-a84b-aaeccefd69d0.png)

handshake의 클라이언트 부분이 끝남

지금까지의 교환 내역을 해시한 값을 `대칭키`로 암호화하여 보냄





## 6. 서버의 'Finished'

![image](https://user-images.githubusercontent.com/97648258/219343673-4232a2c2-b357-4361-95ad-f1c82190ac83.png)

서버가 스스로 해시를 생성해 클라이언트의 값과 일치하는지 확인

`대칭키`를 통해 암호화한 메시지를 클라에게 보냄



## 이후

`대칭키`로 암호화된 HTTP 데이터를 주고 받는다







[참고]

- https://wangin9.tistory.com/entry/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90-URL-%EC%9E%85%EB%A0%A5-%ED%9B%84-%EC%9D%BC%EC%96%B4%EB%82%98%EB%8A%94-%EC%9D%BC%EB%93%A4-5TLSSSL-Handshake
- https://www.youtube.com/watch?v=sEkw8ZcxtFk





