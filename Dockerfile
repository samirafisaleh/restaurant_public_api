FROM python:3.9.18-slim-bullseye

WORKDIR /

COPY django_run.sh gunicorn_run.sh django_run_migration.sh ./

RUN mkdir logging
RUN mkdir logging/gunicorn

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY source/ source/
RUN ./django_run_migration.sh dev


ENTRYPOINT [ "/bin/bash" ]