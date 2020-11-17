FROM python:3.6.9-slim-buster

RUN groupadd foo && \
    useradd -m -g foo foo

RUN pip install pymongo


USER foo

WORKDIR /home/foo

COPY --chown=foo:foo main.py .

ENTRYPOINT ["./main.py"]


