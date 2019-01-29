# 15homework

1. 우리가사용하는SQLite는RDBMS에속한다.RDBMS의특징을2가지만작성하세요.

   -   데이터베이스 테이블을 재구성하지 않더라도 다양한 방법으로 접근하거나 조합
   -    관계형 데이터베이스는 만들거나 이용하기가 비교적 쉽지만, 무엇보다도 확장이 용이하다는 장점


2. True False

  2.1. RDBMS를 조작하기 위해서는 SQL문을 사용한다.[ o ]
  2.2. SQL에서 명령어는 대문자로 써야만 동작한다.[ x ]
  2.3. 일반적인 SQL문에서 명령어는세미콜론(;)  으로 끝난다.[ o ]
  2.4. SQLite에서 dot(.)으로시작하는 명령어는 SQL이아니다.[ o ] 
  2.5. 한개의 DB에는 한개의 테이블만 존재한다. [ x ]



  3.다음코드의실행결과로나타나는값을작성하세요.
  sqlite> .nullvalue“NULL”
  sqlite> CREATE TABLE ssafy(
  …> id INTEGER,
  …> location TEXT,
  …> class INTEGER
  …> );
  sqlite> INSERT INTO ssafy(id, location)
  …> VALUES (1, ‘JEJU’);
  sqlite> SELECT class FROM ssafyWHERE id=1;



NULL 이 뜹니다.