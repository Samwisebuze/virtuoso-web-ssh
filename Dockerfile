# slim includes gcc, which we need for building
FROM python:3.7-slim

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "run.py"]
