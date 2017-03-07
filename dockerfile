#
# Python Dockerfile
#

# Base ubuntu image.
FROM ubuntu:16.04

MAINTAINER Jarvis Prestidge "jarvisprestidge@gmail.com"

# Update and install dependancies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
		git \
		build-essential \
		libssl-dev \
		libffi-dev \
		python-dev \
		python3-pip \
		python3-venv
		
# Create working dir
RUN mkdir environments && cd !$

# Clone my repo
RUN git clone https://github.com/JarvisPrestidge/hacker-news-scraper.git

RUN pip install -r /path/to/requirements.txt && echo python hackernews.py --posts <num of posts>

