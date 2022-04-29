FROM dldhk97/python-chrome-kor-docker:3.8_amd64

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

# install requirements
RUN pip3 install -r requirements.txt

ENV SERVER_IP 127.0.0.1
ENV SERVER_PORT 5000
ENV SELF_CHECK_URL https://naver.me/abcdefg
ENV TEACHER_NAME 홍길동
ENV DO_NOT_SUBMIT False
ENV CHROME_DRIVER_VERSION None

CMD (sed -i '/^SERVER_IP=/c\SERVER_IP=$SERVER_IP' .env) && \
(sed -i '/^SERVER_PORT=/c\SERVER_PORT=$SERVER_PORT' .env) && \
(sed -i '/^SELF_CHECK_URL=/c\SELF_CHECK_URL=$SELF_CHECK_URL' .env) && \
(sed -i '/^TEACHER_NAME=/c\TEACHER_NAME=$TEACHER_NAME' .env) && \
(sed -i '/^DO_NOT_SUBMIT=/c\DO_NOT_SUBMIT=$DO_NOT_SUBMIT' .env) && \
(sed -i '/^CHROME_DRIVER_VERSION=/c\CHROME_DRIVER_VERSION=$CHROME_DRIVER_VERSION' .env)

ENTRYPOINT [ "python", "-u", "main.py" ]