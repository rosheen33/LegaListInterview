# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /legalist
COPY requirements.txt /legalist/
RUN pip install -r requirements.txt
COPY . /legalist/

RUN apt-get update && apt-get -y install cron

# Copy hello-cron file to the cron.d directory
COPY crawler-cron /etc/cron.d/crawler-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crawler-cron

# Apply cron job
RUN crontab /etc/cron.d/crawler-cron
