# tdd-with-python

'(파이썬을 이용한)클린 코드를 위한 테스트 주도 개발' 책의 예제 공부

## 환경설정
* venv 환경 진입 : 
  ```batch 
  call venv\Scripts\activate 
  ```
* 필요 모듈 설치
  ```batch
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
* 작업완료후에는 빠져나온다.
  ```batch
  deactivate
  ```
* DB 업그레이드
  ```batch
  python manage.py makemigrations
  python manage.py migrate
  ```
  
## 기능 테스트
```batch
python manage.py test functional_tests
```
* 각 파일별로 실행하려면 다음과 같이 한다.
```batch
python manage.py test functional_tests._file_name_
```

## 유닛 테스트
python manage.py test lists
