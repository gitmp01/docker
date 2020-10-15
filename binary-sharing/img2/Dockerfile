#
# Sample image to show how to share a
# binary between container:
# 
# Here we just copy the bash script `nice`
# in order to be called from the other 
# container.
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

COPY bin ./bin/

VOLUME ['./bin']