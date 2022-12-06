FROM python:3.9

WORKDIR /app
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
COPY requirements.txt .

RUN apt-get update && \
apt-get install -y vim && \
apt-get install -y locales locales-all && \
apt-get install -y cmake && \
pip install -U pip && \
pip install --no-cache-dir -r requirements.txt
