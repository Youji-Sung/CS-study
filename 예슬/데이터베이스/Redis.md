## Redis (Remote Dictionary Server)

> Remote(원격)에 위치하고 프로세스로 존재하는 **In-Memory 기반**의 key-value 구조(NoSQL) 데이터 관리 Server 시스템

- 메모리 기반이라 모든 데이터들을 메모리에 저장하고 빠른 접근 속도를 가짐
- DB, Cache, Message Queue, Shared Memory 용도로 사용
  - 인증 토큰, Ranking 보드(Sorted Set), 유저 API Limit

- 메모리 기반이지만 Redis는 **영속적인 데이터 보존(Persistence)**이 가능
  - RDB (snapshotting) : 특정한 각격마다 메모리에 있는 레디스 데이터 전체를 디스크에 백업
  - AOF (Append Only File) :  write/update 연산 자체를 모두 log 파일에 기록 → 서버가 재시작될 때 연산 재실행하여 데이터 복구 

- 다양한 자료 구조 지원
  - string, list, set, sorted set, hash 등  

- 싱글 스레드 기반, 여러 프로세스에서 동시에 같은 key에 대한 갱신을 요청하는 경우, 데이터 부정합 방지 Atomic 처리 함수를 제공 (원자성)





##### ☹ 주의

- O(n) 명령어 지양
  - 싱글 스레드 기반 → 처리 시간이 긴 명령어가 들어오면 그 뒤에 명령어는 대기 상태로 전환
- 메모리 관리 
  - 메모리 파편화
    - 메모리를 할당하고 해제하는 과정에서 빈 공간이 생김. 이후, 빈 공간보다 더 큰 메모리를 할당하게 되면 빈 공간은 채워지지 않게되고 메모리 낭비
  - 쓰기 연산이 copy on wirte 방식으로 동작하기 때문에 최대 메모리를 2배 이상까지 사용



