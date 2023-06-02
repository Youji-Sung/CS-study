## DCL

Data Control Language

데이터베이스 사용자에게 `권한을 부여/회수`하는 언어

- GRANT: 권한 부여

  ```sql
  GRANT 권한
  ON 테이블
  TO 유저;
  ```

- REVOKE: 권한 회수

  ```sql
  REVOKE 권한
  ON 테이블
  FROM 유저;
  ```

### 권한의 종류

- SELECT, INSERT, UPDATE, DELETE
- REFERENCES, ALTER, INDEX
- ALL

### GRANT 옵션

```sql
TO 유저
WITH GRANT OPTION;
# 특정 사용자에게 권한 부여가능한 권한을 부여함
```

```sql
TO 유저
WITH ADMIN OPTION;
# 테이블에 대한 모든 권한 부여
```



ROLE: 다양한 권한을 하나의 그룹으로 묶어서 관리





## DDL

Data Definition Language

데이터를 보관하고 관리하기 위한 객체의 `구조를 정의`하기 위한 언어

- ### CREATE: 구조 생성

  ```sql
  CREATE TABLE 테이블명 (
  	컬럼명 자료형
  	이름 varchar2(10),
  	생년 number(4)
  	첫방문일 date,
  	...
  );
  ```

  ### 구조

  - 컬럼명

    영문, 한글, 숫자 모두 가능

    (시작만 문자로)

    ex) h10 (o), 10h (x)

  - 데이터 타입

    - number: 숫자형

    - date: 날짜형

    - varchar2: 가변길이 문자열

      ex: '호호' != '호호    '

    - char: 고정된 크기 문자열

      할당된 길이만큼 문자 채움

      ex: '호호' = '호호   '

  ### 제약조건 (CONSTRAINT)

  ```sql
  CREATE TABLE 테이블명(
  	이름 varchar2(10),
  	생년 number(4) default 9999,
  	phone varchar2(15) not null,
  	첫방문일 date,
  	고객번호 varchar2(10) primary key
  );
  ```

  - default: 기본값 지정

  - not null: null 입력 불가

  - primary key: 기본키 지정

    - PK는 not null

    - PK는 unique한 값

      (테이블 내 중복 없음)

  - foreign key: 외래키 지정

    - 테이블 내 여러개 가능

- count(*): 전체 행의 수 카운트, null 포함
- count(컬럼명): null 제외한 행 수 카운트



- ### ALTER: 구조 수정

  테이블과 컬럼에 대해 이름 및 속성 변경, 추가/삭제 등 구조 수정을 위해 사용

  ```sql
  # 테이블명 변경
  ALTER TABLE 테이블명 RENAME TO 바꾸려는이름;
  
  # 컬럼명 변경
  ALTER TABLE 테이블명 RENAME COLUMN 컬럼명 TO 바꾸려는이름;
  
  # 컬럼 속성 변경
  ALTER TABLE 테이블명 MODIFY (이름 varchar(20) not null);
  
  # 컬럼 추가
  ALTER TABLE 테이블명 ADD (거주지역 varchar(10));
  
  # 컬럼 삭제
  ALTER TABLE 테이블명 DROP COLUMN 컬럼명;
  
  # 제약조건 추가/삭제
  ALTER TABLE 테이블명 ADD CONSTRAINT;
  				   DROP CONSTRAINT;
  ```

  ```sql
  # 테이블명 변경
  RENAME TABLE 테이블명 TO 바꾸려는이름;
  ```

  



- ### DROP: 테이블 및 컬럼 삭제

  ```sql
  # 컬럼 삭제
  ALTER TABLE 테이블명 DROP COLUMN 이름;
  
  # 테이블 삭제
  DROP TABLE 테이블명
  
  # 테이블 삭제 (유의)
  DROP TABLE 테이블명 CASCADE CONSTRAINT;
  --> 해당 테이블의 데이터를 외래키 (FK)로 참조한 제약사항도 모두 삭제
  --> Oracle에만 있는 옵션, SQL Server에는 존재하지 않음
  --> FK 제약조건과 참조테이블 먼저 삭제하고, 해당 테이블을 삭제한다
  ```

  ```sql
  # 테이블 삭제
  DROP TABLE 테이블명
  --> 테이블 관련해서 모두 삭제된다 (구조, 데이터)
  
  # 테이블 초기화
  TRUNCATE TABLE MENU
  --> 테이블 데이터만 삭제되고 구조는 살아있다
  ```

  |      | DROP                                      | TRUNCATE                                               |
  | ---- | ----------------------------------------- | ------------------------------------------------------ |
  |      | 테이블 정의를 완전 삭제                   | 테이블을 초기상태로 만든다                             |
  |      | 테이블이 사용했던 모든 저장공간을 Release | 테이블 최초 형성 시 사용했던 저장공간만 남기고 Release |

  