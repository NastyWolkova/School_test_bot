FROM python:3.10

WORKDIR  /school_test_bot

#копирование файла с зависимостями
COPY  ./requirements.txt ./    

#COPY  ./school_test_bot/pictures ./school_test_bot/pictures

#установка зависимостей
RUN pip3 install --upgrade setuptools && pip3 install -r ./requirements.txt

RUN chmod 755 .

COPY /. /.

CMD [ "python", "bot.py" ] 
