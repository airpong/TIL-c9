# 1. create_table

```sqlite
CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
.mode csv
.import boxoffice.csv movies
.headers on
.mode column
SELECT * FROM movies;
```

- `.mode csv `
  - 쉘이 INPUT 파일을 csv 로 읽기 위한 모드를 변경
- `.import boxoffice.csv movies`
  - csv 파일을 내가 만든 movies 테이블에 입력
- `.headers on`
  - 헤더 입력
- `.mode column`
  - 모드를  column 으로 변경

# 2. crud

## C

```sql
INSERT INTO movies VALUES(20182530,'극한직업','15세이상관람가','이병헌',20190123,3138467,111,'한국','코미디');
```

- INSERT INTO (테이블명) (COL1,COL2,...(디폴트는 전체)) VALUES(...)

## R

```sql
SELECT * FROM movies WHERE 영화코드=20185124;
```

- SELECT (원하는 컬럼) FROM (테이블) WHERE (조건)

## U

```sql
UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;
```

- UPDATE (테이블) SET (변경할려는 컬럼) WHERE (조건)

## D

```sql
DELETE FROM movies WHERE 영화코드=20040521;
```

- DELETE FROM (테이블) WHERE (조건)

# 3.SELECT

```sql
SELECT 영화이름 FROM movies WHERE 상영시간>=150;
SELECT 영화코드,영화이름 FROM movies WHERE 장르='애니메이션';
SELECT 영화이름 FROM movies WHERE 장르='애니메이션' AND 제작국가='덴마크';
SELECT 영화이름,누적관객수 FROM movies WHERE 누적관객수>1000000 AND 관람등급='청소년관람불가';
SELECT * FROM movies WHERE 개봉연도 BETWEEN '20000101' AND '20091231';
SELECT DISTINCT 장르 FROM movies;

```

1. 상영시간 이 150분 이상인 데이터의 영화이름 출력 
   1. =,<,<= 등 여러 비교연산자 사용가능
2. 장르가 '애니메이션' 인 데이터중 영화코드,이름 출력
3. WHERE 안에 AND 혹은 OR 을 사용가능해 이중 조건 사용가능
4. 3번과 동일
5. BETWEEN syntex를 사용해 두날짜 사이의 데이터 출력
6. DISTINCT = 중복제거

# 4.expression

```sql
SELECT SUM(누적관객수) FROM movies;
SELECT 영화이름,max(누적관객수) FROM movies;
SELECT 장르,min(상영시간) FROM movies;
SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';
SELECT COUNT(*) FROM movies WHERE 장르='애니메이션' AND 상영시간>=100;
```

1. SUM 함수 - 원하는 컬럼의 값을 더해준다
2. max - 원하는 컬럼의 최대값을 출력
3. min- 원하는 컬럼의 최소값 출력
4. AVG - 원하는 컬럼의 평균 출력
5. count - 조건에 부합하는 데이터의 개수 출력

# 5.order

```sql
SELECT * FROM (SELECT * FROM movies ORDER BY 누적관객수 DESC) limit 5;
SELECT * FROM movies WHERE 장르 = '애니메이션' ORDER BY 제작국가 ASC,누적관객수 DESC limit 10;
SELECT 감독 FROM movies ORDER BY 상영시간 DESC limit 10;
```

1. sqlite 가 제공하는 syntex (limit ) - 원하는 개수만큼 출력가능

2. 두개의 조건으로 정렬 가능, 처음 조건으로 정렬한뒤 같은것이 같은 조건이라면 뒤의 조건으로 정렬
