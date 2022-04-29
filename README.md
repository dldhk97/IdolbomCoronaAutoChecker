# IdolbomCoronaAutoChecker
![작업중](https://user-images.githubusercontent.com/20237869/154913463-8419239d-d1a0-4eab-84d2-62551327e98d.png)

아이돌봄 서비스 방문 전후 자가 건강 체크리스트 자동 체크 서비스입니다.

.env에 설정된 URL에 따라 구글 설문, 네이버 설문지를 자동으로 체크하여 제출합니다.

## Requirements
Google Chrome, python3.8

## How to use
```
# install requirements
python3 -m pip install -r requirements.txt

# setup .env
Open .env file and fill environment

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
    restart: unless-stopped
    ports:
      - "5000:5000"
    environment:
      - SERVER_IP=YOUR_SERVER_IP
      - SERVER_PORT=5000
      - SELF_CHECK_URL=https://abcdefg.com
      - TEACHER_NAME=홍길동
      - DO_NOT_SUBMIT=False
      - CHROME_DRIVER_URL=https://chromedriver.storage.googleapis.com/
      - CHROME_DRIVER_VERSION=Auto
      - HEADLESS_MODE=True
```

### run
```
docker-compose up -d
```
