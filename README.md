# IdolbomCoronaAutoChecker
아이돌봄 서비스 방문 전후 자가 건강 체크리스트 자동 체크 서비스

## Requirements
Google Chrome, python3.8

## How to use
```
# install requirements
python3 -m pip install -r requirements.txt

# setup .env
Open .env file and put environment data

# run
python3 main.py
```

## How to use with docker-compose

### build docker image
```
docker build -t dldhk97/idolbom_auto_checker:0.1 .
```

### create docker-compose.yml
```
version: "3"
services:
  idolbom_auto_checker:
    image: dldhk97/idolbom_auto_checker:0.1
    container_name: idolbom_auto_checker
    environment:
      - SERVER_IP=127.0.0.1
      - SERVER_PORT=5000
      - TEACHER_NAME=홍길동
      - DO_NOT_SUBMIT=False
```

### run
```
docker-compose up -d
```
