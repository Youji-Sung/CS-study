### [HTTP 프로토콜](https://youtu.be/TwsQX1AnWJU?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

## 웹을 만드는 기술들

### 웹을 만들기 위해 사용되는 다양한 기술들

#### 필수

- HTTP (HTTPS --> SSL/TLS)
  - HTTPS: HTTP에 보안적인 요소(SSL/TLS)를 추가함
  - HTML과 JS와 CSS 같은 파일을 웹 서버에게 요청하고 받아오는 프로토콜
- HTML
  - 웹 페이지를 채울 내용
- Javascript
  - 웹 페이지에 들어갈 기능
- CSS
  - 웹 페이지를 예쁘게 꾸밀 디자인

##### 웹 서버 페이지를 만드는 기술들

- ASP / ASP.NET
- JSP
- PHP

- DB

#### 선택

- Python
- Spring
- Jquery
- Ajax



## HTTP 프로토콜

### HTTP 프로토콜의 특징

> HyperText Transfer Protocol (하이퍼 텍스트 전송 프로토콜)
>
> www에서 쓰이는 핵심 프로토콜로 문서의 전송을 위해 쓰이며, 오늘날 거의 모든 웹 애플리케이션에서 사영되고 있다
>
> ​	--> 음성, 화상 등 여러 종료의 데이터를 MIME으로 정의하여 전송 가능
>
> HTTP 특징
>
> ​	--> Request / Response (요청/응답) 동작에 기반하여 서비스 제공

> HTTP 1.0의 특징
>
> - '연결 수립, 동작, 연결 해제'의 단순함이 특징
>
>   --> 하나의 URL은 하나의 TCP 연결
>
>   HTML 문서를 전송 받은 뒤 연결을 끊고 다시 연결하여 데이터를 전송한다
>
> HTTP 1.0의 문제점
>
> - 단순 동작 (연결 수립, 동작, 연결 해제)이 반복되어 통신 부하 문제 발생

![12](https://user-images.githubusercontent.com/97648258/194865449-9d616c81-7536-4553-91a2-f1a32899d553.png)

![111](https://user-images.githubusercontent.com/97648258/194865682-ee2ff67f-7d19-4309-850d-6a9f2f19c07a.png)





### [HTTP 요청 프로토콜](https://youtu.be/rxaBwwI_JnI?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- HTTP Method 설명 중 GET, POST만 사용해야 한다고 하지만 개발자 입장에서 RESTful API 개발시 PUT, DELETE도 사용하는게 원칙임

### HTTP 요청 프로토콜의 구조

- 요청하는 방식을 정의 하고 요청 프로토콜 구조 // 클라이언트의 정보를 담고 있는

1. Request Line
   - 요청 타입
     - GET : Client가 Server로부터 문서를 읽어오려 할 때 사용
     - POST : Client가 Server에게 어떤 정보를 전송할 때 사용
   - 공백
   - URI
   - 공백
   - HTTP 버전
2. Headers
3. 공백
4. Body



### [URL, URI란?](https://youtu.be/2ikhZ_fNP5Y?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### Uniform Resource Identifier

![제목 없음](https://user-images.githubusercontent.com/97648258/194867937-a2144f86-33f8-4a59-9fa2-497df9d18b7b.png)



### [HTTP 요청 프로토콜 작성 실습](https://youtu.be/XbGJYsxed2w?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- `GET / HTTP/1.1`



### [URI 이해를 위한 실습](https://youtu.be/HBojczyd1Ac?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 

### [HTTP 응답 프로토콜](https://youtu.be/kuucNF4Zvbs?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### HTTP 응답 포로토콜의 구조

> 서버가 알려주는 여러가지 정보 : 상태 코드

| 상태 코드 종류 | 설명                                             |
| -------------- | ------------------------------------------------ |
| 100~199        | 단순한 정보                                      |
| 200~299        | Client의 요청이 성공                             |
| 300~399        | Client의 요청이 수행되지 않아 다른 URL로 재지정  |
| 400~499        | Client의 요청이 불완전하여 다른 정보가 필요      |
| 500~599        | Server의 오류를 만나거나 Client의 요청 수행 불가 |



#### 성공적인 통신 200 OK

- 200 : 상태 문구 (OK) : Client의 요청이 성공했다는 것을 나타낸다



#### 클라이언트의 실수, 잘못, 오류

| 상태 코드 종류 | 상태 문구 | 설명                                      |
| -------------- | --------- | ----------------------------------------- |
| 403            | Forbidden | Client가 권한이 없는 페이지를 요청했을 때 |
| 404            | Not Found | Client가 서버에 없는 페이지를 요청했을 때 |



#### 서버의 실수, 잘못, 오류

| 상태 코드 종류 | 상태 문구             | 설명                                      |
| -------------- | --------------------- | ----------------------------------------- |
| 500            | Internet Server Error | Server의 일부가 멈췄거나 설정 오류가 발생 |
| 503            | Service Unavailable   | 최대 Session 수를 초과했을 때             |





### [HTTP 헤더 포맷](https://youtu.be/mQTGmxendk8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

### 일반 헤더

#### 일반적인 정보를 담고 있는 일반 헤더

| 헤더 종류      | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| Content-Length | 메시지 바디 길이를 나타낼 때 쓰인다                          |
| Content-Type   | 메시지 바디에 들어있는 컨텐츠 종류 (Ex: HTML 문서는 text/html) |



### 응답 헤더

#### 서버 정보를 담고 있는 응답 헤더

| 헤더 종류  | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| Server     | 사용하고 있는 웹서버의 소프트웨어에 대한 정보를 포함         |
| Set-Cookie | 쿠키를 생성하고 브라우저에 보낼 때 사용. 해당 쿠키 값을 브라우저가 서버에게 다시 보낼 때 사용한다 |





### [HTTP 프로토콜 분석 실습](https://youtu.be/dhMrKTwNI8U?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

