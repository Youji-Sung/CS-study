# OSI 7계층

[참고영상](https://youtu.be/1pfTxp25MA8)



## Physical Layer (1계층)

### 두 대의 컴퓨터가 통신하려면?

- 모든 파일과 프로그램은 0과 1의 나열이다.
- 결국 0과 1만 주고받을 수 있으면 된다.

![image-20230206152137375](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152137375.png)

두 대의 컴퓨터를 전선 하나로 연결한다고 생각해보자.

- 1을 보낼 때는 +5V의 전기를 전선으로 흘려보내고
- 0을 보낼 때는 -5V의 전기를 전선으로 흘려보내면
- 0과 1의 전송이 가능할 것이다.

- 0과 1을 주고받을 수 있으면 모든 데이터를 주고받을 수 있으므로,
- 이제 두 컴퓨터는 모든 데이터를 주고받을 수 있게 되었다!

> 그러나 세상은 그렇게 만만하지 않은데..

- 이 간단한 아이디어는, 실제에선 잘 동작하지 않았습니다.
- 그 이유는 무엇일까요?

![image-20230206152330490](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152330490.png)

이런 그림 보신 적 있으신가요? 바로 sin 함수입니다!

- x축은 뭘까요? : 시간이네요!
- y축은 뭘까요? : 전압이네요!
- 이것은 전자기파를 표현하는 함수입니다.

![image-20230206152450490](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152450490.png)

- 이 전자기파의 주파수는 4Hz입니다.

> 하지만..

![image-20230206152521179](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152521179.png)

이 전자기파는 주파수 값이 숫자 하나로 고정되지 않습니다.

- 이 전자기파의 주파수 최솟값이 최댓값 10Hz, 최솟값 1Hz라고 해봅시다.

![image-20230206152620090](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152620090.png)

- 전선의 한계로 인해서 손상된 값을 얻게 됩니다.

> 그런데..

앞서 두 대의 컴퓨터가 통신하려면 0과 1을 주고받을 수 있으면 된다고 했습니다.

![image-20230206152712352](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152712352.png)

두 대의 컴퓨터는 이런 전자기파를 받을 수 있으면 됩니다.

하지만, 수직선과 수평선이 있는 전자기파는 항상 0 ~ 무한대 Hz의 주파수 범위를 가집니다.

따라서 이런 전기신호를 통과시킬 수 있는 전선은 없습니다.

그렇다면 이 신호를 어떻게 전송해야 할까요?

![image-20230206152759452](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152759452.png)

이렇게, 아날로그 식으로 바꿔서 전송해야 합니다.

![image-20230206152854115](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206152854115.png)

이렇게 데이터를 전송할 수 있게 됩니다.

### 그래서 결국 Physical Layer란?

- 0과 1의 나열을 아날로그 신호로 바꾸어 전선으로 흘려 보내고, (encoding)
- 아날로그 신호가 들어오면 0과 1의 나열로 해석하여 (decoding)
- 물리적으로 연결된 두 대의 컴퓨터가 0과 1의 나열을 주고받을 수 있게 해주는 모듈(module)

### Physical Layer 인코딩/디코딩

![image-20230206153053206](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153053206.png)

- 0101 0101을 아날로그 신호로 변조하는 것 : encoding
- 변조해주는 친구 : encoder

![image-20230206153127918](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153127918.png)

- 변조된 아날로그 신호로부터 원본을 해석해내는 것 : decoding
- 해석해주는 친구 : decoder

![image-20230206153236381](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153236381.png)

이 encoder와 decoder는 모두 함수에요.

### Physical Layer 기술은 어디에 구현되어 있을까?

- PHY 칩
- 사실 1계층 모듈은 하드웨어적으로 구현되어 있습니다.

> Data-Link Layer 시작하기 전에..

## 여러 대의 컴퓨터 간의 통신

![image-20230206153446959](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153446959.png)

예림이와 혜령이는 전선으로 연결되어 있으므로 컴퓨터로 데이터를 주고받을 수 있다.

![image-20230206153507232](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153507232.png)

그런데 예림이는 하빈이한테도 데이터를 보내고 싶어졌어요.

![image-20230206153525582](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153525582.png)

하빈이한테도 전선을 연결하고.. 그럼 어디까지 전선을 연결해야 하는 걸까요?

![image-20230206153545657](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153545657.png)

- 이런 방식은 전선 꽂을 구멍도 많이 필요하고 전선도 많이 필요
- 통신하려는 컴퓨터가 많아지면 많아질수록 비용 면에서 비효율적

> 따라서, 우리는 전선 하나를 가지고 여러 대의 컴퓨터와 통신할 방법을 찾아야 합니다.

![image-20230206153737786](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153737786.png)

전기가 통하는 구리선을 중앙에 두고, 혜림이한테 정보를 보내면 모든 컴퓨터가 이 정보를 받게 됩니다.

그래도 혜림이한테 정보를 전송하는 데에는 성공했네요!

그럼 중간에 전기가 통하는 구리선을 구겨서 빈 상자 안에 넣어보겠습니다.

![image-20230206153827272](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153827272.png)

이제 네 대의 컴퓨터는 통신할 수 있겠군요!

- 하지만, 예림이가 혜림이에게 보내면 다른 모든 컴퓨터가 알 수 있습니다.
- 그런데, 만일 이 상자가 메세지의 목적지를 확인해서 혜림이에게만 줄 수 있다면?

![image-20230206153907223](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153907223.png)

- 그런 똑똑한 상자가 스위치입니다. 스위치는 일종의 컴퓨터로서 이러한 일을 수행합니다.

![image-20230206153958498](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206153958498.png)

- 서로 다른 네트워크가 두 개 있습니다.
- 전선으로 연결되어 있지 않기 때문에, 통신할 수 없습니다.

![image-20230206154026359](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154026359.png)

그래서 스위치와 스위치를 연결했습니다.

이렇게 서로 다른 네트워크에 속한 컴퓨터끼리 통신하게 해주는 장비를

![image-20230206154101076](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154101076.png)

- **라우터**라고 합니다.
- 엄밀히 따지면 이 장비는 스위치 + 라우터인 L3스위치이지만, 그냥 라우터라고 뭉뚱그려 생각합시다..

![image-20230206154145459](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154145459.png)

이 때, 예림이와 혜림이가 통신할 수 있게 해주는 이 상자는 **공유기**에 해당합니다.

이제 더 많은 네트워크를 연결해봅시다.

![image-20230206154239535](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154239535.png)

이렇게 전 세계의 컴퓨터를 연결한 것을 **인터넷**이라고 합니다.

![image-20230206154314373](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154314373.png)

나라와 나라를 잇는 케이블은 짱 크겠죠?

![image-20230206154330262](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154330262.png)

실제로 바다 밑에 짱 크게 이어져 있습니다.

## Data-Link Layer (2계층)

![image-20230206154508003](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154508003.png)

4대의 컴퓨터가 통신합니다. 예림이는 받은 데이터를 잘못 끊어 읽으면 망하겠죠?

> 어떻게 해야 제대로 읽을 수 있을까요?

![image-20230206154626892](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154626892.png)

시작 부분에는 1111, 끝에는 0000을 붙여서 통신하기로 했습니다.

![image-20230206154648603](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154648603.png)

이렇게 해서, 예림이는 여러 발송지로부터 전달받은 데이터를 잘 끊어 읽을 수 있게 되었습니다.

### 그래서 결국 Data-Link Layer란?

- 같은 네트워크에 있는 여러 대의 컴퓨터들이 데이터를 주고받기 위해서 필요한 모듈
- Framing은 Data-link Layer에 속하는 작업들 중 하나입니다.
  - Framing : 1111이나 0000같은 것으로 원본 데이터를 감싸는 작업

![image-20230206154915340](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154915340.png)

데이터는 2계층 encoder에 들어가서 감싸져서 나온 후, 1계층 encoder에 들어가서 아날로그 신호가 됩니다.

![image-20230206154958130](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206154958130.png)

디코딩도 같은 방식으로 진행됩니다.

### Data-Link Layer 기술은 어디에 구현되어 있을까?

- 랜카드
- 2계층 모듈도 1계층 모듈처럼 하드웨어적으로 구현되어 있군요!

## Network Layer (3계층)

![image-20230206155214846](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206155214846.png)

A는 B에게 데이터를 보내고 싶어서 데이터 앞에 B의 목적지 주소를 붙였습니다.

![image-20230206155243978](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206155243978.png)

이렇게 각 컴퓨터들이 갖는 고유한 주소를 IP주소라고 합니다.

A가 B에게 데이터를 보내기 위해서는 B의 IP주소를 알아야 합니다. 어떻게 아는 걸까요?

> 궁금한 사람은 DNS를 공부해보세요. 데이터를 보낸다는건, 기본적으로 IP를 알고 있다는 뜻

![image-20230206155454657](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206155454657.png)

데이터 앞에 주소를 붙인 이 친구를 앞으로 **패킷**이라고 부르기로 했습니다.

패킷의 여행을 따라가봅시다.

1. `가`라우터로 갑니다.
2. `가`는 패킷을 열어서 목적지 IP주소를 확인합니다.
3. `가` : 나에게 연결된 친구 중에 없군! `마`에게 전달해야겠다.
4. `마`는 패킷을 까서 어디로 가야 하는지 확인합니다.
5. `마`는 `나`, `가`, `바` 중 어디로 보내야 할지 고민합니다.
   - 이게 궁금하다면, `라우터`를 공부해보세요! 우리는 알고 있다고 생각합시다.
6. `마`는 패킷을 다시 포장해서 `바`에게 보내줍니다.
7. `바`는 같은 방법으로 `라`에게 연결해 줍니다.
8. `라`는 B에게 패킷을 줍니다.

### 그래서 결국 Network Layer란?

- 수많은 네트워크 연결로 이루어지는 inter-network속에서
- 어딘가에 있는 목적지 컴퓨터로 데이터를 전송하기 위해,
- IP주소를 이용해서 길을 찾고(routing)
- 자신 다음의 라우터에게 데이터를 넘겨주는 것(forwarding)

![image-20230206160011667](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160011667.png)

지금까지와 같은 방법으로 차근차근 encoder를 탑니다.

![image-20230206160141955](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160141955.png)

라우터에서도 decoder를 탄 다음 다시 encoder를 탑니다.

### Network Layer 기술은 어디에 구현되어 있을까?

- 운영체제의 커널에 소프트웨어적으로 구현되어 있다.

## Transport Layer (4계층)

![image-20230206160250602](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160250602.png)

- 이제 인터넷 상의 모든 컴퓨터가 통신할 수 있게 되었습니다.

![image-20230206160316275](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160316275.png)

데이터를 받는 수신자는 전 세계의 컴퓨터로부터 데이터를 받을 것입니다.

> 그런데 컴퓨터에는 여러가지 프로그램이 실행되고 있었습니다.
> 실행 중인 프로그램 = 프로세스

![image-20230206160349952](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160349952.png)

컴퓨터는 저 세 개의 데이터를 프로세스들에게 나누어주려고 합니다.

- 어떤 데이터를 무슨 프로세스에게 줘야 하는지 컴퓨터는 어떻게 알 수 있을까요?
- 먼저, 데이터를 받고자 하는 프로세스들은 포트 번호(Port Number)라는 것을 가져야 합니다.

- 포트 번호란 하나의 컴퓨터에서 동시에 실행되고 있는 프로세스들이 서로 겹치지 않게 가져야하는 정수 값 입니다.

![image-20230206160545152](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160545152.png)

예를 들어, 코코아톡은 8081, 배달의 부족은 9000 포트번호를 가진다고 해봅시다.

![image-20230206160615903](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160615903.png)

한편, 송신자는 데이터를 보낼 때 데이터를 받을 수신자 컴퓨터에 있는 프로세스의 포트 번호를 붙여서 보냅니다.

- 그럼, 데이터 전송자는 9000이라는 포트번호까지 미리 알고 있어야 하나요?

- `네 맞습니다!`

![image-20230206160714931](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160714931.png)

> 그렇다고 합니다.

![image-20230206160800405](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160800405.png)

이런 식으로 포트번호가 붙어서 오고, 데이터를 하나하나 까서 프로세스한테 넘겨주게 됩니다.

### 그래서 결국 Transport Layer란?

- Port 번호를 사용하여
- 도착지 컴퓨터의 최종 도착지인 **프로세스**에 까지
- 데이터가 도착하게 하는 모듈

![image-20230206160946309](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206160946309.png)

요렇게 인코딩과 디코딩이 되어서 전달됩니다.

### Transport Layer 기술은 어디에 구현되어 있을까?

- 운영체제의 커널에 소프트웨어적으로 구현되어 있다.

## Application Layer (7계층)

OSI 네트워킹 모델은 그 구조가 총 7개의 Layer로 나뉘어져 있습니다.

> 그런데 왜 갑자기 5, 6계층을 건너뛰고 7계층으로 넘어가죠?

### OSI 모델 vs TCP/IP 모델

- 사실 현대의 인터넷은 OSI 모델이 아니라 TCP/IP 모델을 따르고 있습니다.
- TCP/IP 모델도 OSI 모델과 마찬가지로 네트워크 시스템에 대한 모델인데요.
- 현대의 인터넷이 TCP/IP 모델을 따르는 이유는 OSI 모델이 TCP/IP 모델과의 시장 점유 싸움에서 졌기 때문입니다.
- TCP/IP 모델은 어떻게 생겼을까요?

![image-20230206161340621](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206161340621.png)

OSI 7 Layer의 5, 6, 7계층이 뭉뚱그려졌네요!

>  속성이 조금씩 다른데, 앞에서는 왜 하나하나 나누어서 설명했나요?

- TCP/IP모델이 업데이트 되면서 조금 바뀌었어요.

![image-20230206161445771](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206161445771.png)

업데이트되면서 OSI 모델과 1, 2계층이 같아지고, 5, 6, 7계층은 여전히 뭉뚱그려져 있습니다.

오늘날에는 Updated 모델이 더 많이 사용되므로, 여기에 맞추어서 설명하겠습니다.

이제 다시 Application Layer로 돌아가겠습니다.

---

- TCP/IP 소켓 프로그래밍
  - 운영체제의 Transport layer에서 제공하는 API를 활용해서 통신 가능한 프로그램을 만드는 것을 TCP/IP 소켓 프로그래밍, 또는 네트워크 프로그래밍이라고 합니다.
  - 소켓 프로그래밍 만으로도 클라이언트, 서버 프로그램을 따로 만들어서 동작시킬수 있습니다.
  - 뿐만 아니라, TCP/IP 소켓 프로그래밍을 통해서 누구나 자신만의 Application Layer 인코더와 디코더를 만들 수 있습니다.
  - 누구든 자신만의 Application Layer 프로토콜을 만들어서 사용할 수 있다는 뜻입니다.
  - Application Layer도 다른 Layer들과 마찬가지로 인코더, 디코더가 있을 텐데요.
  - 대표적인 Application Layer 프로토콜인 **HTTP**로 인코딩 & 디코딩을 조금만 살펴봅시다.
  - HTTP를 이해하기 위해서는, 먼저 클라이언트 & 서버 패러다임을 알아야 합니다.
  - HTTP에 익숙할 거에요. 세부적인 부분에서도요.. 만일 아니라면,
    - header, body, request, response, status code..등이 익숙하다면, 익숙한 것입니다.
    - 그러니 이미 알고 있는 지식을 활용해보겠습니다.

![image-20230206162055717](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230206162055717.png)

요렇게 전송이 됩니다.

## 마치며..

- MVC 패턴은 소프트웨어 아카텍처 중 하나입니다.
- MVC와 마찬가지로, 소프트웨어 아키텍처 중에 Layered Architecture라는 게 있습니다.
- Layered 아키텍처를 따르는 대표적인 예가 네트워크 시스템입니다.
- 그러니, 네트워크 시스템은 하나의 거대한 소프트웨어라고 할 수 있습니다.
- OSI 7 Layer 모델은 거대한 네트워크 소프트웨어의 구조를 설명하는 것입니다.