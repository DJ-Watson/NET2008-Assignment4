FROM python:3

ADD main.py /

RUN pip install pytz

CMD [ "python", "./main.py" ]