#
# Sample image to show how to share a
# binary between container:
# 
# Here we call the script `nice` included
# in the img2 image container.
#
FROM python:alpine

MAINTAINER gitmp01 

LABEL version=0.0.1

RUN adduser \
        --disabled-password \
        foo \
        foo

USER foo

WORKDIR /home/foo

RUN mkdir bin

VOLUME ['./bin']

COPY script.py .

ENTRYPOINT ["python", "script.py"]