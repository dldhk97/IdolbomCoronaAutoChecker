FROM python:3.8

LABEL maintainer="dldhk97@naver.com"

COPY . /checker

WORKDIR /checker

# set timezone
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install korean locale
RUN apt-get update && apt-get install -y locales git
RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR.UTF-8

# install korean font
RUN mkdir /usr/share/fonts/nanumfont
RUN wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
RUN unzip NanumFont_TTF_ALL.zip -d /usr/share/fonts/nanumfont
RUN fc-cache -f -v

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# set display port to avoid crash
ENV DISPLAY=:99

# install requirements
RUN pip3 install -r requirements.txt

ENV SERVER_IP 127.0.0.1
ENV SERVER_PORT 5000
ENV SELF_CHECK_URL https://naver.me/abcdefg
ENV TEACHER_NAME 홍길동
ENV DO_NOT_SUBMIT False

CMD (sed -i '/^SERVER_IP=/c\SERVER_IP=$SERVER_IP' .env) && \
(sed -i '/^SERVER_PORT=/c\SERVER_PORT=$SERVER_PORT' .env) && \
(sed -i '/^SELF_CHECK_URL=/c\SELF_CHECK_URL=$SELF_CHECK_URL' .env) && \
(sed -i '/^TEACHER_NAME=/c\TEACHER_NAME=$TEACHER_NAME' .env) && \
(sed -i '/^DO_NOT_SUBMIT=/c\DO_NOT_SUBMIT=$DO_NOT_SUBMIT' .env)

ENTRYPOINT [ "python", "-u", "main.py" ]