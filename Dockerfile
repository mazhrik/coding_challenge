FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN mkdir sky_it_app
WORKDIR sky_it_app
COPY ./SKY_IT sky_it_app

RUN adduser -D user
USER user
