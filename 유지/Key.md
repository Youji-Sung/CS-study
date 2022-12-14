# Key

> Key란? : 검색, 정렬시 Tuple을 구분할 수 있는 기준이 되는 Attribute. 유일한 기준이다.
>
> Tuple : 릴레이션(테이블)을 구성하는 각각의 행, 속성의 모임. 파일 구조에서는 레코드와 같은 개념이다.
>
> 튜플의 수 = Cardinality(전체 행에 대한 특정 컬럼의 중복 수치) = 기수 = 대응수
>
> 릴레이션 : 테이블과 같은 의미로 사용되며, 데이터의 집합을 의미한다. 튜플(tuple)과 속성(attribute)로 구성되어 있다.



<학생> 릴레이션

| 학번 | 주민번호       | 성명   | 성별 |
| ---- | -------------- | ------ | ---- |
| 1001 | 810429-1231457 | 김형석 | 남   |
| 1002 | 800504-1546781 | 김현천 | 남   |
| 1003 | 811216-2547842 | 류기선 | 여   |
| 1004 | 910322-1233445 | 홍영선 | 여   |



<수강> 릴레이션

| 학번 | 과목명 |
| ---- | ------ |
| 1001 | 영어   |
| 1001 | 전산   |
| 1002 | 영어   |
| 1003 | 수학   |
| 1004 | 영어   |
| 1004 | 전산   |



**1. 후보키 (Candidate Key)**

- 튜플을 유일하게 식별할 수 있는 속성들의 부분집합

- 모든 릴레이션은 반드시 하나 이상의 후보키를 가진다.

- 릴레이션에 있는 모든 튜플에 대해 유일성과 최소성을 만족시켜야 한다.

ex) <학생> 릴레이션에서 '학번'이나 '주민번호'는 다른 레코드를 유일하게 구별할 수 있는 기본키로 사용할 수 있으므로 후보키가 될 수 있습니다. 즉 기본키가 될 수 있는 키들을 후보키라고 합니다.



**2. 기본키 (Primary Key)**

- 후보키 중에서 선택한 주키(Main Key)

- 한 릴레이션에서 특정 튜플을 유일하게 구별할 수 있는 속성

- Null 값을 가질 수 없다.

- 기본키로 정의된 속성에는 동일한 값이 중복되어 저장될 수 없다.

ex) <학생> 릴레이션에는 '학번'이나 '주민번호'가 기본키가 될 수 있고, <수강> 릴레이션에는 '학번'+'과목명'으로 조합해야 기본키가 만들어 질 수 있습니다. <수강> 릴레이션에서는 '학번' 속성과 '과목명' 속성은 개별적으로 기본키로 사용할 수 없습니다. 

ex) <학생> 릴레이션에서 '학번'을 기본키로 정의하면 이미 입력된 '1001'은 다른 튜플의 '학번' 속성 값으로 입력할 수 없습니다.



> **Null 이란?**
>
> null은 원시값(Primitive Type) 중 하나로, 어떤 값이 **의도적으로** 비어있음을 표현한다. undefined는 값이 지정되지 않은 경우를 의미하지만, null의 경우에는 해당 변수가 어떤 객체도 가리키고 있지 않다는 것을 의미한다.
>
> - typeof undefined는 출력하면 undefined이다.
> - typeof null은 출력하면 object이다. 하지만 이는 여전히 원시 타입(primitive value)로, JavaScript에서는 구현 버그로 간주한다.
> - undefined == null은 true이다.
>
> **undefined란?**
>
> undefined는 원시값(Primitive Type)으로, 선언한 후에 값을 할당하지 않은 변수나 값이 주어지지 않은 인수에 자동으로 할당된다. 이 값은 전역 객체의 속성 중 하나로, 전역 스코프에서의 변수이기도 하다. 따라서 undefined 변수의 초기 값은 undefined 원시 값이다.
>
> 아래의 경우에서 undefined를 반환한다.
>
> - 값을 할당하지 않은 변수
> - 메서드와 선언에서 변수가 할당받지 않은 경우
> - 함수가 값을 return 하지 않았을 때
>
> **null과 undefined의 차이**
>
> `undefined`은 변수를 선언하고 값을 할당하지 않은 상태, `null`은 변수를 선언하고 빈 값을 할당한 상태(빈 객체)이다. 즉, `undefined`는 자료형이 없는 상태이다.



**3. 대체키 (Alternate Key)**

- 후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키들을 말한다.

- 보조키라고도 한다.

ex) <학생> 릴레이션에서 '학번'을 기본키로 정의하면 '주민번호'는 대체키가 됩니다. 



**4. 슈퍼키 (Super Key)**

- 슈퍼키는 한 릴레이션 내에 있는 속성들의 집합으로 구성된 키로서 릴레이션을 구성하는 모든 튜플 중 슈퍼키로 구성된 속성의 집합과 동일한 값은 나타내지 않는다.

- 릴레이션을 구성하는 모든 튜플에 대해 유일성은 만족하지만, 최소성은 만족시키지 못한다.

ex) <학생> 릴레이션에서는 '학번', '주민번호', '학번'+'주민번호', '학번'+'주민번호'+'성명' 등으로 슈퍼키를 구성할 수 있습니다. 또한 여기서 최소성을 만족시키지 못한다는 말은 '학번'+'주민번호'+'성명' 가 슈퍼키인 경우 3개의 속성 조합을 통해 다른 튜플과 구별이 가능하지만, '성명' 단독적으로 슈퍼키를 사용했을 때는 구별이 가능하지 않기 때문에 최소성을 만족시키지 못합니다. 즉 뭉쳤을 경우 유일성이 생기고, 흩어지면 몇몇 속성들은 독단적으로 유일성있는 키로 사용할 수 없습니다. 이것을 최소성을 만족하지 못한다고 합니다.



**5. 외래키 (Foreign Key)**

- 관계(Relation)를 맺고 있는 릴레이션 R1, R2에서 릴레이션 R1이 참조하고 있는 릴레이션 R2의 기본키와 같은 R1 릴레이션의 속성

- 외래키는 참조되는 릴레이션의 기본키와 대응되어 릴레이션 간에 참조 관계를 표현하는데 중요한 도구로 사용된다.
- 외래키로 지정되면 참조 테이블의 기본키에 없는 값은 입력할 수 없다.

ex) <수강> 릴레이션이 <학생> 릴레이션을 참조하고 있으므로 <학생> 릴레이션의 '학번'은 기본키이고, <수강> 릴레이션의 '학번'은 외래키입니다.

ex) <수강> 릴레이션의 '학번'에는 <학생> 릴레이션의 '학번'에 없는 값은 입력할 수 없습니다.