FROM python:3.10

WORKDIR  /app

COPY  ./requirements.txt ./

RUN pip3 install --upgrade setuptools

RUN pip3 install -r ./requirements.txt

RUN chmod 755 .

COPY /. /.





# FROM docker/whalesay:latest
# LABEL Name=testingbot Version=0.0.1
# RUN apt-get -y update && apt-get install -y fortunes
# CMD ["sh", "-c", "/usr/games/fortune -a | cowsay"]
