FROM python:latest

WORKDIR /python-app

COPY ./ /python-app

RUN pip install flask

ENTRYPOINT [ "python" ]

CMD [ "helloworld.py" ]