FROM python:3.10

WORKDIR  /app

#копирование файла с зависимостями
COPY  ./requirements.txt ./    

#установка зависимостей
RUN pip3 install --upgrade setuptools && pip3 install -r ./requirements.txt

RUN chmod 755 .

COPY  ./school_test_bot/pictures ./app/pictures

COPY /. /.

CMD [ "python", "bot.py" ] 
