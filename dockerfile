#
# Python Dockerfile
#

# Base alpine image.
FROM python:3.5-alpine

MAINTAINER Jarvis Prestidge "jarvisprestidge@gmail.com"

# Adding requirement.txt
WORKDIR /app/hacker-news-scraper
ADD requirements.txt /app/hacker-news-scraper

# Udating dependancies
RUN apk update python3 pip3 && \
    pip3 install --no-cache-dir -r requirements.txt

# Adding source
ADD . /app/hacker-news-scraper

# Open a shell
ENTRYPOINT [ "/bin/ash" ]

