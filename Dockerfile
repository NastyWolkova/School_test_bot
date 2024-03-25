FROM python:3.10

WORKDIR  /school_bot

COPY  ./requirements.txt ./

RUN pip3 install --upgrade setuptools && pip3 install -r ./requirements.txt

RUN chmod 755 .

COPY /. /.

CMD [ "python", "bot.py" ] 



