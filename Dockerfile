FROM python:3.7.1

COPY . /

WORKDIR /

RUN pip install -r /requirements.txt

ENTRYPOINT ["python"]

CMD ["manage.py", "run"]
