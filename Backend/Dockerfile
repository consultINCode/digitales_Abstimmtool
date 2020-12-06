FROM python:3.9-alpine

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]