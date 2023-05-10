## 스케줄링의 목표

Batch System

- CPU 이용률을 높게
- 주어진 시간에 많은 일을 하게

Interactive System

- 응답 시간은 빠르게

- 준비 큐(ready queue)에 있는 프로세스는 적게

Real-time System

- 기한 맞추기





## 비선점형 방식

> 프로세스가 스스로 CPU 소유권을 포기하는 방식

### FCFS(First Come First Served)

- 큐에 도착한 순서대로 CPU 할당

- 길게 수행되는 프로세스 --> `준비 큐에서 오래 기다리는 현상(convoy effect)` 발생

### SJF(Shortest Job First)

- 실행 시간이 가장 짧은 프로세스를 가장 먼저 실행
- 평균 대기시간이 짧다
- 긴 시간을 가진 프로세스가 설행되지 않는 현상(starvation)이 일어난다
- 과거의 실행했던 시간을 토대로 추측해서 사용

### HRN(Highest Response-ration Next)

- `SJF`의 `starvation`  보완하기 위해 오래된 작업일 수록 `우선수위를 높인다(aging)`
- 우선순위 = (대기시간 + 실행시간) / (실행시간)





## 선점형 방식

> 현대 운영체제가 쓰는 방식으로, 지금 사용하고 있는 프로세스를 알고리즘에 의해 중단시켜버리고 강제로 다른 프로세스에 CPU 소유권을 할당하는 방식

### 라운드 로빈

- `우선순위 스케줄링(priority scheduling)`의 일종
- 각 프로세스는 동일한 할당시간을 주고 그 시간 안에 끝나지 않으면 다시 준비 큐의 뒤로 가는 알고리즘
- ex: N개의 프로세스가 운영됨, q만큼의 할당 시간(Time Quantum)이 부여됨
  - (N-1) * q 시간이 지나면 차례가 온다
  - 할당시간이 크면 `FCFS`, 짧으면 컨텍스트 스위칭이 잦아져서 `오버헤드`



### SRF

- 중간에 짧은 작업이 들어오면 수행하던 프로세스를 중지하고 해당 프로세스를 수행하는 알고리즘



### 다단계 큐

- 우선순위에 따른 준비 큐를 여러 개 사용한다
- 큐마다 다른 스케줄링 알고리즘을 적용함
- 우선순위가 높은 큐는 작은 Time Quantum 할당, 낮은 큐는  큰 TIme Quantum 할당 (다단계 피드백 큐)





## 스케줄링 척도

Response time(응답시간)

- 작업이 처음 실행되기까지 걸린 시간

Turnaround time(반환시간)

- 실행 시간과 대기 시간을 모두 합한 시간으로 작업이 완료될 때 까지 걸린 시간
- 짧을 수록 좋다

CPU Utilization(이용률, %)

- CPU가 수행되는 비율

Throughput(처리율, jobs/sec)

- 단위시간 당 처리하는 작업의 수(처리량)

Waiting time (대기시간)

- CPU를 점유하기 위해서 ready queue에서 기다린 시간







*참고*

- https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Operating%20System/CPU%20Scheduling.md
- https://m.blog.naver.com/PostView.nhn?blogId=so_fragrant&logNo=80056608452&proxyReferer=https:%2F%2Fwww.google.com%2F
- https://velog.io/@ich0906/CPU-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
- https://velog.io/@codemcd/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-6.-CPU-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81
- 면접을 위한 CS 전공지식 노트