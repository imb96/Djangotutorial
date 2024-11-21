# Django Tutorial

### Install Python

1. [Python Download](https://www.python.org/downloads/)
2. python 설치 확인

```bash
python3 --version
```

3. Django 설치

```bash
pip3 install django
```

4. django 설치 확인

```bash
python3 -m django --version
```

5. Django 웹앱 생성

```bash
django-admin startproject {mysite} {djangotutorial}
```

### 파일구조

기본 생성된 파일 구조

```shell
📂 djangotutorial/          # 루트 디렉토리
    ├── 📄 manage.py        # Django 프로젝트 관리 커맨드라인 유틸리티. 서버 실행, DB관리, 앱 생성 등 다양한 명령 실행
    └── 📂 mysite/          # 실제 프로젝트 설정 패키지
        ├── 📄 __init__.py  # Python 패키지임을 인식하게 해주는 빈 파일
        ├── 📄 settings.py  # 프로젝트의 모든 설정을 담고 있는 파일. DB설정, 설치된 앱 목록, 보안 설정 등
        ├── 📄 urls.py      # 프로젝트의 URL 패턴을 정의하는 파일
        ├── 📄 asgi.py      # ASGI(Asynchronous Server Gateway Interface) 호환 웹 서버의 진입점. 비동기 웹 서버를 위한 설정파일. 실시간 기능(웹소캣 등)을 구현할 때 사용
        └── 📄 wsgi.py      # WSGI(Web Server Gateway Interface) 호환 웹 서버의 진입점. 웹 서버와 Django 앱을 연결해주는 역할. 실제 서비스 배포할 때 주로 사용.
```

### 서버 실행

```bash
python3 manage.py runserver
```

기본설정 서버주소
`http://127.0.0.1:8000/` or `http://localhost:8000`

### 앱 생성

```bash
python3 manage.py startapp {polls}
```

```shell
polls/                  # 앱 디렉토리
    ├── __init__.py    # Python 패키지라고 알려주는 파일
    ├── admin.py       # 관리자 페이지 설정
    ├── apps.py        # 앱 설정
    ├── models.py      # 데이터베이스 모델
    ├── tests.py       # 테스트 코드
    ├── views.py       # 뷰 함수들
    └── migrations/    # 데이터베이스 변경사항 폴더
        └── __init__.py
```

### DB 테이블 생성

```bash
python manage.py migrate
```

마이그레이션 명령은 INSTALLED_APPS 설정을 살펴보고 mysite/settings.py 파일의 데이터베이스 설정과 앱과 함께 제공된 데이터베이스 마이그레이션에 따라 필요한 데이터베이스 테이블을 생성

1. Django의 데이터베이스 설계도(migration)를 실제 데이터베이스에 적용
2. 테이블 생성, 수정, 삭제 등의 작업을 자동으로 처리

- 사용자 인증 시스템 테이블 생성
- 관리자 페이지 테이블 생성
- 세션 관리 테이블 생성
- 기타 Django 기본 기능에 필요한 테이블들 생성

### 모델 생성

```python
from django.db import models

# Create your models here.

# Question 모델 (설문조사 질문)
class Question(models.Model):
  question_text = models.CharField(max_length=200) # 문자열을 저장하는 필드(최대 200자까지 저장 가능)
  pub_date = models.DateTimeField('date published') # 날짜와 시간을 저장하는 필드(관리자 페이지에서 보여질 이름)

# Choice 모델 (설문조사 선택지)
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 관계 설정. Question 모델과 연결. 삭제되면 CASCADE 옵션에 따라 관련된 Choice 객체도 삭제
  choice_text = models.CharField(max_length=200) # 문자열을 저장하는 필드(최대 200자까지 저장 가능)
  votes = models.IntegerField(default=0) # 정수를 저장하는 필드(기본값은 0)
```

### 테이블 구조 명칭

```shell
         열(Column) = 필드(Field)
         ↓        ↓         ↓
id       이름      나이       이메일
1        김철수    20        kim@email.com    ← 행(Row) = 레코드(Record)
2        이영희    22        lee@email.com    ← 행(Row) = 레코드(Record)
3        박지민    21        park@email.com   ← 행(Row) = 레코드(Record)
```

### 모델 활성화

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig", # 앱 추가
    #...
]
```

### DB 마이그레이션 파일 생성

```bash
python manage.py makemigrations polls
```

- makemigrations를 실행하면 Django에 모델을 변경했다는 사실과 변경 사항을 마이그레이션으로 저장하고 싶다는 사실을 알리는 것.
- 마이그레이션은 장고가 모델(데이터베이스 스키마)에 대한 변경사항을 저장하는 방식으로, 디스크 파일에 저장됨.
- polls/migrations/0001_initial.py 파일에서 읽을 수 있음.
- 마이그레이션을 실행하고 데이터베이스 스키마를 자동으로 관리하는 명령이 마이그레이트라고 함.

### SQL 반환 (읽기 전용)

sqlmigrate 명령은 마이그레이션 이름을 가져와서 해당 SQL을 반환함.

```bash
python manage.py sqlmigrate polls 0001
```

결과

```bash
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, # 자동 증가하는 기본 키
  "question_text" varchar(200) NOT NULL, # 질문 내용(200자 제한)
  "pub_date" datetime NOT NULL # 게시 날짜
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, # 자동 증가하는 기본 키
  "choice_text" varchar(200) NOT NULL, # 선택지 내용(200자 제한)
  "votes" integer NOT NULL, # 투표 수
  "question_id" bigint NOT NULL REFERENCES # Question 테이블과의 연결 고리
  "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED # 외래 키 제약조건의 검사 시점을 설정.
  # DEFERRABLE: 제약조건 검사를 나중으로 미룰 수 있다는 의미
  # INITIALLY DEFERRED: 트랜잭션 끝에서 제약조건을 검사한다는 의미
);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON # question_id 컬럼에 대한 인덱스를 생성하는 명령
  "polls_choice" ("question_id");
COMMIT;
```

** Note the following **

- 정확한 출력은 DB 마다 다름.
- 테이블명은 앱 이름(polls)와 모델의 소문자 이름(question, choice)와 결합하여 자동생성됨. (재정의 가능)
- 기본키(Primary keys) ID가 자동으로 추가됨. (재정의 가능)
- 컨벤션에 따라, Django가 외래 키 필드 이름에 `_id`를 추가함. (재정의 가능)
- 외래 키 관계는 FOREIGN KEY 제약 조건으로 명시적으로 만들어짐.
- DEFERRABLE 부분은 SQL에 트랜잭션이 끝날 때까지 외래키를 적용하지 않는다는 의미.

### 프로젝트 검사

```bash
python3 manage.py check
```

### 실제 DB 변경

```bash
python3 manage.py migrate
```

1. 하는 일

- 마이그레이션 파일의 내용을 실제 데이터베이스에 적용해요
- 테이블 생성, 수정, 삭제 등을 실행해요
- 데이터베이스 스키마를 변경해요

2. 실행 시점

- 새로운 마이그레이션 파일을 만든 후
- 프로젝트를 처음 설정할 때
- 다른 개발자의 마이그레이션을 받았을 때

3. 주요 동작 순서

- 1. 아직 적용되지 않은 마이그레이션 파일을 확인
- 2. 순서대로 마이그레이션 실행
- 3. 데이터베이스에 변경사항 적용
- 4. 마이그레이션 기록 업데이트

4. 주의사항

- 실행 전에 makemigrations가 필요함.
- 데이터베이스를 직접 변경하므로 신중히 실행해야 함.
- 가능하면 백업 후 실행하는 것이 좋음.
- makemigrations가 설계도를 그리는 거라면
  migrate는 실제로 건물을 짓는 것과 같다.

**모델 변경을 위한 3단계 가이드**

1. 모델 변경(models.py)
2. `python manage.py makemigrations`를 실행하여 해당 변경 사항에 대한 마이그레이션을 생성.
3. `python manage.py migrate`를 실행하여 해당 변경 사항을 데이터베이스에 적용,

### Django 환경이 설정된 파이썬 대화형 쉘

```bash
python manage.py shell
```

일반 `python` 실행과 다른점

- Django 프로젝트의 모든 설정이 로드된 상태로 시작
- 모델을 직접 import해서 사용 가능
- 데이터베이스 쿼리 테스트 가능
- API 테스트 가능

### Python 특별 메서드

```python
class MyClass:
    def __init__(self):      # 생성자
    def __str__(self):       # 문자열 표현
    def __len__(self):       # 길이 반환
    def __repr__(self):      # 개발자를 위한 문자열 표현
    def __add__(self):       # + 연산자 동작 정의
```

```python
def show_text(self):         # ❌ 파이썬이 특별 메서드로 인식 못함
    return self.question_text

def my_str(self):           # ❌ 역시 특별 메서드로 인식 못함
    return self.question_text

def __str__(self):          # ✅ 정상 동작!
    return self.question_text
```

**self**

- 클래스의 인스턴스(객체) 자기 자신을 가리킴
- 메서드가 호출될 때 자동으로 첫 번째 인수로 전달됨
