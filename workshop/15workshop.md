# 15workshop

* bands 라는 테이블을 생성 후 값을 인서트 해줘서 완성

```python
 CREATE TABLE bands(
 id INTEGER PRIMARY KEY AUTOINCREMENT,                         
 name TEXT NOT NULL,
 debut INTEGER NOT NULL);
 
sqlite> INSERT INTO bands(name, debut)
   ...> VALUES('Queen', 1973);
sqlite> INSERT INTO bands(name, debut)
   ...> VALUES('Coldplay', 1998);                                     
sqlite> INSERT INTO bands(name, debut)
   ...> VALUES('MCR', 2001);          
```



* bands 테이블에서 모든 데이터 레코드의 id와 name만 조회하는 Query를 작성하라.

```python
SELECT id, name FROM bands;
```



* bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 Query를 작성하라.

```python
SELECT name FROM bands WHERE debut < 2000;
```

